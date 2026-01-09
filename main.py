<<<<<<< HEAD
import src.MLEtahmin as mle
import os

print("--- AKTÜERYA MLE TAHMİN SİSTEMİ ---")

# --- ADIM 1: Girdileri En Başta Al ---
dosya_yolu = input("Dosya Adı (örn: Kitap1.csv): ").strip()
dagilim_tercihi = input("Dağılım Adı (gamma, pareto, lomax): ").lower().strip()

# Dosya kontrolü
if not os.path.exists(dosya_yolu):
    print(f"\nHATA: '{dosya_yolu}' dosyası bulunamadı.")
    exit()

try:
    # --- ADIM 2: Analizciyi Başlat ---
    analizci = mle.DagilimAnalizcisi(dosya_yolu)
    
    # --- ADIM 3: Doğrudan İlgili Dağılıma Git ---
    print(f"\n>> {dagilim_tercihi.upper()} dağılımı için hesaplama yapılıyor...\n")
    
    sonuc = None

    if dagilim_tercihi == "gamma":
        sonuc = analizci.gamma_MLE()
        
    elif dagilim_tercihi == "pareto":
        sonuc = analizci.pareto_MLE()
        
    elif dagilim_tercihi == "lomax":
        sonuc = analizci.lomax_MLE()
        
    else:
        print("HATA: Geçersiz dağılım ismi girdin! (gamma, pareto veya lomax yazmalısın)")
        exit()

    # --- ADIM 4: Sonucu Göster ---
    # Senin Class yapın zaten sözlük (dict) döndürdüğü için direkt basabiliriz
    if isinstance(sonuc, dict):
        print("-" * 30)
        print(f"SONUÇLAR ({sonuc['Dagilim']})")
        print("-" * 30)
        for anahtar, deger in sonuc.items():
            # Sayıları daha okunaklı yapmak için formatlama
            if isinstance(deger, float):
                print(f"{anahtar:<15}: {deger:.4f}")
            else:
                print(f"{anahtar:<15}: {deger}")
        print("-" * 30)
    else:
        # Eğer hata mesajı döndüyse (string olarak)
        print(f"BİR SORUN OLUŞTU: {sonuc}")

except Exception as e:
    print(f"Beklenmeyen Hata: {e}")
=======
import os
import sys

# src klasörünü Python path'e ekle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_DIR)

from mle import DagilimAnalizcisi

print("--- AKTÜERYA MLE TAHMİN SİSTEMİ ---")

# --- ADIM 1: Kullanıcı girdileri ---
dosya_yolu = input("Dosya Adı (örn: Kitap1.csv): ").strip()
dagilim_tercihi = input("Dağılım Adı (gamma, pareto, lomax): ").lower().strip()

if not os.path.exists(dosya_yolu):
    print(f"HATA: '{dosya_yolu}' dosyası bulunamadı.")
    sys.exit()

try:
    analizci = DagilimAnalizcisi(dosya_yolu)

    print(f"\n>> {dagilim_tercihi.upper()} dağılımı için hesaplama yapılıyor...\n")

    if dagilim_tercihi == "gamma":
        sonuc = analizci.gamma_MLE()
    elif dagilim_tercihi == "pareto":
        sonuc = analizci.pareto_MLE()
    elif dagilim_tercihi == "lomax":
        sonuc = analizci.lomax_MLE()
    else:
        print("HATA: Geçersiz dağılım ismi girdin!")
        sys.exit()

    if isinstance(sonuc, dict):
        print("-" * 35)
        print(f"SONUÇLAR ({sonuc['Dagilim']})")
        print("-" * 35)
        for k, v in sonuc.items():
            if isinstance(v, float):
                print(f"{k:<20}: {v:.4f}")
            else:
                print(f"{k:<20}: {v}")
        print("-" * 35)
    else:
        print("HATA:", sonuc)

except Exception as e:
    print("Beklenmeyen hata:", e)
>>>>>>> 1ae5344 (İlk sürüm - Aktüeryal MLE Tahmin Sistemi)
