class Odam:
    def __init__(
            self, ism, yosh,
            daromad, passport):
        self.ism = ism
        self.yosh = yosh
        self._daromad = daromad
        self.__passport = passport

    def get_passport(self):
        return self.__passport

    def set_passport(self, yangi):
        self.__passport = yangi

o1 = Odam(
    "Abbos", 14, 5_000_000,
    "AB1239876"
)
# print(o1.__passport)
print(o1.get_passport())
        