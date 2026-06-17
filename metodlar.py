#metodlar
"""
def metodadi(paramtre listesi):
kodlar
metodu cagırma
metodadı()
"""
# parametreli ve değer dondürmeyin bir metod olusturalım
# def selamlama(ad,soyad):
#     print("merhaba",ad,soyad)
#     print("dersimize hosgeldiniz")
#metodu calıstıralım
# selamlama("kübra","göksuguzel")
# selamlama("tomris","günaşan")
# ad=input("adınızı girin:")
# soyad=input("soyadınızı girin:")
# selamlama(ad,soyad)



#parametreli ve değer dödüren metod oluşturalım
# yarı zamanlı çalışan personelin maaşını hesaplayalım

# def maashesapla(saat, saatücreti):
#     maas=saat*saatücreti
#     return maas 
# def main():
#     saat=int(input("kaç saat çalıştınız:"))
#     saatücreti=int(input("saat ücreti nedir?:"))
#     print("maaşınız:",maashesapla(saat,saatücreti))
# main()




# bir öğrencinin not ortalamasını metod kullanarak bulalım
# def ortalama(vize,final):
#     return vize*0.4+final*0.6
# vize=int(input("vize notunuzu girin:"))
# final=int(input("final notunu girin:"))
# print("ortalamanız:",ortalama(vize,final))


# def ortalama(vize,final):
#     ort= vize*0.4+final*0.6
#     print("ortalamaız:",ort)
#     vize=int(input("vize notunuzu girin:"))
#     final=int(input("final notunu girin:"))
#     ortalama(vize,final)
#     print("ortalamanız:",ortalama(vize,final))
    

"""
a bankası
1-bakiye göruntüleme
2-para cek
3-para yatır
4-cıkış
işlem metodlar kullanarak yapalım
"""

bakiye=15000           #global değişken olarak tanımlayalım
def bakiye():
    global bakiye
    print("bakiyeniz:",bakiye)
def paracek(cekilenMiktar):
    global bakiye
    if bakiye >=cekilenMiktar:
        bakiye-=cekilenMiktar              # bakiye= bakiye-cekilenmiktar
        return bakiye
    else:
        print("yetersiz bakiye")
def parayatir(yatirilanMiktar):
    global bakiye
    bakiye+=yatirilanMiktar           #bakiye=bakiye-cekilenMiktar
    return bakiye
def Main():
    while True:
        print("1-bakiye\n2-para cek\n3-para yatır\n4-cıkış")
        secim=int(input("seçiminizi girin:"))
        if secim==1:
            bakiye()
        elif secim==2:
            cekilenMiktar=int(input("ne kadar para cekmek istiyorsunuz:"))
            print("yeni bakiyeniz:", paracek(cekilenMiktar))
        elif secim==3:
            yatirilanMiktar=int(input("ne kadar para yatırmak istiyorsunuz"))
            print("yeni bakiyeniz:" ,parayatir(yatirilanMiktar))
        elif secim==4:
            break  
            print("yanlıs secim")  
Main()
        