from colorama import Fore, Style, init

init()


# models.py
class Car:
    def __init__(self, brand, model, year, car_number, repair_cost=0, status="repair"):
        self.brand = brand
        self.model = model
        self.year = year
        self.car_number = car_number
        self.repair_cost = repair_cost
        self.status = status

    def get_info(self):
        color = Fore.GREEN if self.status == "ready" else Fore.RED
        label = "Готова" if self.status == "ready" else "В ремонті"
        # Додаємо ціну до рядка виводу
        return f"{color}{self.brand} {self.model} [{self.car_number}] ({self.year}) - {self.repair_cost} грн -> {label}{Style.RESET_ALL}"
