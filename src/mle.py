import pandas as pd
import numpy as np
from scipy.stats import lomax, gamma, pareto

class DagilimAnalizcisi:
    def __init__(self, veri_yolu):
        print(f"--- Veri Yükleniyor: {veri_yolu} ---")
        
        # 1. Dosyayı Okuma (Ayraç ne olursa olsun okumaya çalışır)
        try:
            # engine='python' ve sep=None, ayırıcıyı (virgül mü noktalı virgül mü) otomatik algılar
            df = pd.read_csv(veri_yolu, sep=None, engine='python', header=None)
        except Exception as e:
            print(f"Dosya okuma hatası: {e}")
            self.veri = pd.Series([])
            return

        # 2. Veriyi Temizleme ve Sayıya Çevirme
        # İlk sütunu alıyoruz (0. sütun)
        ham_veri = df.iloc[:, 0]
        
        # Metinleri sayıya çevir (Hata verenleri NaN yapar)
        self.veri = pd.to_numeric(ham_veri, errors='coerce')
        
        # Boş (NaN) verileri sil
        self.veri = self.veri.dropna()
        
        # --- KRİTİK NOKTA: SIFIRLARI TEMİZLEME ---
        toplam_veri = len(self.veri)
        self.veri = self.veri[self.veri > 0] # Sadece 0'dan büyükleri al
        kalan_veri = len(self.veri)
        
        if toplam_veri != kalan_veri:
            silinen = toplam_veri - kalan_veri
            print(f"DİKKAT: {silinen} adet veri '0' veya negatif olduğu için silindi.")
            print("Gamma ve Pareto dağılımları için veriler 0'dan büyük olmalıdır.")

        print(f"Analize Hazır Veri Sayısı: {len(self.veri)}")

        # İstatistikler
        self.ortalama = self.veri.mean()
        self.varyans = self.veri.var()

    def temel_istatistikleri_getir(self):
        return {"Ortalama": self.ortalama, "Varyans": self.varyans}

    def gamma_MLE(self):
        if len(self.veri) == 0: return "Veri Yok!"
        try:
            # floc=0 diyerek verinin 0'dan başladığını varsayıyoruz
            alpha, loc, scale = gamma.fit(self.veri, floc=0)
            return {
                "Dagilim": "Gamma", 
                "Alpha (Şekil)": alpha, 
                "Theta (Ölçek)": scale, 
                "Beklenen Deger": gamma.mean(alpha, loc=loc, scale=scale)
            }
        except Exception as e:
            return f"Gamma Hesaplanamadı: {e}"

    def pareto_MLE(self):
        if len(self.veri) == 0: return "Veri Yok!"
        try:
            alpha, loc, scale = pareto.fit(self.veri, floc=0)
            return {
                "Dagilim": "Pareto", 
                "Alpha (Şekil)": alpha, 
                "Xm (Ölçek)": scale, 
                "Beklenen Deger": pareto.mean(alpha, loc=loc, scale=scale)
            } 
        except Exception as e:
            return f"Pareto Hesaplanamadı: {e}"

    def lomax_MLE(self):
        if len(self.veri) == 0: return "Veri Yok!"
        try:
            alpha, loc, scale = lomax.fit(self.veri, floc=0)
            return {
                "Dagilim": "Lomax", 
                "Alpha (Şekil)": alpha, 
                "Beta (Ölçek)": scale, 
                "Beklenen Deger": lomax.mean(alpha, loc=loc, scale=scale)
            }
        except Exception as e:
            return f"Lomax Hesaplanamadı: {e}"