class Telefon:
    def __init__(self, model, zaryad=50):
        self.model = model
        self.__zaryad = max(0, min(100, zaryad))

    def get_zaryad(self):
        return self.__zaryad

    def zaryadlash(self, miqdor):
        if miqdor <= 0:
            print(f"[{self.model}] Xatolik: Zaryadlash miqdori musbat bo'lishi kerak!")
            return
        self.__zaryad = min(100, self.__zaryad + miqdor)
        print(f"[{self.model}] +{miqdor}% zaryadlandi. Hozirgi zaryad: {self.__zaryad}%")

    def ishlatish(self, miqdor):
        if miqdor <= 0:
            print(f"[{self.model}] Xatolik: Ishlatish miqdori musbat bo'lishi kerak!")
            return
        self.__zaryad = max(0, self.__zaryad - miqdor)
        print(f"[{self.model}] -{miqdor}% ishlatildi. Hozirgi zaryad: {self.__zaryad}%")



tel1 = Telefon("iPhone 17 Pro Max", 95)
tel2 = Telefon("Samsung S24", 70)

tel1.zaryadlash(50)   
tel1.ishlatish(35)    

tel2.ishlatish(40)    
tel2.zaryadlash(-10)  
tel2.ishlatish(0)    
