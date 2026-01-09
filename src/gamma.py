import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln

#Gamma

#ONEMLİ NOT:csv dosyamizin ustune sag tik yapip yolu kopyalayıp ayıracları  
# " \ " seklini " / " sekline cevirip veri dosyamizi olusturuyoruz.


veri_dosya_gamma="C:/Users/melih/OneDrive/Desktop/testMLE/Gamma_TEST.csv"

veri_tab_gamma=pd.read_csv(veri_dosya_gamma, sep=';', decimal=',')


#eger veriler 2. sutunda ise 0 kısmını 1 yapın.
gamma_veri= veri_tab_gamma.iloc[:, 0].values.astype(float)





def Gamma_MLE(veri):
    """
    Gamma dağılımı için MLE
    """

    def negatif_log_olabilirlik(parametreler):
        alfa, beta = parametreler

#alfa ve beta negatif degerler alamaz.
        if alfa <= 0 or beta <= 0:
            return np.inf

        n = len(veri)

        oyf = (n*(alfa*np.log(beta)-gammaln(alfa))+(alfa-1)*np.sum(np.log(veri))-beta*np.sum(veri))

        return -oyf

    # Moment tahmini ile başlangıç
    ortalama = np.mean(veri)
    varyans = np.var(veri)

    baslangic = [ortalama ** 2 / varyans,ortalama / varyans]

    sonuc = minimize(negatif_log_olabilirlik,baslangic,method="L-BFGS-B",bounds=((1e-6, None), (1e-6, None)))

    alfa, beta = sonuc.x

    return {"Alfa": float(alfa),"Beta": float(beta),"Beklenen Deger": float(alfa / beta)}



Gamma_MLE(gamma_veri)