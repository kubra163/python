bakiye=15000           #global değişken olarak tanımlayalım
def Bakiye():
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
            Bakiye()
        elif secim==2:
            cekilenMiktar=int(input("ne kadar para cekmek istiyorsunuz:"))
            print("yeni bakiyeniz:",paracek(cekilenMiktar))
        elif secim==3:
            yatirilanMiktar=int(input("ne kadar para yatırmak istiyorsunuz"))
            print("yeni bakiyeniz:",parayatir(yatirilanMiktar))
        elif secim==4:
            break  
            print("yanlıs secim")  
Main()