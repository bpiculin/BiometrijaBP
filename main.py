import os
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#Ucitavanje i priprema samih podataka
def load_and_preprocess(base_path):
    X, y = [], []
    for person in sorted(os.listdir(base_path)):
        person_path = os.path.join(base_path, person)
        if not os.path.isdir(person_path):
            continue
        for finger_num in range(1, 11):
            finger_path = os.path.join(person_path, f"Prst_{finger_num}")
            if not os.path.isdir(finger_path):
                continue
            for file in sorted(os.listdir(finger_path)):
                if file.endswith(".tif") or file.endswith(".tiff"):
                    img_path = os.path.join(finger_path, file)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        img = cv2.resize(img, (128, 128))  #povecana rezolucija
                        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                        img = img.astype('float32') / 255.0
                        X.append(img)
                        y.append(person)
    return np.array(X), np.array(y)

#db
base_path = r"C:\Users\bruno\Desktop\UareU_sample_DBTT"
X, y = load_and_preprocess(base_path)

#encoding i kategorije
le = LabelEncoder()
y_enc = le.fit_transform(y)
num_classes = len(le.classes_)
y_cat = to_categorical(y_enc, num_classes=num_classes)

#podjela na trening i test
X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2, random_state=42, stratify=y_enc)

#augmentacija kako bi smanjila prenaucenoost (CNN)
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.05,
    height_shift_range=0.05,
    zoom_range=0.1,
    horizontal_flip=False,  # necemo rotirati prste horizontalno
    fill_mode='nearest'
)
datagen.fit(X_train)

#fine-tuning MobileNetV2
base_model = MobileNetV2(input_shape=(128, 128, 3), include_top=False, weights='imagenet')
base_model.trainable = True

#zamrzni donjih ~100 slojeva (osnovni feature extractor)
#nauce rubove, kontrast, teksturu, linije i ostale karakteristike posto mobilenet vec je dio naucio iz drugih
for layer in base_model.layers[:100]:
    layer.trainable = False

#dodaj vlastite slojeve
inputs = Input(shape=(128, 128, 3))
x = base_model(inputs, training=True)
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
outputs = Dense(num_classes, activation='softmax')(x)

model = Model(inputs, outputs)

#kompajliranje s manjim learning rateom, ne zelimo unistiti njegove slojeve pritom zadrzati predhodno naucene
model.compile(optimizer=Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

#treniranje
history = model.fit(
    datagen.flow(X_train, y_train, batch_size=32),
    validation_data=(X_test, y_test),
    epochs=50
)

#evaluacija
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.4f}")

#predikcije
y_pred_probs = model.predict(X_test)
y_pred_classes = np.argmax(y_pred_probs, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

#konfuzijska matrica(sklearn.metrics) vrati 2D matricu
cm = confusion_matrix(y_true_classes, y_pred_classes)
ConfusionMatrixDisplay(cm, display_labels=le.classes_).plot(cmap='Blues', xticks_rotation=45)
plt.title("Konfuzijska matrica")
plt.show()
#matrica nam prikazuje koji se prsti najcesce mjesaju

#FAR,FRR
total_tests = np.sum(cm)
correct_predictions = np.trace(cm)
false_accepts = total_tests - correct_predictions
false_rejects = np.sum((cm.sum(axis=1) - np.diag(cm)) > 0)

FAR = false_accepts / total_tests
FRR = false_rejects / total_tests

print(f"\nFalse Acceptance Rate (FAR): {FAR:.4f}")
print(f"False Rejection Rate (FRR): {FRR:.4f}")
