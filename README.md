# Biometrija 

## Varaždin, 2025.
# SVEUČILIŠTE U ZAGREBU
# FAKULTET ORGANIZACIJE I INFORMATIKE
# V A R A Ž D I N


### Bruno Pičulin, Denis Šantek
## Studij: Informacijske tehnologije i digitalizacija poslovanja


## Identificiranje i verificiranje osoba u kriminalnim istragama

# PROJEKT



### Mentori/Mentorice:
Izv. prof. dr. sc. Petra Grd
Domagoj Tuličić, mag. inf.


## Uvod
Biometrija je postala jedan od najvažnijih, ako ne i najvažniji alat za provođenje kriminalističkih istraživanja. Biometrija je oduvijek bila jedan od najboljih načina za identifikaciju ljudi, obzirom da je većina biometrijskih karakteristika unikatna za svaku osobu. Međutim, njezina praktična primjena, pogotovo u kriminalističkom svijetu, raste tek u modernije doba, obzirom na sazrijevanje tehnologije za identifikaciju biometrijskih uzoraka. Taj pomak u tehnologiji je izrazito važan, obzirom da u kriminalistici svaki krivi korak može dovesti do katastrofalne greške koja može imati velik utjecaj na ljudske živote. Zato je jako bitno da se koriste metode koje su dosljedne i točne te da se može osigurati pravilna analiza i prikupljanje uzoraka te pravilno tumačenje rezultata. U ovom projektu ćemo analizirati neke od javno dostupnih baza podataka koje sadrže biometrijske podatke te ćemo obraditi analize metoda strojnog učenja u biometriji i napraviti primjenu jedne od metoda sa ciljem da naučimo i prikažemo koje od ovih metoda i baza imaju najviše prednosti, odnosno mana u korištenju u svrhe kriminalističke istrage.







## Biometrija

Općenito, biometrija je skup tehnika za autentifikaciju osobe prema njezinim jedinstvenim biološkim karakteristikama. Postoje razne biometrijske karakteristike koje se mogu analizirati. Najčešće su to: otisci prstiju ili dlanova, karakteristike lica ili očiju, glas, uho, potpis ili hod. Svaki od njih se može analizirati i prikupiti na više načina. Razlog zašto se koristi i istražuje toliko različitih karakteristika i tehnika je zato što variraju u vjerodostojnosti i konzistentnosti. Primjerice, identifikacija ljudi pomoću otiska prstiju je danas jedna od najpopularnijih metoda biometrije. Razlog je taj što je otisak prstiju različit kod svake osobe, postoji relativno malo prostora za pogrešku i prijevaru te se otisak prsta minimalno mjenja kroz život osobe. Još jedna bitna stavka je da je identifikacija kroz otisak prsta detaljno istraživano područje te je tehnologija koja omogućuje takav proces dovoljno jeftina da se može koristiti i u nekim masovno-dostupnim uređajima kao što su mobiteli. S druge strane, hod je isto karakterističan od osobe do osobe, no nije jako popularna tehnika autentifikacije. Razlog je što je razlike u hodu teže identificirati, mogu se mjenjati ozljedom ili prijevarom, vanjski faktori često mogu utjecati na hod osobe itd. Važno je napomenuti da iako su neke tehnike vjerodostojnije od drugih, ni jedna današnja biometrijska analiza nije savršena. Uz individualne nedostatke karakteristične za svaku tehniku, uvijek mogu postojati kvarovi ili određene vanjske smetnje, kao i namjerni pokušaji prijevare koje smanjuju vjerodostojnost rezultata. Biometrija ima sve širu primjenu u svijetu. Prosjećna osoba se večinom sa biometrijom susreće kada je u pitanju sigurnost, najčešće sigurnost podataka. U povijesti se sigurnost podataka najčešće osiguravala kroz lozinke i tokene. Najveći problemi kod takvih mjera sigurnosti su zaboravljena lozinka, gubitak tokena i općenita frustracija kompleksnošću. Biometrija osigurava da osoba ne mora ništa pamtiti ni nositi kako bi se autentificirala, takav pristup uvelike olakšava poštivanje sigurnosnih mjera, također dopušta da su mjere kompleksnije i sigurnije jer ih je lakše ispuniti. Provjera sigurnosti se može koristiti na poslu, u bankama, prilikom online transakcija itd. Biometrija je puno korištena i kao forenzički alat za rješavanje kompleksnih kriminalističkih slučaja, obzirom da jedinstvene karakteristike čovjeka omogućuju jednostavnu i preciznu identifikaciju, kako žrtava, tako i počitnitelja. Forenzička primjena u kriminalistici će biti detaljno obrađena u ovom radu.





