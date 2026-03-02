from colorama import Fore, Style, init

init()


class Car:
    def __init__(self, brand, model, year, car_number, status="repair"):
        self.brand = brand
        self.model = model
        self.year = year
        self.car_number = car_number
        self.status = status

    def get_info(self):
        if self.status == "ready":
            color = Fore.GREEN
            label = "Готова до виїзду"
        else:
            color = Fore.RED
            label = "На підйомнику"

        return f"{color}{self.brand} {self.model} ({self.car_number}) ({self.year}) -> {label}{Style.RESET_ALL}"
