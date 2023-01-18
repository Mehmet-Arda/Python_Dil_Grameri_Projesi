
# 191307001 - Mehmet Arda Yüksel - Python Final Proje

import random as rastgele

if __name__ == '__main__':

    class Palindrom:

        S=('0S0','1S1','0','1','ε')
        sonlu_karakterler=[]
        devamli_karakterler=[]
        baslangic_sembolu = 'S'
        epsilon='ε'

        print(f"CFG Gramer: {S}")

        for item in S:
            if item.find('S') == -1 and item != 'ε':
                sonlu_karakterler.append(item)
        print(f"Sonlu Karakterler: {sonlu_karakterler}")
        for item in S:
            if item.find('S') != -1:
                devamli_karakterler.append(item)
        print(f"Devamlı Karakterler: {devamli_karakterler}\n ")

        def rastgele_sonlu_devamli_karakter_sec(self,karakter_listesi):
            ri = rastgele.randint(0, len(karakter_listesi) - 1)
            return karakter_listesi[ri]

        def kuralli_sonlu_devamli_karakter_sec(self,karakter_listesi,bas,son,string):
            for i in range(0, len(karakter_listesi)):
                k = karakter_listesi[i]
                if k[0] == string[bas] and k[len(k) - 1] == string[son]:
                    return k

        def yazdir(self):
            print("Yazdırma işlemi gerçekleştiriliyor.")
            print(f"Üretilen Kelime: {self.uretilen_kelime}")
            print("\n")

        def uzunluk(self,p1,p2):
            print("\nUzunluk fonksiyonu çalıştırılıyor.")
            if p1[::-1]==p1 and p2[::-1]==p2:

                if len(p1)==len(p2):
                    print(f"{p1} {p2} Palindrom sayıları aynı uzunluktadır.\n")
                else:
                    print(f"{p1} {p2} Palindrom sayıları aynı uzunlukta değildir.\n")

            else : print(f"{p1} veya {p2} Palindrom değildir.\n")


        def test(self,string=''):

            self.uretilen_kelime =''
            #print(self.uretilen_kelime)

            #w=01110
            bas=son=0
            print("Test Fonksiyonu başlatılıyor.")
            print(f"Girilen Kelime: {string}")

            if string != string[::-1]:
                print(f'{string} Palindrom değildir.')
            else :
                if len(string) == 1:
                    i = self.sonlu_karakterler.index(string)
                    self.uretilen_kelime = self.sonlu_karakterler[i]

                elif len(string) > 1:

                    son=len(string)-1
                    while self.uretilen_kelime != string:

                        self.uretilen_kelime = self.kuralli_sonlu_devamli_karakter_sec(self.devamli_karakterler,bas,son,string)
                        bas = bas + 1
                        son = son - 1

                        print(self.uretilen_kelime)

                        while len(self.uretilen_kelime) < len(string):

                            self.uretilen_kelime=self.uretilen_kelime.replace('S',self.kuralli_sonlu_devamli_karakter_sec(self.devamli_karakterler,bas,son,string))
                            bas = bas + 1
                            son = son - 1
                            print(self.uretilen_kelime)

                        if len(self.uretilen_kelime) == len(string):

                            self.uretilen_kelime=self.uretilen_kelime.replace('S',self.kuralli_sonlu_devamli_karakter_sec(self.sonlu_karakterler,bas,son,string))

                        if len(self.uretilen_kelime) > len(string):

                            self.uretilen_kelime= self.uretilen_kelime.replace('S', self.epsilon)
                            self.uretilen_kelime = self.uretilen_kelime.replace('ε', '')
                            print('Epsilon karakteri silindi\n')

            print(self.uretilen_kelime)
            print("Test Fonksiyonu tamamlandı.")

        def rastgele_Palindrom_Kelime(self):

            uzunluk=rastgele.randint(1,21)

            palindrom_kelime=''
            epsilon = 'ε'
            print("Rastgele Palindrom Kelime oluşturuluyor.")

            while len(palindrom_kelime)!=uzunluk:

                if uzunluk == 1:

                    palindrom_kelime = self.rastgele_sonlu_devamli_karakter_sec(self.sonlu_karakterler)

                if uzunluk > 1:

                    palindrom_kelime = self.rastgele_sonlu_devamli_karakter_sec(self.devamli_karakterler)
                    print(palindrom_kelime)
                    while len(palindrom_kelime) < uzunluk :
                         palindrom_kelime = palindrom_kelime.replace('S',self.rastgele_sonlu_devamli_karakter_sec(self.devamli_karakterler))
                         print(palindrom_kelime)
                    if len(palindrom_kelime) == uzunluk :
                        palindrom_kelime = palindrom_kelime.replace('S',self.rastgele_sonlu_devamli_karakter_sec(self.sonlu_karakterler))

                    if len(palindrom_kelime) > uzunluk :
                        palindrom_kelime = palindrom_kelime.replace('S', epsilon)
                        print('Epsilon karakteri silindi\n')
                        palindrom_kelime = palindrom_kelime.replace('ε', '')


            print("Rastgele Palindrom Kelime oluşturuldu.")
            return palindrom_kelime


        def __init__(self):

            self.uretilen_kelime = self.rastgele_Palindrom_Kelime()

    p=Palindrom()
    p.yazdir()

    p.test('01110')
    p.uzunluk("000000","010010")