## Forenzika

Forenzika je naziv za primjenu širokog spektra znanstvenih grana za utvrđivanje činjenica u kriminalističkim istraživanjima. U ovom radu ćemo se primarno baviti forenzičkim postupcima koji uključuju biometriju. U kriminalističkoj forenzici, biometrija se uglavnom koristi za identifikaciju osumnjičenika i žrtava, kao i za provjeru autentičnosti dokaza. Jasno je da u većini slučajeva forenzički rezultati imaju ogrome utjecaje na ljudske živote. To znači da foreznika smije u obzir uzeti samo one biometrijske karakteristike koje su maksimalno dosljedne, trajne i točne. Također, moraju se uzeti u obzir samo pravilno prikupljeni, analizirani i protumačeni uzorci. Uglavnom se analiziraju otisci (prstiju i dlanova) te analize karakteristika lica. Važno je napomenuti da se povremeno koriste i neke druge karatkeristike (obrisi stopala, karakteristike lica ili očiju...), no rijetko su jedinstveni faktor u odlučivanju. 

### Prikupljanje i analiza uzoraka

### Otisci prstiju i dlanova

Otisci koji se nađu otisnuti na nekoj površini nazivaju se latetni otisci. 
Kako bi se skupio uzorak latetnog otiska, najčešće se koriste crni prah ili ljepljiva traka. Crni prah se premaže preko površine za koju se sumnja da po sebi ima otiske prstiju. Ako uistinu ima latetnih otisaka na premazanoj površini, oni postanu okom vidljivi obzirom da se prah neravnomjerno rasporedi po otisku radi brazda i izbočenja. Nakon toga se prah otisne na ljepljivu traku što daje čist i precizan odraz stvarnog ostavljenog otiska. Pomoću ove metode može se povezati osumjičenika sa mjestom zločina, ali se ne može odrediti što je osoba radila tamo. Nedavno su znanstvenici u NIST-u (Nacionalna institucija standarda i tehnologije) razvili posebnu ljepljivu traku koja može prikupiti i određena kemijska svojstva. Uz pomoć takve trake i alata koji se zovi „mobilni spektrometar iona“, forenzičari mogu dobiti ideju o kemijskom sastavu na rukama osumnjičenih kada su bili na mjestu zločina ili malo ranije. Uz pomoć toga može se odrediti je li osoba pucala iz vatrenog oružja, je li konzumirala alkohol, koristi li kakve specifične preparate itd. Osim latetnih otisaka, forenzičari mogu uzeti otiske direktno od osobe. To je često potrebno ako netko osumnjičen nije u nikakvoj bazi podataka, ako se želi identificirati žrtva, ako je osumnjičena osoba prisutna i želi se potvrditi podudaranje sa latetnim otiscima itd. Takva radnja je moguća uz pomoć elektroničkih čitača čiji senzori imaju mogućnost očitanja udubina i izbočenja na prstu. Uređaj računa dimenzije i raspored izbočenja na prstu te ovinsno o izraženosti izbočine dodjeluje boju, uglavnom iz monokromatske skale boja. Nakon što je za svaki dio očitanog prsta dodjeljena boja, dobije se monokromatska slika na kojoj su jasno vidljive karakteristike otiska važne za autentifikaciju. Nakon što se prikupe uzorci, moraju se usporediti sa otiscima osumnjičenih ili mogućih žrtava. Najčešće se usporedbe odvijaju između uzetog otiska i preuzetog otiska iz neke baze podataka, a može se vršiti usporedba između latetnog otiska i otiska direktno uzetog od prisutnih osumnjičenih. Danas su baze podataka s otiscima prstiju izrazito opširne, obzirom da su večini država su državljani dužni skenirati otiske prilikom izrade identifikacijskih kartica. Postoje i baze podataka koje su dostupne i javnosti, više o tome u sljedećoj cijelini ovog rada. Ni jedna od navedenih metoda ne daje savršene rezultate. Prilikom korištenja ljepljive trake, moguće je da površina nije dobro prebrisana te se na traku zaljepi prljavština koja može omesti analizu. Također, sa trakom može biti problema ako je na istom mjestu više otisaka nastalo u slično vrijeme. Slično je moguće i sa elektroničkim čitačem. Dodatno, elektroničkon čitaču mogu smetati i određeni losioni ili znoj te visoke ili niske temperature. Naravno kod obje metode je moguća greška radi fizičkog kvara ili oštečenja.

