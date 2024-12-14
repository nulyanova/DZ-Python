# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем
# сторонами a и b на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

def cut_into_squares(a, b):
    squares = []

    def recurse_cut(a, b):
        if a == 0 or b == 0:
            return

        # Найти наибольший возможный квадрат на текущем этапе
        size = min(a, b)
        squares.append(size)

        if a > b:
            recurse_cut(a - size, b)
        else:
            recurse_cut(a, b - size)

    recurse_cut(a, b)
    return squares


# Пример использования
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))

squares = cut_into_squares(a, b)
print("Длины ребер полученных квадратов:", squares)
print("Количество полученных квадратов:", len(squares))