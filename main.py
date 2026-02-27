from colorama import Fore, Style, init

init()

# 1. Словник (Dictionary) - це як картка запчастини: Ключ: Значення
car = {
    "brand": "BMW",
    "model": "M5",
    "year": 2020,
    "status": "ready"  # в роботі чи готова
}

# 2. Список (List) - це наш склад або черга на ремонт
garage = [
    {"brand": "Audi", "model": "RS6", "year": 2022, "status": "repair"},
    {"brand": "Toyota", "model": "Supra", "year": 1998, "status": "ready"}
]

# Додаємо нашу нову машину в гараж
garage.append(car)

print(Fore.CYAN + "Список авто в гаражі:" + Style.RESET_ALL)

# 3. Цикл (Loop) - перебираємо всі машини, як майстер робить обхід
for item in garage:
    if item["status"] == "ready":
        color = Fore.GREEN
        msg = "Можна забирати"
    else:
        color = Fore.RED
        msg = "В ремонті"

    print(
        f"{color}Авто: {item['brand']} {item['model']} ({item['year']}) -> {msg}")

print(Style.RESET_ALL)
