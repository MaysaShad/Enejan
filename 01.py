class Sirket:
    def __init__(self, ad):
        self.ad = ad
        self.calisma = True
    
    def program(self):
        saýlaw = self.menuSecim()

        if saýlaw == 1:
            self.calisanEkle()
        elif saýlaw == 2:
            self.işgärÇykar()
        elif saýlaw == 3:
            ýyllyk_görmek = input("Ýyllyk ýagdaýda görmek isleýärsiňizmi? (hawa/ýok): ")
            if ýyllyk_görmek == "hawa":
                self.berilmeliAýlykGör(hasap="ýyllyk")
            else:
                self.berilmeliAýlykGör()
        elif saýlaw == 4:
            self.maaslariVer()
        elif saýlaw == 5:
            self.masrafGir()

    def menuSecim(self):
        try:
            saýlaw = int(input(f""""****{self.ad} Ulgamyna hoş geldiňiz ****\n
            1-Calisan Ekle\n2-Calisan Cikar\n3-Verilek Maas Goster\n4-Maaslari ver\n5-Masraf gir\n\nSaýlawyňyzy giriziň: """))
            while saýlaw < 1 or saýlaw > 6:
                saýlaw = int(input("1-6 aralygynda saýlaw giriziň: "))
            return saýlaw
        except ValueError:
            print("Nädogry giriş. San giriziň.")
            return self.menuSecim()
        
    def calisanEkle(self):
    
        ad = input("Işgäriň adyny giriziň: ")
        soyad = input("Işgäriň soyadyny giriziň: ")
        yas = input("Işgäriň ýaşyny giriziň: ")
        cinsiyet = input("Işgäriň cinsiyetini giriziň: ")
        maas = input("Işgäriň maasny giriziň: ")

        with open("calisanlar.txt", "r") as dosya:
            calislanListesi = dosya.readlines()
    

        if len(calislanListesi) == 0:
            id = 1
        else:
            with open("calisanlar.txt", "a+") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open("calisanlar.txt", "a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id, ad, soyad, yas, cinsiyet, maas))
        

    
    def işgärÇykar(self):
        try:
            with open("calisanlar.txt", "r") as dosya:
                calisanlar = dosya.readlines()
            
            görünerIşgärler = []
            for calisan in calisanlar:
                görünerIşgärler.append(" ".join(calisan[:-1].split(" - ")))

            for idx, calisan in enumerate(görünerIşgärler, start=1):
                print(f"{idx}) {calisan}")

            saýlaw = int(input(f"Çykarmak isleýän işgäriň nomerini giriziň (1-{len(görünerIşgärler)}): "))
            while saýlaw < 1 or saýlaw > len(görünerIşgärler):
                saýlaw = int(input(f"(1-{len(görünerIşgärler)}) aralygynda nomer giriziň: "))

            calisanlar.pop(saýlaw - 1)

            täzeIşgärler = []
            for sanaw, calisan in enumerate(calisanlar, start=1):
                täzeIşgärler.append(f"{sanaw}) {calisan.split(') ')[1]}")

            with open("calisanlar.txt", "w") as dosya:
                dosya.writelines(täzeIşgärler)
            print("Işgär üstünlikli çykaryldy.")
        except Exception as e:
            print(f"Ýalňyşlyk ýüze çykdy: {e}")

    def berilmeliAýlykGör(self, hasap="aýlyk"):
        try:
            with open("calisanlar.txt", "r") as dosya:
                calisanlar = dosya.readlines()

            maaslar = []

            for calisan in calisanlar:
                maaslar.append(int(calisan.split("-")[-1]))
            
            if hasap == "aýlyk":
                print(f"Bu aýda berilmeli umumy aýlyk: {sum(maaslar)} TMT")
            elif hasap == "ýyllyk":
                print(f"Bu ýylda berilmeli umumy aýlyk: {sum(maaslar) * 12} TMT")
        except Exception as e:
            print(f"Ýalňyşlyk ýüze çykdy: {e}")
        
    def maaslariVer(self):
        try:
            with open("calisanlar.txt", "r") as dosya:
                calisanlar = dosya.readlines()

            maaslar = []

            for calisan in calisanlar:
                maaslar.append(int(calisan.split("-")[-1]))
            toplamMaas = sum(maaslar)

            try:
                with open("butce.txt", "r") as dosya:
                    butce = int(dosya.read().strip())
            except FileNotFoundError:
                butce = 0

            butce -= toplamMaas

            with open("butce.txt", "w") as dosya:
                dosya.write(str(butce))

            print(f"Aýlyklar berildi. Galan býudjet: {butce} TMT")
        except Exception as e:
            print(f"Ýalňyşlyk ýüze çykdy: {e}")

    def masrafGir(self):
        try:
            masraf = int(input("Girizjek masraf mukdaryňyzy giriziň: "))
            with open("butce.txt", "r") as dosya:
                butce = int(dosya.read().strip())
            
            butce -= masraf

            with open("butce.txt", "w") as dosya:
                dosya.write(str(butce))

            print(f"Masraf üstünlikli girizildi. Galan býudjet: {butce} TMT")
        except Exception as e:
            print(f"Ýalňyşlyk ýüze çykdy: {e}")


sirket = Sirket("Mert Mekatronik")

while sirket.calisma:
    sirket.program()
