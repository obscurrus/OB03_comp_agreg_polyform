
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.age}"

class Bird(Animal):
    def make_sound(self):
        return "Птички поют"
class Mammal(Animal):
    def make_sound(self):
        return "Млекопитающие издают разные звуки"

class Reptile(Animal):
    def make_sound(self):
        return "Рептилии шипят"
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

    def __str__(self):
        return f"В зоопарке {len(self.animals)} животных и {len(self.employees)} сотрудников"

class Employee():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"Животное {animal.name} покормлено {self.name} {self.surname}")


class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"Животное {animal.name} вылечено {self.name} {self.surname}")

def feed_all_animals(zoo):
    for animal in zoo.animals:
        zoo.employees[0].feed_animal(animal)

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


my_zoo.employees[0].feed_animal(my_zoo.animals[0])
feed_all_animals(my_zoo)

