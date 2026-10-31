import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('diabetic_data.csv')

df = df.drop(columns=['readmitted']) #hedef değişken silindi.

hedef_sutun = "A1Cresult" #yeni hedef değişkenimiz seçildi.

df[hedef_sutun] = df[hedef_sutun].replace('None', np.nan) #None değerini boşa çeviriyoruz.
df[hedef_sutun] = df[hedef_sutun].map({'Norm': 0, '>7': 1, '>8': 1})# Normal olanları 0, anormal (>7 ve >8) olanları 1 yapıyoruz

# Eğitim için sayısal değerli sütunları alıyoruz.
df_sayisal = df.select_dtypes(include=['number'])

# Ayırma işlemleri yapıyoruz.
dolu_veri = df_sayisal.dropna()
eksik_veri = df_sayisal[df_sayisal[hedef_sutun].isna()]

# Lineer regresyon modeli
X_egitim = dolu_veri.drop(columns=[hedef_sutun])
y_egitim = dolu_veri[hedef_sutun]
model = LinearRegression()
model.fit(X_egitim, y_egitim)

# Test yapılmayan (boş olan hücrelerin) hastaların tahmini
X_tahmin = eksik_veri.drop(columns=[hedef_sutun])
tahminler = model.predict(X_tahmin).round()

tahminler = np.clip(tahminler, 0, 1) # 0 ve 1 olarak sınırlandırdık.
df.loc[df[hedef_sutun].isna(), hedef_sutun] = tahminler # Tahminler hücrelere konuldu.

print("Hücre doldurma sonrası A1Cresult sonuçları:")
print(df[hedef_sutun].value_counts())

print("\nSayısal verilerden oluşan tablo")
gosterilecek_sutunlar = list(X_egitim.columns) + [hedef_sutun]
print(df[gosterilecek_sutunlar].head(10))
