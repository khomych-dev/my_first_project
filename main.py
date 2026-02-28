from colorama import Fore, Style, init

init()


class Car:
    def __init__(self, brand, model, year, status="repair"):
        self.brand = brand
        self.model = model
        self.year = year
        self.status = status

    def get_info(self):
        if self.status == "ready":
            color = Fore.GREEN
            label = "Готова до виїзду"
        else:
            color = Fore.RED
            label = "На підйомнику"

        return f"{color}{self.brand} {self.model} ({self.year}) -> {label}{Style.RESET_ALL}"


init()

# Наш порожній список (база даних у пам'яті)
garage = []

print(Fore.CYAN + "=== СИСТЕМА УПРАВЛІННЯ ГАРАЖЕМ АКТИВОВАНА ===" + Style.RESET_ALL)
print("Для виходу напиши 'стоп' у назві марки.\n")

while True:
    # 1. Запитуємо назву марки
    brand = input(
        Fore.YELLOW + "Введи марку авто (або 'стоп' для звіту): " + Style.RESET_ALL)

    # 2. Умова виходу (наш "стоп-кран")
    if brand.lower() == 'стоп':
        break

    # 3. Запитуємо інші дані
    model = input("Введи модель: ")
    year = input("Введи рік: ")

    # Створюємо об'єкт і додаємо в список
    try:
        new_car = Car(brand, model, int(year))
        garage.append(new_car)
        print(Fore.GREEN + "✓ Авто додано до черги\n" + Style.RESET_ALL)
    except ValueError:
        print(
            Fore.RED + "× Помилка: Рік має бути числом! Спробуй ще раз.\n" + Style.RESET_ALL)

# 4. Фінальний звіт після виходу з циклу
print("\n" + Fore.CYAN + "="*30)
print("ПІДСУМКОВИЙ ЗВІТ ГАРАЖА:")
print("="*30 + Style.RESET_ALL)

if not garage:
    print("Гараж порожній. Роботи не було.")
else:
    for car in garage:
        print(car.get_info())

print(Style.RESET_ALL)
