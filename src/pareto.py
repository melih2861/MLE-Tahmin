import pandas as pd
import numpy as np
from scipy.optimize import minimize


#Pareto


#ONEMLİ NOT:csv dosyamizin ustune sag tik yapip yolu kopyalayıp ayıracları  
# " \ " seklini " / " sekline cevirip veri dosyamizi olusturuyoruz.

veri_dosya_pareto = "C:/Users/melih/OneDrive/Desktop/testMLE/Pareto_TEST.csv"

veri_tablosu = pd.read_csv(veri_dosya_pareto, sep=';', decimal=',')
pareto_veri = veri_tablosu.iloc[:, 0].values.astype(float)




def Pareto_MLE(veri):
    """
    Pareto Tip-I için MLE
    """

    xm = np.min(veri)

    def negatif_log_olabilirlik(parametreler):
        alfa = parametreler[0]

        if alfa <= 0:
            return np.inf

        n = len(veri)

        log_l= (n*np.log(alfa)+n*alfa*np.log(xm)-(alfa+1)*np.sum(np.log(veri)))

        return -log_l

    sonuc = minimize(negatif_log_olabilirlik,[2.0],method="L-BFGS-B",bounds=((1e-6, None),))

    alfa = sonuc.x[0]

    if alfa > 1:
        beklenen = (alfa * xm) / (alfa - 1)
    else:
        beklenen = np.inf

    return {"Xm": float(xm),"Alfa": float(alfa),"Beklenen Deger": float(beklenen)}


Pareto_MLE(pareto_veri)




