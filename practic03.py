# Задача №3.
#
# Создайте класс Author и класс Book. Класс Book должен использовать композицию
# для включения автора в качестве объекта.

class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book_info(self):
        print(f"{self.title} by {self.author.name} {self.author.surname}")


author = Author("Leo", "Tolstoy")
book = Book("War and Peace", author)

print(author.name, author.surname)
book.get_book_info()
