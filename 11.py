class BankAccount:
    def __init__(self, owner, card_number, pin, balance=0):
        self.owner = owner
        self.card_number = card_number
        self.__pin = pin
        self.__balance = max(0, balance)
        self.__history = []
        self.__attempts = 0
        self.__blocked = False
        self.__daily_withdrawn = 0

    def __verify(self, pin):
        if self.__blocked:
            print("Karta bloklangan!")
            return False
        if pin != self.__pin:
            self.__attempts += 1
            print("PIN kod noto'g'ri!" if self.__attempts < 3 else "3 marta xato PIN! Karta bloklandi.")
            if self.__attempts >= 3:
                self.__blocked = True
            return False
        self.__attempts = 0
        return True

    def show_info(self):
        print(f"Mijoz: {self.owner}\nKarta: {self.card_number}")

    def check_balance(self, pin):
        if self.__verify(pin):
            print(f"Balans: {self.__balance} so'm")

    def deposit(self, amount):
        if amount <= 0:
            return print("Miqdor musbat bo'lishi kerak!")
        self.__balance += amount
        self.__history.append(f"+{amount} so'm (Kirim)")
        print(f"{amount} so'm hisobga qo'shildi.\nYangi balans: {self.__balance} so'm")

    def withdraw(self, amount, pin):
        if not self.__verify(pin): return
        if amount <= 0:
            return print("Miqdor musbat bo'lishi kerak!")
        if self.__daily_withdrawn + amount > 5_000_000:
            return print("Kunlik limit (5 000 000 so'm) oshib ketdi!")
        if amount > self.__balance:
            return print("Hisobda yetarli mablag' mavjud emas!")

        self.__balance -= amount
        self.__daily_withdrawn += amount
        self.__history.append(f"-{amount} so'm (Chiqim)")
        print(f"{amount} so'm yechildi.\nQolgan balans: {self.__balance} so'm")

    def change_pin(self, old_pin, new_pin):
        if self.__verify(old_pin):
            self.__pin = new_pin
            print("PIN kod muvaffaqiyatli o'zgartirildi!")

    def transfer(self, target, amount, pin):
        if not self.__verify(pin): return
        if amount <= 0 or amount > self.__balance:
            return print("O'tkazma uchun mablag' yetarli emas yoki summa noto'g'ri!")

        self.__balance -= amount
        target.__balance += amount
        self.__history.append(f"-{amount} so'm -> {target.owner}")
        target.__history.append(f"+{amount} so'm <- {self.owner}")
        print(f"{self.owner} -> {target.owner}\n{amount} so'm o'tkazildi.\n")
        print(f"{self.owner} balansi: {self.__balance}\n{target.owner} balansi: {target.__balance}")

    def show_history(self, pin):
        if self.__verify(pin):
            print(f"--- {self.owner} operatsiyalar tarixi ---")
            print("\n".join(self.__history) if self.__history else "Tarix bo'sh.")