## Karakteristike lica

Prikupljanje podataka karakteristika lica je relativno nova tehnologija, koja nastaje pojavom kamera i skenera. Unatoč tomu, identifikacija kroz karakteristike lica se koristi stoljećima, večinom kroz svjedoke koji pokušaju identificirati osumnjičene ili kroz ljudsko prepozvavanje osobe sa fotografija, crteža i videa. Danas se prepozvanje lica provodi uz pomoć algoritama koji uspoređuju podatke sa postojećim bazama podataka ili trenutnim snimkama video nadzora. Uzorci za prepoznavanje mogu biti dani na dva načina. Prvi i manje točan je kroz običnu fotografiju ili video. Glavni problem ove metode je da rezultati variraju obzirom na kvalitetu fotografije. Večina kriminalnih slučaja koji ima fotografske ili video dokaze, raspolaže sa dokazima snimljenim mobitelom od svjedoka zločina. Takvi mediji rijetko u potpunosti prikazuju karakteristike lica, pogotovo neke detaljnije. Kvalitetnije fotografije mogu donijeti bolje rezultate obzirom da današnje kamere mogu raditi fotografije dovoljno detaljne da prikažu svaki detalj lica. Glavni problem je što kvaliteta uređaja sa kojim se snima nije jedini faktor kvalitete. Na kvalietu slike mogu utjecati nemirnost ruke, loše osvjetljenje, brzina kretanja subjekta slikanja itd. Neki od tih faktora mogu čak i prevariti sustav prepoznavanja lica da prepozna krivu osobu. Primjerice, kod lošeg osvjetljenja mogu nastati sjene na licu koji sustav zamjeni za nepostojeće izbočine. Ova tehnika i dalje ima svoje koristi. Iako sustavi teško razaznaju dvoje ljudi sličnih karakteristika, vrlo su dobri u usporedbi. Druga metoda je analiza lica senzorima, koja funkcionira na sličan način kao analiza otisaka prstiju. Ona daje odlične rezultate koje sustav može prepoznati uz malo problema. Međutim nije lako obaviti takvo skeniranje, pogotovo ako se treba obaviti na brzinu ili na osobi koja nije voljna sudjelovati. Za sada je ta tehnologija najkorisnija u identifikaciji žrtava ili provjere alibija osumnjičenih, tako što se njihov sken lica uspoređuje sa snimkama kamera na području gdje tvrde da su se nalazili, dok se lice žrtava uspoređuje s bazom podataka. Usporedba može biti obavljena ručno, fizičkim pregledom snimaka. Međutim, danas postoje softveri za analizu koji mogu dane karakteristike pretražiti kroz snimke nadzornih kamera ili baze podataka, iako takvi softveri su generalno slabo razrađeni i mogu griješiti. Općenito se analize lica smatraju manje vjerodostnojnom od provjere otisaka prstiju, zato što se karatkeristike lica mjenjaju starenjem te zbog životnih navika, a mogu se mjenjati i namjerno, šminkom i operacijama. Također, kao što je prije spomenuto razni faktori, uključujući čak i izraz lica subjekta, mogu različito utjecati na algoritam. Ovi sustavi se još uvelike istražuju i razvijaju.


































