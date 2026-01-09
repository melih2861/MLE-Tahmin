import pandas as pd
import numpy as np
from scipy.optimize import minimize

def lomax_MLE(dosya_yolu):
    df = pd.read_csv(dosya_yolu, sep=';', decimal=',', header=None)
    veri = df.iloc[:, 0].values.astype(float)
    veri = veri[veri > 0]

    def negatif_log_olabilirlik(param):
        alfa, beta = param
        if alfa <= 0 or beta <= 0:
            return np.inf
        n = len(veri)
        oyf = n*np.log(alfa) - n*np.log(beta) - (alfa+1)*np.sum(np.log(1+veri/beta))
        return -oyf

    ortalama = np.mean(veri)
    beta0 = np.mean(veri)/2
    baslangic = [1.0, beta0]

    sonuc = minimize(negatif_log_olabilirlik, baslangic, method="L-BFGS-B", bounds=((1e-6,None),(1e-6,None)))
    alfa, beta = sonuc.x

    return {
        "Dagilim": "Lomax",
        "Alfa": float(alfa),
        "Beta": float(beta),
        "Beklenen Deger": beta/(alfa-1) if alfa > 1 else np.inf
    }
