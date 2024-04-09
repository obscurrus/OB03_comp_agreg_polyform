"""Время выполнить задание

1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
и методы (`make_sound()`, `eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
если требуется (например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут
иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для
`Veterinarian`).


Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации
о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
между запусками программы."""

import json


class Animal:
    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type

    def make_sound(self):
        pass

    def eat(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.age}"


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Птица")

    def make_sound(self):
        return "Птички поют"

    def eat(self):
        return "Птицы едят ягоды"


class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Млекопитающее")

    def make_sound(self):
        return "Млекопитающие издают разные звуки"

    def eat(self):
        return "Млекопитающие едят растения и других животных"


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Рептилия")

    def make_sound(self):
        return "Рептилии шипят"

    def eat(self):
        return "Рептилии едят растения и других животных"


#animals = [Bird("Соловей", 1), Mammal("Медведь", 5), Reptile("Змеюка", 6)]

def animal_sound(animals):
    sounds = []
    for animal in animals:
        sounds.append(f'{animal.name} - {animal.make_sound()}')
    return sounds


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_animals(self):
        return self.animals

    def get_employees(self):
        return self.employees

    def feed_all_animals(self):
        for animal in self.animals:
            self.employees[0].feed_animal(animal)

    def __str__(self):
        return f"В зоопарке {len(self.animals)} животных и {len(self.employees)} сотрудников"


class Employee:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def __str__(self):
        return f"{self.name} {self.surname} - {self.position}"


class ZooKeeper(Employee):
    def __init__(self, name, surname):
        super().__init__(name, surname, "Зоотехник")

    def feed_animal(self, animal):
        print(f"Животное {animal.name} покормлено {self.name} {self.surname}")


class Veterinarian(Employee):
    def __init__(self, name, surname):
        super().__init__(name, surname, "Ветеринар")

    def heal_animal(self, animal):
        print(f"Животное {animal.name} вылечено {self.name} {self.surname}")



'''testing zone'''

my_zoo = Zoo()
my_zoo.add_animal(Bird("Соловей", 1))
my_zoo.add_animal(Bird("Кукушка", 2))
my_zoo.add_animal(Mammal("Медведь", 5))
my_zoo.add_animal(Reptile("Змеюка", 6))
my_zoo.add_employee(ZooKeeper("Вася", "Пупкин"))
my_zoo.add_employee(Veterinarian("Петя", "Иванов"))

#print(f'Животное {my_zoo.animals[0].name} покормлено {my_zoo.employees[0].name} {my_zoo.employees[0].surname}')
print(my_zoo.__str__())

#my_zoo.employees[0].feed_animal(my_zoo.animals[0])
#feed_all_animals(my_zoo)

# в первой версии вынимал тип класса функцией isinstance()
# for animal in my_zoo.animals:
#     if isinstance(animal, Bird):
#         print(f"Птица. {animal.name}. Возраст {animal.age}")
#     elif isinstance(animal, Mammal):
#         print(f"Млекопитающее. {animal.name}. Возраст {animal.age}")
#     elif isinstance(animal, Reptile):
#         print(f"Рептилия. {animal.name}. Возраст {animal.age}")
#
# for i, employee in enumerate(my_zoo.employees, start=1):
#     if isinstance(employee, ZooKeeper):
#         print(f"Сотрудник {i}: Зоотехник - {employee.name} {employee.surname}")
#     elif isinstance(employee, Veterinarian):
#         print(f"Сотрудник {i}: Ветеринар - {employee.name} {employee.surname}")


for animal in my_zoo.get_animals():
    print(f"{animal.animal_type}. {animal.name}. Возраст {animal.age}")

for i, employee in enumerate(my_zoo.get_employees(), start=1):
    print(f"Сотрудник {i}: {employee}")

animals = my_zoo.get_animals()
print(f'Самое молодое животное: {min(animals, key=lambda animal: animal.age)}')
