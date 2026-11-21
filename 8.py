from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def harakatlanish(self):
        pass
class Mashina(Transport):
    def __init__(self, nom):
        self.nom = nom

    def harakatlanish(self):
        print(f"{self.nom} avtomobili asfalt yo'lda dvigatel yordamida tez harakatlanmoqda.")

class Velosiped(Transport):
    def __init__(self, nom):
        self.nom = nom

    def harakatlanish(self):
        print(f"{self.nom} velosipedi veloyo'lakda pedal aylantirish orqali harakatlanmoqda.")
try:
    t = Transport()
except TypeError as e:
    print("Xatolik kuzatildi:", e)

transportlar = [
    Mashina("Chevrolet Gentra"),
    Velosiped("Stels Navigator")
]

for tr in transportlar:
    tr.harakatlanish()

