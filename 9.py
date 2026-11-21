from abc import ABC, abstractmethod

class Tolov(ABC):
    @abstractmethod
    def tolash(self, summa):
        pass


class NaqdTolov(Tolov):
    def tolash(self, summa):
        if summa <= 0:
            print("Xatolik: To'lov summasi 0 dan katta bo'lishi kerak!")
            return
        print(f"Naqd pul orqali {summa:,} so'm to'lov muvaffaqiyatli qabul qilindi.")

class KartaTolovi(Tolov):
    def tolash(self, summa):
        if summa <= 0:
            print("Xatolik: To'lov summasi 0 dan katta bo'lishi kerak!")
            return
        print(f"Bank kartasi orqali {summa:,} so'm yechildi va to'lov tasdiqlandi.")

naqd = NaqdTolov()
karta = KartaTolovi()

tolovlar = [
    (naqd, 150000),
    (karta, 420000),
    (naqd, 0),
    (karta, -50000)
]

for usul, summa in tolovlar:
    usul.tolash(summa)
