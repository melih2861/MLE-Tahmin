from src.mle import DagilimAnalizcisi
import os
import sys

print("--- AKTÜERYA MLE TAHMİN SİSTEMİ ---")

dosya_yolu = input("Dosya Adı (örn: Kitap1.csv): ").strip()
dagilim_tercihi = input("Dağılım Adı (gamma, pareto, lomax): ").lower().strip()

if not os.path.exists(dosya_yolu):
    print(f"HATA: '{dosya_yolu}' dosyası bulunamadı.")
    sys.exit()

analizci = DagilimAnalizcisi(dosya_yolu)

if dagilim_tercihi == "gamma":
    sonuc = analizci.gamma_MLE()
elif dagilim_tercihi == "pareto":
    sonuc = analizci.pareto_MLE()
elif dagilim_tercihi == "lomax":
    sonuc = analizci.lomax_MLE()
else:
    print("Geçersiz dağılım!")
    sys.exit()

print("-"*35)
print(f"SONUÇLAR ({sonuc['Dagilim']})")
print("-"*35)
for k, v in sonuc.items():
    if isinstance(v, float):
        print(f"{k:<20}: {v:.4f}")
    else:
        print(f"{k:<20}: {v}")
print("-"*35)
