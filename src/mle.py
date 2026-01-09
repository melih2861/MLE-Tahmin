from .gamma import gamma_MLE
from .pareto import pareto_MLE
from .lomax import lomax_MLE

class DagilimAnalizcisi:
    def __init__(self, dosya_yolu):
        self.dosya_yolu = dosya_yolu

    def gamma_MLE(self):
        return gamma_MLE(self.dosya_yolu)

    def pareto_MLE(self):
        return pareto_MLE(self.dosya_yolu)

    def lomax_MLE(self):
        return lomax_MLE(self.dosya_yolu)
