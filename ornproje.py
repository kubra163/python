print("kütüphanye hoşgeldiniz:")
print("menü")
print("1-Tarih\n2-Bilim\n3-Roman\n4-çıkış")
secim=int(input("bir seçim yapınız:"))
if secim==1:
    Tarih=int(input("tarih kitabın fiyatı 50tl"))
elif secim==2:
    bilim=int(input("Bilim kitab ücreti 50 tl dir"))
elif secim==3:
    Roman=int(input("roma kitabın fiyatı 80tl dir"))
elif secim==4:
    print("çıkış yapanız")
else:
    print("yanlış secim")
    



