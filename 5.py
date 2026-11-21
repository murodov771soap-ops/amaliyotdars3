class Talaba:
    def __init__(self, ism, baho=0):
        self.ism = ism
        self.__baho = 0
        self.set_baho(baho)

    def get_baho(self):
        return self.__baho

    def set_baho(self, yangi_baho):
        if 0 <= yangi_baho <= 100:
            self.__baho = yangi_baho
        else:
            print(f"Ogohlantirish ({self.ism}): Baho 0 dan 100 gacha bo'lishi kerak! ({yangi_baho} qabul qilinmadi)")


talaba1 = Talaba("Ali", 100)
talaba2 = Talaba("Vali", 100)

print(f"{talaba1.ism}ning bahosi: {talaba1.get_baho()}")
talaba1.set_baho(95)
print(f"{talaba1.ism}ning yangi bahosi: {talaba1.get_baho()}")

talaba1.set_baho(120)
talaba2.set_baho(-15)
print(f"{talaba2.ism}ning bahosi o'zgarmadi: {talaba2.get_baho()}")