## Biometrijske baze podataka

Ponekad je prikupljene podatke nemoguće direktno usporediti sa ljudima od interesa, zato je jako važno imati dobre baze podataka u kojima se mogu izvršiti razne provjere. Najveće baze podataka koje se koriste za potrebe kriminalističkih istraživanja su AFIS (Automated fingerprint identification system), NGI (Next genereation identification) i IBD (Interpol Biometric Databases). To su baze podataka koje održavaju FBI i Interpol, a namjena im je internacionalna. Uključuju nekoliko stotina milijuna biometrijskih zapisa. AFIS se koristi isključivo za otiske pristiju i dlanova, dok NGI uključuje i karakteristika lica i očiju. NGI je ujedno jedna i od najmodernijih baza podataka zato što uključuje do sad najnaprednije alogritme za pretraživanje baze, kao i algoritme za međusobno uspoređivanje uzoraka. IBD ima nešto slabije performanse i nešto manje zapisa od NGI-a, no široko je raspostranjen i sadrži bazu DNK podataka, s kojom NGI ne rasplaže. Uz AFIS i NGI još se često koriste AADHAAR, koji održava Indijska vlada i uključuje više vrsta biometrijskih podataka, te EURODAC, koji održava Europska Unija i koristi se isključivo za otiske prstiju. Baze podataka imaju različite razine ograničenja. Od do sad navedenih baza ni jedna od njih nije dostupna javnosti, isključivo je dostupna službenim državnim organizacijama i to ne uvijek svima. Primjerice, iako je AADHAAR najveća baza podataka na svijetu, rijetko se koristi za forenziku jer večina svjetskih država nema potpun pristup ovoj bazi. Iako se rijetko koriste za forenziku, postoje javno dostupne ili djelomično javno dostupne baze podataka kojima može pristupiti gotovo bilo tko. Djelomično javne baze su često namjenjene za istraživanja i zahtjevaju potpis posebnih dokumenata za ostvarenje pristupa. Mi čemo za ovaj rad detaljnije analizirati 3 javne baze i jednu djelomično javnu. Te baze su:

1.	FVC2004
2.	Neurotechnology Crossmatch
3.	COEP Palmprintdatabase
4.	FACES Database

FVC, Neurotechnology Crossmatch i COEP Palmprintdatabase su baze za otiske, a FACES je baza za karakteristike lica. Iako ćemo se u praktičnom dijelu rada baviti otiscima prstiju, smatramo da je važno analizirati barem jednu bazu sa karakteristikima lica, obzirom da je to jedna od glavnih biometrijskih karakteristika koje se koriste u forenzici. 


### 1.	FVC2004

