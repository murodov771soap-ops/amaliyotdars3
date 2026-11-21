class BankAccount:
    LIMIT = 5_000_000

    def __init__(self, owner, card_number, pin, balance=0):
        self.owner = owner
        self.card_number = card_number
        self.__pin = pin
        self.__balance = max(0, balance)
        self.__tarix = []
        self.__xato_soni = 0
        self.__bloklangan = False
        self.__bugun_yechildi = 0

    def __pin_tekshir(self, pin):
        if self.__bloklangan:
            print("Karta bloklangan!")
            return False
        if pin == self.__pin:
            self.__xato_soni = 0
            return True
        self.__xato_soni += 1
        if self.__xato_soni >= 3:
            self.__bloklangan = True
            print("3 marta xato PIN! Karta bloklandi.")
        else:
            print(f"PIN kod noto'g'ri! ({3 - self.__xato_soni} urinish qoldi)")
        return False

    def show_info(self):
        holat = "Bloklangan" if self.__bloklangan else "Faol"
        print(f"Mijoz: {self.owner} | Karta: {self.card_number} | Holat: {holat}")

    def check_balance(self, pin):
        if self.__pin_tekshir(pin):
            print(f"Balans: {self.__balance} so'm")

    def deposit(self, amount):
        if self.__bloklangan:
            print("Karta bloklangan!")
            return
        if amount <= 0:
            print("Summa musbat bo'lishi kerak!")
            return
        self.__balance += amount
        self.__tarix.append(f"+{amount} so'm kirim (Balans: {self.__balance})")
        print(f"{amount} so'm qo'shildi. Yangi balans: {self.__balance} so'm")

    def withdraw(self, amount, pin):
        if not self.__pin_tekshir(pin):
            return
        if amount <= 0:
            print("Summa musbat bo'lishi kerak!")
        elif amount > self.__balance:
            print("Hisobda mablag' yetarli emas!")
        elif self.__bugun_yechildi + amount > self.LIMIT:
            print("Kunlik limit (5 000 000 so'm) oshib ketdi!")
        else:
            self.__balance -= amount
            self.__bugun_yechildi += amount
            self.__tarix.append(f"-{amount} so'm chiqim (Balans: {self.__balance})")
            print(f"{amount} so'm yechildi. Qolgan balans: {self.__balance} so'm")

    def change_pin(self, old_pin, new_pin):
        if self.__pin_tekshir(old_pin):
            self.__pin = new_pin
            self.__tarix.append("PIN kod o'zgartirildi")
            print("PIN kod yangilandi.")

    def transfer(self, qabul_qiluvchi, amount, pin):
        if not self.__pin_tekshir(pin):
            return
        if amount <= 0:
            print("Summa musbat bo'lishi kerak!")
        elif amount > self.__balance or self.__bugun_yechildi + amount > self.LIMIT:
            print("Mablag' yetarli emas yoki kunlik limit oshdi!")
        else:
            self.__balance -= amount
            self.__bugun_yechildi += amount
            qabul_qiluvchi.__balance += amount
            self.__tarix.append(f"-{amount} so'm -> {qabul_qiluvchi.owner}")
            qabul_qiluvchi.__tarix.append(f"+{amount} so'm <- {self.owner}")
            print(f"{self.owner} -> {qabul_qiluvchi.owner}\n{amount} so'm o'tkazildi.")
            print(f"{self.owner} balansi: {self.__balance}\n{qabul_qiluvchi.owner} balansi: {qabul_qiluvchi.__balance}")

    def show_history(self, pin):
        if self.__pin_tekshir(pin):
            if not self.__tarix:
                print("Tarix bo'sh.")
            for qator in self.__tarix:
                print(qator)