#------------------------------II.Kısım------------------------------------*

    class Unlemli_Palindrom(Palindrom):

        def test(self,string=''):

            self.uretilen_kelime =''
            bas=son=0

            print("Test Fonksiyonu başlatılıyor.")
            print(f"Girilen Kelime: {string}")


            if string != string[::-1]:
                print(f'{string} Palindrom değildir.')
            elif string.startswith('!')!=True or string.endswith("!")!=True:
                print(f"{string} Ünlemli Palindrom değildir.")
            else :
                string=string.replace('!','')


                if len(string) == 1:
                    i = self.sonlu_karakterler.index(string)
                    self.uretilen_kelime = self.sonlu_karakterler[i]

                elif len(string) > 1:

                    son=len(string)-1
                    while self.uretilen_kelime != string:

                        self.uretilen_kelime = self.kuralli_sonlu_devamli_karakter_sec(self.devamli_karakterler,bas,son,string)
                        bas = bas + 1
                        son = son - 1

                        print(self.uretilen_kelime)

                        while len(self.uretilen_kelime) < len(string):

                            self.uretilen_kelime=self.uretilen_kelime.replace('S',self.kuralli_sonlu_devamli_karakter_sec(self.devamli_karakterler,bas,son,string))
                            bas = bas + 1
                            son = son - 1
                            print(self.uretilen_kelime)

                        if len(self.uretilen_kelime) == len(string):

                            self.uretilen_kelime=self.uretilen_kelime.replace('S',self.kuralli_sonlu_devamli_karakter_sec(self.sonlu_karakterler,bas,son,string))

                        if len(self.uretilen_kelime) > len(string):

                            self.uretilen_kelime= self.uretilen_kelime.replace('S', self.epsilon)
                            self.uretilen_kelime = self.uretilen_kelime.replace('ε', '')
                            print('Epsilon karakteri silindi\n')

                self.uretilen_kelime=self.unlem_ekle(self.uretilen_kelime)
                print(self.uretilen_kelime)
                print("Test Fonksiyonu tamamlandı.")




        def unlem_ekle(self,palindrom_kelime):

            palindrom_kelime='!'+palindrom_kelime+'!'
            return palindrom_kelime


        def rastgele_Palindrom_Kelime(self):

            uzunluk=rastgele.randint(2,21)

            palindrom_kelime=''

            epsilon = 'ε'
            print("\nRastgele Ünlemli Palindrom Kelime oluşturuluyor.")

            while len(palindrom_kelime)!=uzunluk-2:

                if uzunluk == 2:
                    palindrom_kelime=self.unlem_ekle(palindrom_kelime)

                if uzunluk == 3:

                    palindrom_kelime = self.rastgele_sonlu_devamli_karakter_sec(self.sonlu_karakterler)
                    palindrom_kelime = self.unlem_ekle(palindrom_kelime)

                if uzunluk > 3:

                    palindrom_kelime = self.rastgele_sonlu_devamli_karakter_sec(self.devamli_karakterler)
                    print(palindrom_kelime)
                    while len(palindrom_kelime) < uzunluk-2 :
                         palindrom_kelime = palindrom_kelime.replace('S',self.rastgele_sonlu_devamli_karakter_sec(self.devamli_karakterler))
                         print(palindrom_kelime)
                    if len(palindrom_kelime) == uzunluk-2 :
                        palindrom_kelime = palindrom_kelime.replace('S',self.rastgele_sonlu_devamli_karakter_sec(self.sonlu_karakterler))

                    if len(palindrom_kelime) > uzunluk-2 :
                        palindrom_kelime = palindrom_kelime.replace('S', epsilon)
                        print('Epsilon karakteri silindi\n')
                        palindrom_kelime = palindrom_kelime.replace('ε', '')

            palindrom_kelime = self.unlem_ekle(palindrom_kelime)
            print("Rastgele Palindrom Kelime oluşturuldu.")
            return palindrom_kelime



    up=Unlemli_Palindrom()
    up.yazdir()
    up.test("!10101!")
    up.uzunluk("!111!","!010!")