FVC je prvo međunarodno natjecanje u izradi algoritama za autentifikaciju otisaka prstiju (i kasnije dlanova. Organizacija je osnovana 2000. godine od strane profesora Laboratorija biometrijskih sistema za Sveučilšta u Bolonji. Natjecanja se održavaju svake dvije godine i svi ostvareni rezultati, kao i svi podatci prikupljeni za analizu su javno objavljeni na službenim stranicama. Mi smo istraživali i koristili otiske iz natjecanja 2004. godine, razlog je taj što se od 2004. godine počinju koristiti slike bolje kvalitete i veće rezolucije, što znatno olakšava rad s istima. Ove baze su kompletno javne, iz tog razloga imaju ozbiljne mjere vezane uz zaštitu podataka. Otisci su označeni kodnim imenima, kako bi se spriječila zlouporaba podataka. Svako natjecanje sadrži nekoliko različitih baza, svaka od kojih se sastoji od 80 otisaka od 10 osoba. Rezultati istraživanja se po pravilu moraju objaviti u TIFF formatu, koji se može otvorit i na računalima bez nekog posebnog softwarea u obliku slike. Način prikupljanja otisaka je rijetko specificiran, a uglavnom su korišteni senzori koji nisu na javnom tržištu. Za bazu su kao dio natjecanja razvijeni algoritmi za 1-1 usporedbu. Nažalost obzirom da se radi o softwareu koji je razvijen prije više od 20 godina, nemoguće ga je pokrenuti na modernim operativnim sustavima.

### 2.	Neurotechnology Crossmatch

Neurotechnology je kompanija koja se bavi istraživanjem i integracijom biometrije u moderne tehnologije, sa naglaskom na umjetnu inteligenciju i robotiku. U svojim laboratorijima imaju neke od vodećih svijetskih stručnjaka za biometriju, robotiku i informatiku. Crossmatch je tehnologija koju su razvili za 1-1 usporedbu otisaka prstiju. Softver je namjenjen za komercijalno korištenje, ali nudi besplatne opcije za demonstraciju. Kao dio te demonstracije podjelili su dio baze podataka koju smo mogli analizirati i iskoristiti. Besplatna baza sadrži 408 uzoraka od 51 osobe. Za prikupljanje su korišteni „Verifier 300“ optički senzori koje je razvila ista firma. Otisci su viljdilvo bolje kvalitete od onih preuzetih sa FVC-a, što nije čudno obzirom da se ovdje radi o bazi za komercijalnu upotrebu. Puna verzija aplikacije pruža pristup bazi od nekoliko desetaka tisuća uzoraka te dopušta dodatno proširenje baze, također dopušta i pretraživanje jedan na više. Softver je i danas održavan i funkcionira na svim modernim platformama. Večinom se koristi za potrebe manjih organizacija koje koriste biometriju kao mjeru sigurnosti.



### 3.	COEP Palmprintdatabase

Coep (College of Enfineering Pune) je treći najstariji fakultet strojarstva na svijetu, osnovan 1854. godine u Engleskoj. Provodi mnoga istraživanja vezana uz integraciju biometrije u inženjerske prakse. Palmprintdatabase je baza podataka otisaka dlana, koja se satoji od 1344 uzorka prikupljena u svrhu istraživanja nove vrste bezkontaktnog senzora. Glavna zamisao iza razvoja senzora je da se očitanja mogu izvršiti bez nastajanja dodatnih bora zbog pritiska dlana na senzor. Za uzimanje otiska se koristi slična laserska tehnologija kao što se koristi kod očitanja dvda u računalima. Koristi se izrazito precizan, novo-razvijen laser kojem se obzirom na izbočenja mijenja valna duljina, integrirano računalo dodjeljuje svakoj razini izbočenja vrijednost na monokromatskoj skali boja te tako izrađuje sliku. Projekt nije bio pretjerano uspješan, što je vidljivo i na samoj bazi. Kako bi se umanjio rizik loše prikupljanja obrasca zbog pre velike udaljenosti od senzora, koristile su se slike velike rezolucije. Također, da bi se obrada na daljinu dovoljno dobro izvršila za autentifikaciju, slike su morale biti izrazito velike kvalitete. Ovakvi zahtjevi su zahtjevali izrazito jaka računala kako bi radila dovoljno brzo bez da uzrokuju nelagodu prilikom uzimanja uzorka. Uz to, na mašinu su znatno utjecali dodatni vanjski faktori kao osvjetljenje, temperatura i prljavština. Zbog svega toga konačni sistem je bio spor, skup te bi uzorci često ispadali mutni te nikad nije vidio komercijalne primjene, a baza je objavljena na stranici fakulteta kako bi se mogla koristiti za svrhe istraživanja, iako su uzorci relativno loše kvalitetes.

### 4.	FACES Database

FACES je baza podataka sastavljana od 2005.-2007. godine u svrhu istraživanja utjecaja izraza lica na komercijalne uređaja za biometrijsku autentifikaciju. Istraživanje je proveo Max Planc institut od Berlinu. Baza podataka sadrži slike od 171 različitog čovjeka, podjeljenih ravnomjerno prema dobi i spolu. Za svaku osobu napravljeno je 12 skenova, po dva za svaki promatran izraz lica (neutralni izraz, tuga, gađenje, strah, ljutnja i sreća). Faces je baza limitiranog pristupa, mali dio baze je dostupan europskim studentima uz registraciju i potpis izjave koja spriječava zloupotrebu baze. Podatci su visokokavalitetni i mogu se s lakoćom koristiti za bilo koju istraživačku, pa i komercijalnu svrhu, iako nisu namjenjeni za komercijalnu upotrebu. Ovo je ujedno i najveća javno dostupna baza podataka ne-alteriranih lica. Baze podataka sa karakteristikama lica rijetko su javne zato što predstavljaju sigurnosni rizik za ljude koji su bili dio istraživanja, iz tog razloga večina današnjih javnih baza koristi slike izmjenjene umjetnom inteligencijom. Rezultati istraživanja su se analizirali kroz 4 kategorije: „prema izrazu lica, prema dobi, prema razini privlačnosti te prema posebno izraženim karakteristikama lica“. Baza je kasnije nadograđena boljom kvalitetom slika i integracijom pretrage po kategorijama korištenim za analizu rezultata prvotnog istraživanja. Javna dostupna baza ne uključuje nikakve posebne algoritme za pretragu, no relativno je malog opsega (72 uzorka) pa samim time nije zahtjevna za pretragu.


#### Analiza metoda strojnog učenja

Strojno učenje igra ključnu ulogu u prepoznavanju, klasifikaciji i autentifikaciji ljudi na temelju biometrijskih karakteristika. Uvođenje strojnog učenja je znatno poboljšalo biometrijske sisteme zato što im omogučuje učenje i adaptaciju na jedinstvene karakteristike korisnika bez ručnih promjena i računanja. Na taj način su se kroz zadnjih nekoliko desetljeća uvelike poboljšali brzina i preciznost biometrijskih sustava. U ovom radu ćemo analizirati nekoliko najpoznatijih metoda strojnog učenja. 


#### Convolutional Neural Networks

CNN je tip strojnog učenja, kojeg karakterizira učenje pomoću takozvane filter ili kernel optimizacije. Takva vrsta optimizacije vrši se pomoću posebnih filtera koji miču neželjene šumove sa uzetih uzoraka i „pogađaju“ kako bi uzeti uzorci trebali izgledati bez njih. Smatra se standardom u industriji zbog vrhunske mogućnosti sinteze podataka koji su bili izgubljeni šumom. Posebno je prisutan u razvoju biometrijske tehnologije koja se primjenjuje na računalima. Općenito se koristi za prepoznavanje lica, očitanje otisaka prstiju ili dlana, analizu šarenice i analizu uzoraka žila. Uz to popularan je i van u biometrije u bilo kojoj disciplini koja zahtjeva ispravljanje teksta, slika i videa. Neke od popularnih arhitektura koje ga koriste su VGGNet (jednostavna arhitektura za prepoznavanje lica), InceptionNet (za procesiranje biometrijskih slika) i Mobilenet (za prepoznavanje biometrije u moilnim uređajima i računalima).

#### Recurrent Neural Networks

RNN je tip strojnog učenja koji je dizajniran za korištenje u situacijama kad je bitan slijed uzoraka. Poseban je od ostalih mreža zato što iste ulazne podatke koristi u više navrata, odnosno čuva ih u phorani. To je važan dio ovog tipa učenja zato što se svaki sljedeći ulaz uspoređuje sa onim prošlim te se tako mogu otkriti i analizirati promjene nastale vremenom ili uzorci koji mogu imati manje razlike prilikom svakog prikupljanja. Primjerice, RNN se često koristi za prepoznavanje govora ili potpisa, obzirom da ista osoba istu frazu može izgovoriti ili napisati malo drugačije svaki put. Iako je ovakav mehanizam koristan za gotovo bilo koju vrstu biometrijske autentifikacije, potreba za prostorom za pohranu čini ovaj sistem nešto sporijim i skupljim za implementaciju, pa se izbjegava ako nije potreban. Također, nije koristan kod karakteristika koje se puno mjenjaju ali kroz dugo vrijeme, primjerice lice, koje se mjenja kroz starenje ali kroz dulji niz godina. Razlog je što RNN sustavi imaju problem sa gubljenjem vjerodostojnosti starih uzoraka što češće se koriste za usporedbu s novim uzorcima. 

### Siamese Neural Networks

SNN, nekad znan kao i Twin Neural Network je tip strojnog učenja koji radi na principu spajanja dvaju ulaznih očitanja u jedan izlaz, kako bi se pokušale izbječi smetnje nastale zbog okoline. Prilikom analize ulaznog očitanja softver radi analizu koji dijelovi datoteke bi mogli uzrokovati najveći problem pri uspješnoj identifikaciji. Nakon toga,analiziraluči obje slike, računa kolika je minimalna mogućnost da se izbjegne takva smetnja. Temeljem tog izračuna, računalo napravi takozvanu „predsliku“ koja je direktan spoj obje slike. Za razliku od predslike, završni izlaz je kombinacija izrezaka različitih točaka sa svake slike. Računalo uzima područja koja je identificirao kao kritična te uzima uzorak iz one slike za koju smatra da ima manje šumova. Nakon što se izresci spoje, slika se uspoređuje sa predslikom i sa izračunatom mogučnošću izbjegavanaj smetnje. Izlaz mora biti veći od minimalne izračunate mogućnosti, a da pritom ne postane neusporedivo različit od predslike. Ova metoda je korisna za učenje algoritama gdje je dostupno malo uzoraka, primjerice u mobilnim uređajima koji imaju mogućnost prepoznavanja lica. Često se koristi i za autentifikaciju potpisa. 


#### Hibridi

Hibridni sustavi su vrste sustava koji koriste više različitih metoda strojnog učenja. Česti primjer su sustavi koji koriste CNN i SNN u kombinaciji.U ovom konkretnom primjeru, praksa je da se SNN koristi za prikupljanje više uzoraka i analizu kritičnih područja u uzorku, dok se kritična područja saniraju uz pomoć CNN-a. Na kraju SNN radi sintezu dva uzorka koji su bili obnovljeni. U nekim verzijama se CNN koristi samo na završni izlat SNN-a. Postoje razne mogućnosti, no večinom se se u široj javnosti hibridi ne primjenjuju. Razlog je što se biometrija u široj javnosti koristi za niske potrebe sigurnosti, primjerice na mobilnim uređajima. Za takve potrebe dovoljni su i pojedinačni sistemi, čija je implementacija jeftinija od hibrida. Hibridi se mogu češće vidjeti u područjima gdje je pogrešna autentifikacija ogroman rizik, primjerice u državnim službama.

Odabir baze
Pri odabiru baza smo koristili github repozitorij:
https://github.com/robertvazan/fingerprint-datasets?tab=readme-ov-file

Iz njega smo koristio bazu od „Neurotechnology UareU“ koja sadrži 7 različitih osoba te njihovih 10 prstiju te po svakom prstu 8 otisaka, formata TIFF te rezolucije 512 dpi. 

Priprema baze
Za pripremu baze smo posložili ih u datoteku zvanu “UareU_sample_DBTT”
te unutar nje više osoba je dobilo svoju datoteku. 
Podjela glasi:
Osoba_12 
Osoba_13
Osoba_17
Osoba_22
Osoba_27
Osoba_57
Osoba_76
 
Unutar svake datoteka pošto osoba ima 10 prstiju potrebno je rasporediti na 10 datoteka naziva od “Prst_1” do “Prst_10” i unutar njih 8 slika koje su naziva poput 012_1_3 (osoba 12, prst 1, slika 3)
 
 
Programski kod
Potreban nam je bio jedan od programskih jezika te smo se odabrali za python. 
Pyhton nam je omogućio razne mogučnosti kao što je upotreba raznih biblioteka i vanjskih resursa koje ćemo razraditi.
Kod se može pronaći na: https://github.com/bpiculin/BiometrijaBP
Kao što se može primjetiti u početku koda os i cv2 su korišteni, os nam služi za navigaciju po folderima i radi lakšeg dohvata datoteka iako smo precizno naznačili putanje i nazive.
Cv2 je biblioteka koja nam omogućuje obradu slika, konverziju boja, skaliranje, čitanje i te funkcije smo I koristili. Pretvaranje u RGB radi korištenja MobileNetV2 I resize-anje na dimenzije koje model može prihavtiti.
Nuphy je korište za rad s matricama, uz to je bilo potrebno skidanje raznih vanjskih biblioteka tijekom izrade projekta kako bi poboljšali preciznost. 
Tensorflow.keras, pretrenirani CNN model koji znatno ubrzava I poboljšava treniranje, pošto već zna osnovne vizualne značajke kao što su to linije, rubovi, kontrast.
Fine-tuning-om smo zamrzli donjih 100 slojeva MobileNeta kako bi zadržali opće naučene značajke dok su Gornji slojevi trenirani na specifičnom datasetu.
Također smo koristili ImageDataGenerator kako bi izbjegli prenaučenost, learning_rate podešen na 1e-5 nam služi kako nebi uništili njegove slojeve I pritom zadržali predhodno naučene
Onfusion_matrix i ConfusionMatrixDisplay
Za analizu točnosti modela i vizualizaciju gdje se točno model najviše griješi (koji prsti se najčešće miješaju).
To je važno za praktičnu primjenu jer nije dovoljno samo znati točnost već treba razumjeti i koje klase su problematične.
 

  
 






U kodu prvo se učitavaju slike otisaka iz foldera,pretvaranjem u RGB format i normalizacijom vrijednosti piksela na raspon od 0 do 1. Oznake (osobe) se kodiraju numerički, a zatim se podaci dijele na trening i test skupove u omjeru 80:20, a ne kao što je prije rečeno 6:2, ali ipak smo vodili računa o proporcionalnoj zastupljenosti svake klase (stratifikacija).
Kako bi se smanjila mogućnost prenaučenosti, koristi se augmentacija podataka - slike se rotiraju, pomiču i zumiraju nasumično, stvarajući varijacije podataka za treniranje. Zatim se MobileNetV2 učitava bez zadnjeg sloja (top layer) i dio njegovih ranih slojeva se "zamrzava" tj. ne trenira se, jer su oni već dobro naučili prepoznati osnovne vizualne obrasce (rubove, teksture).
Na MobileNetV2 dodaju se novi slojevi: globalno prosječenje, gusto povezani sloj od 256 neurona sa ReLU aktivacijom i dropout sloj koji sprječava prenaučenost, te na kraju sloj s brojem neurona jednakim broju klasa i softmax aktivacijom za klasifikaciju.
*MobileNetV2 je neuronska mreža za “računalni vid” odnosno dizajnirana posebno da bude lagana, brza I efikasna iako smo vršili pokretanje na osobnom računalu.
Model se trenira s malim learning rate-om (1e-5) kako bi se prilagodio postojećim naučenim težinama bez njihova narušavanja. Koristili smo epohe, odnosno iteracije prolaska cijelog treninga kroz skup podataka, 1:n. 
Nakon 50 epoha treniranja dobivamo rezultate treniranja i FAR,FRR. Točnost na test skupu iznosi oko 79,8%, što znači da model prilično dobro prepoznaje osobe prema otiscima, ali uvijek postoji mjesta za poboljšanje.

 
FAR (False Acceptance Rate) i FRR (False Rejection Rate) pokazuju sigurnost sustava: FAR od 20.19% znači da oko 20% lažno prihvaćenih podudaranja, a FRR od 4.81% znači da se oko 5% stvarnih korisnika pogrešno odbija.

 


Izvori
•	http://bias.csr.unibo.it/fvc2000/download.asp
•	https://www.neurotechnology.com/download.html#databases
•	https://www.coep.org.in/resources/coeppalmprintdatabase
•	https://faces.mpdl.mpg.de/imeji/
•	Materijali iz kolegija „Primjena biometrijskih tehnologija“, autorice izv.prof.dr.sc. Petre Grd
•	Fingerprint recognition, autora Jianjiang
•	https://www.britannica.com
•	https://www.geeksforgeeks.org/introduction-deep-learning/
•	https://www.ibm.com/think/topics/deep-learning
•	https://www.simplilearn.com
•	https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2
•	https://www.python.org/downloads/release/python-31011/
•	https://paperswithcode.com/method/mobilenetv2
•	https://www.tensorflow.org/install
