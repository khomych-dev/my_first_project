from colorama import Fore, Style, init
import json
import os

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


def load_from_file():
    file_name = 'garage.json'
    loaded_garage = []

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)

        for item in raw_data:
            loaded_garage.append(
                Car(item['brand'], item['model'], item['year']))

    return loaded_garage


def save_to_file(garage_list):
    if not garage_list:
        return

    data_to_save = []
    for car in garage_list:
        data_to_save.append(
            {'brand': car.brand, 'model': car.model, 'year': car.year})

    with open("garage.json", "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    print(Fore.BLUE + "Дані збережено у файл garage.json!" + Style.RESET_ALL)


garage = load_from_file()

print(Fore.CYAN + "=== СИСТЕМА УПРАВЛІННЯ ГАРАЖЕМ АКТИВОВАНА ===" + Style.RESET_ALL)
print("Для виходу напиши 'стоп' у назві марки.\n")

while True:
    brand = input(
        Fore.YELLOW + "Введи марку авто (або 'стоп' для звіту): " + Style.RESET_ALL)

    if brand.lower() == 'стоп':
        break

    model = input("Введи модель: ")
    year = input("Введи рік: ")

    try:
        new_car = Car(brand, model, int(year))
        garage.append(new_car)
        print(Fore.GREEN + "✓ Авто додано до черги\n" + Style.RESET_ALL)
    except ValueError:
        print(
            Fore.RED + "× Помилка: Рік має бути числом! Спробуй ще раз.\n" + Style.RESET_ALL)

print("\n" + Fore.CYAN + "="*30)
print("ПІДСУМКОВИЙ ЗВІТ ГАРАЖА:")
print("="*30 + Style.RESET_ALL)

if not garage:
    print("Гараж порожній. Роботи не було.")
else:
    for car in garage:
        print(car.get_info())

save_to_file(garage)

print(Style.RESET_ALL)
