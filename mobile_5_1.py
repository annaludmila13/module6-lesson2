class Vehicle:
    # Атрибут класса со списком допустимых цветов
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    @property
    def model(self):
        return f"Модель: {self.__model}"

    @property
    def horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    @property
    def color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"{self.model}\n{self.horsepower}\n{self.color}\nВладелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)
# Создаем объект класса Sedan
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Исходные свойства
print("\n# Изначальные свойства:")
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
print("\n# Меняем свойства (в т.ч. вызывая методы):")
vehicle1.set_color('Pink')  # Ожидается сообщение об ошибке
vehicle1.set_color('BLACK')  # Цвет сменится на черный
vehicle1.owner = 'Vasyok'   # Владелец изменится на Vasyok

# Проверяем изменения
print("\n# Проверяем что поменялось:")
vehicle1.print_info()
