class OmborMahsuloti:
    def __init__(self, nom, miqdor=0):
        self.nom = nom
        self.__miqdor = miqdor if miqdor >= 0 else 0

    def get_miqdor(self):
        return self.__miqdor

    def mahsulot_qoshish(self, son):
        if son <= 0:
            print(f"[{self.nom}] Xatolik: Qo'shiladigan son 0 dan katta bo'lishi kerak!")
            return
        self.__miqdor += son
        print(f"[{self.nom}] +{son} ta qo'shildi. Omborda jami: {self.__miqdor} ta.")

    def mahsulot_sotish(self, son):
        if son <= 0:
            print(f"[{self.nom}] Xatolik: Sotiladigan son 0 dan katta bo'lishi kerak!")
            return
        if son > self.__miqdor:
            print(f"[{self.nom}] Xatolik: Omborda yetarli mahsulot yo'q (Mavjud: {self.__miqdor} ta, so'raldi: {son} ta).")
            return
        self.__miqdor -= son
        print(f"[{self.nom}] {son} ta sotildi. Omborda qoldi: {self.__miqdor} ta.")

mahsulot1 = OmborMahsuloti("Noutbuk", 10)
mahsulot2 = OmborMahsuloti("Sichqoncha", 5)
mahsulot1.mahsulot_qoshish(5)
mahsulot1.mahsulot_sotish(8)
mahsulot2.mahsulot_sotish(10)  
mahsulot2.mahsulot_qoshish(-3) 
mahsulot2.mahsulot_sotish(0)   