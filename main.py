from colorama import Fore, Style, init

init()

# 1. Створюємо Креслення (Клас)


class Car:
    def __init__(self, brand, model, year, status="repair"):
        # Це "конструктор" - він визначає, які деталі МАЮТЬ бути у машини
        self.brand = brand
        self.model = model
        self.year = year
        self.status = status

    def get_info(self):
        # Метод - це те, що машина "вміє" робити (наприклад, звітувати про себе)
        if self.status == "ready":
            color = Fore.GREEN
            label = "Готова до виїзду"
        else:
            color = Fore.RED
            label = "На підйомнику"

        return f"{color}{self.brand} {self.model} ({self.year}) -> {label}{Style.RESET_ALL}"

    def start_engine(self):
        print(f"Врум-врум! {self.brand} заведена!")


print(Fore.CYAN + "--- Вхід у систему гаража ---" + Style.RESET_ALL)

# Створюємо порожній список для нових авто
my_new_garage = []

# Просимо користувача ввести дані
new_brand = input("Введи марку машини: ")
new_model = input("Введи модель: ")
new_year = input("Введи рік випуску: ")

# Створюємо об'єкт на основі введених даних
# перетворюємо рік на число (int)
user_car = Car(new_brand, new_model, int(new_year))

print("\n" + Fore.YELLOW + "Система обробила дані:" + Style.RESET_ALL)
print(user_car.get_info())
user_car.start_engine()
