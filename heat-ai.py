import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class Ev:
    def __init__(self, odalar, sicaklik_ayarlayici):
        self.odalar = odalar
        self.sicaklik_ayarlayici = sicaklik_ayarlayici
        
    def sicaklik_olcumu(self):
        # Burada sıcaklık sensörlerinden veri okunur, şu anlık rastgele bir değer alıyoruz
        return {oda: 20 + (odalar.index(oda) * 2) for oda in self.odalar}
    
    def sicaklik_ayarla(self, hedef_sicaklik):
        sicakliklar = self.sicaklik_olcumu()
        X = np.array([list(sicakliklar.values())])  # Özellikler: Mevcut sıcaklıklar
        yeni_sicakliklar = self.sicaklik_ayarlayici.predict(X)
        for i, oda in enumerate(self.odalar):
            mevcut_sicaklik = sicakliklar[oda]
            yeni_sicaklik = yeni_sicakliklar[i]
            if yeni_sicaklik < mevcut_sicaklik:
                print(f"{oda} ısınmaya ihtiyaç duyuyor. Isıtıcıyı aç.")
                # Isıtıcı açma kodu buraya gelebilir.
            elif yeni_sicaklik > mevcut_sicaklik:
                print(f"{oda} serinlemeye ihtiyaç duyuyor. Klimayı aç.")
                # Klima açma kodu buraya gelebilir.
            else:
                print(f"{oda} sıcaklık hedefe ulaştı. Isıtıcıyı/klimayı kapat.")
                # Isıtıcı veya klimayı kapatma kodu buraya gelebilir.

# Veri toplama ve model eğitimi
def veri_toplama_ve_egitim():
    # Örnek veri oluşturalım
    # Özellikler: Mevcut sıcaklıklar
    X = np.random.randint(15, 30, size=(100, 4))
    # Etiketler: Hedef sıcaklıklar
    y = np.random.randint(18, 26, size=100)
    
    # Veriyi eğitim ve test setlerine bölelim
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Modeli eğitelim
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Modelin performansını değerlendirelim
    y_pred_train = model.predict(X_train)
    rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
    print(f"Eğitim seti RMSE: {rmse_train:.2f}")
    
    y_pred_test = model.predict(X_test)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
    print(f"Test seti RMSE: {rmse_test:.2f}")
    
    return model

# Örnek kullanım
if __name__ == "__main__":
    odalar = ["salon", "mutfak", "yatak_odasi", "cocuk_odasi"]
    ev = Ev(odalar, sicaklik_ayarlayici=veri_toplama_ve_egitim())
    hedef_sicaklik = 22
    ev.sicaklik_ayarla(hedef_sicaklik)
