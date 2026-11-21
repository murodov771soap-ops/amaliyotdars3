from datetime import date


class BankAccount:
    KUNLIK_LIMIT = 5_000_000
    MAKS_XATO_PIN = 3

    def __init__(self, owner: str, card_number: str, pin: int, balance: int = 0):
        if balance < 0:
            raise ValueError("Boshlang'ich balans 0 dan kam bo'lishi mumkin emas!")
        self.owner = owner
        self.card_number = card_number
        self.__pin = pin
        self.__balance = balance
        self.__tarix: list[str] = []
        self.__xato_urinishlar = 0
        self.__bloklangan = False
        self.__oxirgi_yechish_sanasi: date | None = None
        self.__bugun_yechilgan = 0

    def __kunlik_limitni_yangila(self) -> None:
        bugun = date.today()
        if self.__oxirgi_yechish_sanasi != bugun:
            self.__oxirgi_yechish_sanasi = bugun
            self.__bugun_yechilgan = 0

    def __pin_tekshir(self, pin: int) -> bool:
        if self.__bloklangan:
            print("Karta bloklangan!")
            return False
        if pin == self.__pin:
            self.__xato_urinishlar = 0
            return True
        self.__xato_urinishlar += 1
        if self.__xato_urinishlar >= self.MAKS_XATO_PIN:
            self.__bloklangan = True
            print("PIN kod 3 marta noto'g'ri kiritildi! Karta bloklandi.")
        else:
            qolgan = self.MAKS_XATO_PIN - self.__xato_urinishlar
            print(f"PIN kod noto'g'ri! ({qolgan} ta urinish qoldi)")
        return False

    def show_info(self) -> None:
        holat = "Bloklangan" if self.__bloklangan else "Faol"
        print(f"Mijoz: {self.owner}")
        print(f"Karta: {self.card_number}")
        print(f"Holat: {holat}")

    def check_balance(self, pin: int) -> None:
        if self.__pin_tekshir(pin):
            print(f"Balans: {self.__balance} so'm")

    def deposit(self, amount: int) -> bool:
        if self.__bloklangan:
            print("Karta bloklangan!")
            return False
        if amount <= 0:
            print("Pul miqdori musbat bo'lishi kerak!")
            return False
        self.__balance += amount
        self.__tarix.append(f"+{amount} so'm kirim | Balans: {self.__balance} so'm")
        print(f"{amount} so'm hisobga qo'shildi.")
        print(f"Yangi balans: {self.__balance} so'm")
        return True

    def withdraw(self, amount: int, pin: int) -> bool:
        if not self.__pin_tekshir(pin):
            return False
        if amount <= 0:
            print("Pul miqdori musbat bo'lishi kerak!")
            return False
        if amount > self.__balance or (self.__balance - amount) < 0:
            print("Hisobda yetarli mablag' mavjud emas!")
            return False
        self.__kunlik_limitni_yangila()
        if self.__bugun_yechilgan + amount > self.KUNLIK_LIMIT:
            qolgan = self.KUNLIK_LIMIT - self.__bugun_yechilgan
            print(f"Kunlik limit oshdi! Bugun yana {qolgan} so'm yechish mumkin.")
            return False
        self.__balance -= amount
        self.__bugun_yechilgan += amount
        self.__tarix.append(f"-{amount} so'm chiqim | Balans: {self.__balance} so'm")
        print(f"{amount} so'm yechildi.")
        print(f"Qolgan balans: {self.__balance} so'm")
        return True

    def change_pin(self, old_pin: int, new_pin: int) -> None:
        if not self.__pin_tekshir(old_pin):
            return
        if not isinstance(new_pin, int) or not (1000 <= new_pin <= 9999):
            print("Yangi PIN 4 xonali son bo'lishi kerak!")
            return
        self.__pin = new_pin
        self.__tarix.append("PIN kod o'zgartirildi")
        print("PIN kod o'zgartirildi.")

    def transfer(self, qabul_qiluvchi: "BankAccount", amount: int, pin: int) -> None:
        if not isinstance(qabul_qiluvchi, BankAccount) or qabul_qiluvchi is self:
            print("Qabul qiluvchi hisob noto'g'ri!")
            return
        if qabul_qiluvchi.__bloklangan:
            print("Qabul qiluvchi karta bloklangan!")
            return
        if amount <= 0:
            print("O'tkazma summasi musbat bo'lishi kerak!")
            return
        if not self.__pin_tekshir(pin):
            return
        if amount > self.__balance or (self.__balance - amount) < 0:
            print("Hisobda yetarli mablag' mavjud emas!")
            return
        self.__kunlik_limitni_yangila()
        if self.__bugun_yechilgan + amount > self.KUNLIK_LIMIT:
            qolgan = self.KUNLIK_LIMIT - self.__bugun_yechilgan
            print(f"Kunlik limit oshdi! Bugun yana {qolgan} so'm o'tkazish mumkin.")
            return
        self.__balance -= amount
        self.__bugun_yechilgan += amount
        qabul_qiluvchi.__balance += amount
        self.__tarix.append(
            f"-{amount} so'm o'tkazma -> {qabul_qiluvchi.owner} | Balans: {self.__balance} so'm"
        )
        qabul_qiluvchi.__tarix.append(
            f"+{amount} so'm o'tkazma <- {self.owner} | Balans: {qabul_qiluvchi.__balance} so'm"
        )
        print(f"{self.owner} -> {qabul_qiluvchi.owner}")
        print(f"{amount} so'm o'tkazildi.\n")
        print(f"{self.owner} balansi: {self.__balance}")
        print(f"{qabul_qiluvchi.owner} balansi: {qabul_qiluvchi.__balance}")

    def show_history(self, pin: int) -> None:
        if not self.__pin_tekshir(pin):
            return
        if not self.__tarix:
            print("Tranzaksiyalar tarixi bo'sh.")
            return
        for i, yozuv in enumerate(self.__tarix, start=1):
            print(f"{i}. {yozuv}")