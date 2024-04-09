# Задача №2 с использованием полиморфизма.
#
# Продемонстрировать принцип полиморфизма через реализацию разных классов,
# представляющих геометрические формы, и метод для расчёта площади каждой формы.
#
#     Создать базовый класс Shape с методом area(), который просто возвращает 0.
#
#     Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square),
#     каждый из которых переопределяет метод area().
#
#     В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
#
#     Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def calculate_area(shape):
    print(f'Площадь {type(shape).__name__}: {shape.area()}')  #В этом коде функция type(shape) возвращает тип объекта shape, а метод __name__ возвращает имя класса. Таким образом, строка type(shape).__name__ будет возвращать название класса объекта, например, Circle, Rectangle или Square.


figures = [Circle(5),Rectangle(10, 5),Square(5)]

for figure in figures:
    calculate_area(figure)



