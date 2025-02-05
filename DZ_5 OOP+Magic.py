#Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей. ДОБАВИТЬ МЕТОДЫ КЛАССА И СТАТИЧЕСКИЕ МЕТОДЫ.
# Вар.1 Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности). Создать список объектов.
# Вывести: a) список книг заданного автора; б) список книг, выпущенных после заданного года.
#Добавить: магические методы __setattr__, __str__, арифметические методы __add__ и __sub__,
# операторы сравнения __eq__ и __lt__, а также методы __new__ и __del__.

class Book:
    # Статическое поле
    book_count = 0

    def __new__(cls, *args, **kwargs):
        # Создание нового экземпляра
        instance = super(Book, cls).__new__(cls)
        return instance

    def __init__(self, book_id, title, authors, publisher, year, pages, price, binding_type):
        # Динамические поля
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.price = price
        self.binding_type = binding_type
        Book.book_count += 1

    def __setattr__(self, key, value):
        # Проверка корректности при установке атрибутов
        if key == "price" and value <= 0:
            raise ValueError("Price must be a positive number")
        super().__setattr__(key, value)

    def __str__(self):
        # Строковое представление объекта
        return f"Book({self.book_id}, {self.title}, {self.authors}, {self.publisher}, {self.year}, {self.pages}, {self.price}, {self.binding_type})"

    def __add__(self, other):
        # Сложение цен двух книг
        if isinstance(other, Book):
            return self.price + other.price
        return NotImplemented

    def __sub__(self, other):
        # Вычитание цен двух книг
        if isinstance(other, Book):
            return self.price - other.price
        return NotImplemented

    def __eq__(self, other):
        # Сравнение книг по идентификатору
        if isinstance(other, Book):
            return self.book_id == other.book_id
        return NotImplemented

    def __lt__(self, other):
        # Сравнение книг по году издания
        if isinstance(other, Book):
            return self.year < other.year
        return NotImplemented

    def __del__(self):
        # Уменьшение счетчика книг при удалении объекта
        Book.book_count -= 1

    # Метод объекта
    def display_info(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Authors: {self.authors}, Publisher: {self.publisher}, Year: {self.year}, Pages: {self.pages}, Price: {self.price}, Binding: {self.binding_type}"

    # Статический метод
    @staticmethod
    def get_book_count():
        return f"Total number of books: {Book.book_count}"

    # Метод класса
    @classmethod
    def create_book(cls, book_id, title, authors, publisher, year, pages, price, binding_type):
        return cls(book_id, title, authors, publisher, year, pages, price, binding_type)

    # Инкапсулированное поле (сеттер и геттер)
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be a positive number")

    def get_price(self):
        return self.__price


# Создание списка объектов
books = [
    Book(1, "Book One", "Author A", "Publisher X", 2021, 300, 25.99, "Hardcover"),
    Book(2, "Book Two", "Author B", "Publisher Y", 2020, 150, 15.50, "Paperback"),
    Book(3, "Book Three", "Author A", "Publisher Z", 2022, 200, 20.00, "Hardcover")
]

# Вывод списка книг заданного автора
author_books = [book.display_info() for book in books if book.authors == "Author A"]
print("Books by Author A:")
for info in author_books:
    print(info)

# Вывод списка книг, выпущенных после заданного года
year_books = [book.display_info() for book in books if book.year > 2020]
print("\nBooks published after 2020:")
for info in year_books:
    print(info)