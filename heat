import time

class Ev:
    def __init__(self, odalar, hedef_sicaklik):
        self.odalar = odalar
        self.hedef_sicaklik = hedef_sicaklik
        
    def sicaklik_olcumu(self):
        # Burada sıcaklık sensörlerinden veri okunur, şu anlık rastgele bir değer alıyoruz
        return {oda: 20 + (odalar.index(oda) * 2) for oda in self.odalar}
    
    def sicaklik_ayarla(self):
        while True:
            sicakliklar = self.sicaklik_olcumu()
            print("Oda Sicakliklari:", sicakliklar)
            for oda, sicaklik in sicakliklar.items():
                if sicaklik < self.hedef_sicaklik:
                    print(f"{oda} ısınmaya ihtiyaç duyuyor. Isıtıcıyı aç.")
                    # Isıtıcı açma kodu buraya gelebilir.
                elif sicaklik > self.hedef_sicaklik:
                    print(f"{oda} serinlemeye ihtiyaç duyuyor. Klimayı aç.")
                    # Klima açma kodu buraya gelebilir.
                else:
                    print(f"{oda} sıcaklık hedefe ulaştı. Isıtıcıyı/klimayı kapat.")
                    # Isıtıcı veya klimayı kapatma kodu buraya gelebilir.
            time.sleep(60)  # 1 dakika bekleme süresi

# Örnek kullanım
if __name__ == "__main__":
    ev = Ev(["salon", "mutfak", "yatak_odasi", "cocuk_odasi"], hedef_sicaklik=22)
    ev.sicaklik_ayarla()
