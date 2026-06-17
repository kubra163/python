import pandas as pd
import numpy as np
import matplotlib.pyplot as plt             # burada da kütüphaneleri yükledim ama gerekli olanları
import seaborn as sns
import missingno as msno
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_excel("gorevler.xlsx", sheet_name="Sheet1")
print(df.head())                  #veri okuması yaptım burada

print("\n--- Veri tipi ve eksik değerler ---")
print(df.info())                      # burada da veri tiplerini ve eksik değerleri aldım

print("\n--- Temel istatistikler ---")
print(df.describe(include='all').T)                 # burada ki işlemde Sayısal ve kategorik sütunların özet istatistiklerini verdim


missing = df.isnull().sum().sort_values(ascending=False)                      #Hangi sütunda kaç eksik değer var onu buldum
missing_percent = (df.isnull().mean()*100).sort_values(ascending=False)
missing_df = pd.concat([missing, missing_percent], axis=1, keys=['count','percent'])
print("\n--- Eksik değerler ---")
print(missing_df)


msno.matrix(df, figsize=(10,4))
plt.show()


num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
num_cols = [c for c in num_cols if c != 'HastaNo']  
print("Sayısal sütunlar:", num_cols)

for col in num_cols:
    plt.figure(figsize=(6,3))
    sns.histplot(df[col].dropna(), bins=30, kde=True)           # burada da yukarıdaki kütüphanelerden biri olan seaborn kütüphanesi bir sayısal sutunda frekans dağılımını gösterir
    plt.title(f"{col} dağılımı")         #dropna yani buraya boş değerler atadım ve nan cıkmasonı sağladım
    plt.show()
    
    plt.figure(figsize=(6,2))
    sns.boxplot(x=df[col])
    plt.title(f"{col} boxplot")
    plt.show()


cat_cols = df.select_dtypes(include=['object']).columns.tolist()
print("Kategorik sütunlar:", cat_cols)

for col in cat_cols:
    print(f"\n--- {col} frekans tablosu ---")
    print(df[col].value_counts().head(20))
    
    plt.figure(figsize=(8,3))
    sns.countplot(y=df[col], order=df[col].value_counts().index[:20])
    plt.title(col)
    plt.show()

num_imputer = SimpleImputer(strategy='median')
df[num_cols] = num_imputer.fit_transform(df[num_cols])
                                        # devamlı               # bilinmiyor 
cat_imputer = SimpleImputer(strategy='constant', fill_value='unknown')     # şimdi buradaki işlemde tüm eksik değerler sabit bir değerle doldurdum aynı zamanda boş hücreler "unknown" ile doldurdum
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])


low_cardinality = [c for c in cat_cols if df[c].nunique() < 30]               #buradaki işlemde çok fazla kategori olmayan sütunlar seçtim
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')              #Kategorik değerler 0-1 sütunlarına çevridim ve ayrıca Eğitimde olmayan kategori ile karşılaşırsa hata veremez 
encoded = ohe.fit_transform(df[low_cardinality])
encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out(low_cardinality))

df = pd.concat([df.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)
df = df.drop(columns=low_cardinality)


scaler = StandardScaler()                #Sayısal değerler ortalaması 0 olan ve standart sapması 1 olacak şekilde normalize ettim
df[num_cols] = scaler.fit_transform(df[num_cols])

df.to_excel("gorevler_veri.xlsx", index=False)
print("İşlenmiş veriler kaydedildilmiştir: gorevler_veri.xlsx")





