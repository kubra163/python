dict={
    "ali":32,
    "zehra":30,
    "emir":33,
    "serra":14
}

print(dict)
print(type(dict))
# anahtar yazdıralım
print("anahtarlar(keys):")
for i in dict.keys():
    print(i)
# değerleri yazdıralım
print("items:")
for i in dict.items():
    print(i)
    
    
#---------------------
isimler=["Ahmet", "gül", "canan", "gamze"]
maaslar=[50000,45000,30000,70000]
# bu iki listeyi dictionary veri yapısına dönüştürelim
personel_bilgileri=dict(zip(isimler,maaslar))
print(personel_bilgileri)
print(type(personel_bilgileri))
for i, j in personel_bilgileri.items():
    print(i,j)
# maasları %20 arttıralım
print("---------")
for i, j in personel_bilgileri.items():
    print(i, j+(j*0.20))
    
    
#---------------------

