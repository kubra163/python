#liste=["pembe","mor","lacivert","sarı","yeşil","turuncu","gri"]
#print(liste)
#liste=["pembe","mor","lacivert","sarı","yeşil","turuncu","gri"]
#liste.extend(["siyah","beyaz"])
#print(liste)
#liste=["pembe","mor","lacivert","sarı","yeşil","turuncu","gri"]
#liste.remove("yeşil")
#print(liste)
#liste=["pembe","mor","lacivert","sarı","yeşil","turuncu","gri"]
#liste.remove("yeşil")
#print(liste)
#liste=["pembe","mor","lacivert","sarı","yeşil","turuncu","gri"]
#print(liste.index('yeşil'))




market = {
    "Gıda": {"Ekmek": [50, 5], "Pirinç": [30, 20], "Makarna": [40, 15], "su": [80,2], "cay": [85,20] },
    "Temizlik": {"Deterjan": [20, 30], "Sabun": [50, 5], "Çamaşır Suyu": [15, 25], "torsil": [90,60], "bulaşık detarjyan": [100,50]},
    "Meyve/Sebze": {"Elma": [100, 10], "Domates": [80, 8], "Patates": [70, 7], "muz": [60,12], "portakal": [13,2]}
}

def urun_listele():
    print("\nKategoriler ve Ürünler:")
    for kategori, urunler in market.items():
        print(f"{kategori}:")

        for urun, bilgiler in urunler.items():
            print(f"  {urun} - Stok: {bilgiler[0]}, Fiyat: {bilgiler[1]} TL")

def stok_guncelle(kategori, urun, adet):
    if kategori in market and urun in market[kategori]:
        if market[kategori][urun][0] >= adet:
            market[kategori][urun][0] -= adet
            print(f"{adet} adet {urun} alındı. Kalan stok: {market[kategori][urun][0]}")
            return market[kategori][urun][1] * adet  # Toplam fiyat
        else:
            print("Yeterli stok yok!")
            return 0
    else:
        print("Geçersiz kategori veya ürün!")
        return 0

def toplam_fiyat_hesapla():
    urun_listele()
    toplam_fiyat = 0
    while True:
        secim = input("\nAlışverişe devam etmek için 'E' yazın, çıkmak için 'H' yazın: ").strip().upper()
        if secim == "H":
            break
        kategori = input("Kategori seçin (Gıda, Temizlik, Meyve/Sebze): ").strip()
        urun = input("Ürün seçin: ").strip()
        adet = int(input("Kaç adet almak istiyorsunuz?: "))
        toplam_fiyat += stok_guncelle(kategori, urun, adet)
    print(f"\nToplam ödenecek tutar: {toplam_fiyat} TL")

