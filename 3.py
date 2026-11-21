# abstract - mavhum
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def ovoz(self):
        pass

    def yugurish(self):
        pass


class Mushuk(Animal):
    def ovoz(self):
        print("Miyov")


m1 = Mushuk()
m1.ovoz()