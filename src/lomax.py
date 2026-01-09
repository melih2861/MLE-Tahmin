import pandas as pd
import numpy as np
from scipy.optimize import minimize


#Lomax

#ONEMLİ NOT:csv dosyamizin ustune sag tik yapip yolu kopyalayıp ayıracları  
# " \ " seklini " / " sekline cevirip veri dosyamizi olusturuyoruz.

veri_dosya_lomax = "C:/Users/melih/OneDrive/Desktop/testMLE/Lomax_TEST.csv"

veri_tablosu = pd.read_csv(veri_dosya_lomax, sep=';', decimal=',')
lomax_veri = veri_tablosu.iloc[:, 1].values.astype(float)






def Lomax_MLE(veri):
    """
    Lomax dağılımı için MLE
    """

    def negatif_log_olabilirlik(parametreler):
        alfa, lamda = parametreler

#alfa ve lamda 0 dan kucuk olamaz.
        if alfa <= 0 or lamda <= 0:
            return np.inf

        n = len(veri)

        log_l = (n * np.log(alfa)- n * np.log(lamda)- (1 + alfa) * np.sum(np.log(1 + veri / lamda)))

        return -log_l

    baslangic = [2.0, np.mean(veri)]

    sonuc = minimize(negatif_log_olabilirlik,baslangic,method="L-BFGS-B",bounds=((1e-6, None), (1e-6, None)))

    alfa_hat, lamda_hat = sonuc.x

    if alfa_hat > 1:
        beklenen = lamda_hat / (alfa_hat - 1)
    else:
        beklenen = np.inf

    return {"Alfa": float(alfa_hat),"Lamda": float(lamda_hat),"Beklenen Deger": float(beklenen)}


Lomax_MLE(lomax_veri)