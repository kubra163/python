# ilk şifre yapma projem
sifre=input("sekiz karakterli bir şifre giriniz;")
if len(sifre) <8:
    print("şifre çok kısa o yüzden sekiz karakterli olmalı;")
kucuk_karakter=any(c.islower() for c in sifre)
buyuk_karakter=any(c.isupper() for c in sifre)
rakam=any(c.isdigit() for c in sifre)
ozel=any(not c.isalnum() for c in sifre)
print("küçük harfi girin:", kucuk_karakter)
print("büyük harfi girin:", buyuk_karakter)
print("rakamları girin:" ,rakam)
print("ozel karakter girin:", ozel)

