'''Композиция'''


# Композиция - когда объект создается внутри класса.


class Engine:

    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine stopped')


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()


my_car = Car()
my_car.start()
my_car.stop()

'''Агрегация'''


# Агрегация - когда объект создается независимо, внутри класса используются методы другого класса.

class Teacher:

    def teach(self):
        print('Teacher teaching')


class School:
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()


my_teacher = Teacher()
my_school = School(my_teacher)

my_school.start_lesson()

'''Полиморфизм'''


# когда один и тот же метод используется в разных реализациях разных объектов.

class Dog:

    def say(self):
        return "Gav gav"


class Cat:

    def say(self):
        return "Meow meow"


def animal_say(animal):
    print(animal.say())


my_dog = Dog()
my_cat = Cat()

animal_say(my_dog)
animal_say(my_cat)
