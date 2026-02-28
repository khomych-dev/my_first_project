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


# 2. Використовуємо креслення для створення реальних об'єктів (Екземплярів)
car1 = Car("BMW", "M5", 2020, "ready")
car2 = Car("Audi", "RS6", 2022)  # статус буде "repair" за замовчуванням
car3 = Car("Toyota", "Supra", 1998, "ready")

# 3. Наш склад (тепер тут не просто тексти, а об'єкти)
garage = [car1, car2, car3]

print(Fore.CYAN + "--- Звіт інженерного відділу ---" + Style.RESET_ALL)

for car in garage:
    print(car.get_info())

car3.start_engine()

print(Style.RESET_ALL)
