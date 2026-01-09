import pandas as pd
import numpy as np
from scipy.optimize import minimize

def pareto_MLE(dosya_yolu):
    df = pd.read_csv(dosya_yolu, sep=';', decimal=',', header=None)
    veri = df.iloc[:, 0].values.astype(float)
    veri = veri[veri > 0]

    def negatif_log_olabilirlik(param):
        alfa, xm = param
        if alfa <= 0 or xm <= 0:
            return np.inf
        n = len(veri)
        oyf = n*np.log(alfa) + n*alfa*np.log(xm) - (alfa+1)*np.sum(np.log(veri))
        return -oyf

    ortalama = np.mean(veri)
    xm0 = np.min(veri)
    baslangic = [1.0, xm0]

    sonuc = minimize(negatif_log_olabilirlik, baslangic, method="L-BFGS-B", bounds=((1e-6,None),(1e-6,None)))
    alfa, xm = sonuc.x

    return {
        "Dagilim": "Pareto",
        "Alfa": float(alfa),
        "Xm": float(xm),
        "Beklenen Deger": xm*alfa/(alfa-1) if alfa > 1 else np.inf
    }
