import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = fetch_openml(name='heart-statlog', version=1, as_frame=False, parser='auto')
X = data.data
y_orijinal = data.target

siniflar = np.unique(y_orijinal)
y = np.where(y_orijinal == siniflar[1], 1, 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

birler_train = np.ones((X_train_scaled.shape[0], 1))
X_train_son = np.concatenate((birler_train, X_train_scaled), axis=1)

birler_test = np.ones((X_test_scaled.shape[0], 1))
X_test_son = np.concatenate((birler_test, X_test_scaled), axis=1)

def sigmoid(z):
    z = np.clip(z, -250, 250)
    return 1 / (1 + np.exp(-z))

def hata_hesapla(w, x, y):
    n = len(y)
    tahmin = sigmoid(x @ w)
    eps = 1e-15
    hata = (1/n) * np.sum(y * np.log(tahmin + eps) + (1 - y) * np.log(1 - tahmin + eps))
    return -hata

def gradyan_hesapla(w, x, y):
    n = len(y)
    tahmin = sigmoid(x @ w)
    grad = (1/n) * x.T @ (tahmin - y)
    return grad

w = np.zeros(X_train_son.shape[1])
iterasyon_sayisi = 1000 
ogrenme_orani = 0.1 
kayip_gecmisi = []

for i in range(iterasyon_sayisi):
    g = gradyan_hesapla(w, X_train_son, y_train)
    mevcut_hata = hata_hesapla(w, X_train_son, y_train)
    
    w = w - ogrenme_orani * g
    kayip_gecmisi.append(mevcut_hata)

tahmin_olasiliklari = sigmoid(X_test_son @ w)
y_tahmin = (tahmin_olasiliklari >= 0.5).astype(int)

acc = accuracy_score(y_test, y_tahmin)
prec = precision_score(y_test, y_tahmin)
rec = recall_score(y_test, y_tahmin)
f1 = f1_score(y_test, y_tahmin)

print("Lojistik Regresyon Sonuçları:")
print("-" * 50)
print(f"Accuracy  : {acc:.4f}")
print(f"Precision : {prec:.4f}")
print(f"Recall    : {rec:.4f}")
print(f"F1 Score  : {f1:.4f}")

plt.plot(kayip_gecmisi)
plt.title("Eğitim Sürecindeki Hata Değişimi")
plt.xlabel("İterasyon Sayısı")
plt.ylabel("Kayıp")
plt.grid(True)
plt.show()