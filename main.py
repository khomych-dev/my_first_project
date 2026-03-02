from models import Car
from colorama import Fore, Style, init
import os
import json

init()


def load_from_file():
    file_name = 'garage.json'
    loaded_garage = []

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)

        for item in raw_data:
            new_car = Car(
                item['brand'],
                item['model'],
                item['year'],
                item['car_number'],
                item['status']
            )
            loaded_garage.append(new_car)

    return loaded_garage


def save_to_file(garage_list):
    if not garage_list:
        return

    data_to_save = []
    for car in garage_list:
        data_to_save.append(
            {
                'brand': car.brand,
                'model': car.model,
                'year': car.year,
                'car_number': car.car_number,
                'status': car.status
            }
        )

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

    if brand.lower() == 'список':
        for i, car in enumerate(garage, start=1):
            print(f"{i}. {car.get_info()}")

    if brand.lower() == 'ready':
        search_number = input("Введи д.н.з. авто для видачі: ")
        found = False

        for car in garage:
            if car.car_number == search_number:
                if car.status == 'ready':
                    print(Fore.YELLOW + "Це авто вже готове!" + Style.RESET_ALL)
                else:
                    car.status = 'ready'
                    print(
                        Fore.GREEN + f"🔧 Статус авто {search_number} змінено на READY!" + Style.RESET_ALL)
                found = True
                break

        if not found:
            print(
                Fore.RED + f"Авто з номером {search_number} не знайдено в базі." + Style.RESET_ALL)

        continue

    model = input("Введи модель: ")
    year = input("Введи рік: ")
    car_number = input("Введи д.н.з. автомобіля: ")

    try:
        new_car = Car(brand, model, int(year), car_number)
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
