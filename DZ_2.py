# Задание 1. Задачи на одномерные списки
# Вариант 2. Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.
# Вариант 5. Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

A = list(map(int, input("Введите элементы списка через пробел: ").split()))

max_odd = None
min_abs = A[0]
min_even = None

for i in range(len(A)):
    # Наибольший нечетный элемент
    if A[i] % 2 != 0:
        if max_odd is None or A[i] > max_odd:
            max_odd = A[i]

    # Минимальный по модулю элемент
    if abs(A[i]) < abs(min_abs):
        min_abs = A[i]

    # Наименьший четный элемент
    if A[i] % 2 == 0:
        if min_even is None or A[i] < min_even:
            min_even = A[i]

# Если четного элемента нет, берем первый элемент
if min_even is None:
    min_even = A[0]

# Преобразование списка: сначала нулевые элементы
zero_count = 0
for i in range(len(A)):
    if A[i] == 0:
        zero_count += 1

# Создаем новый список с нулями впереди
B = [0] * zero_count + [x for x in A if x != 0]

print("Наибольший нечетный элемент:", max_odd)
print("Минимальный по модулю элемент:", min_abs)
print("Наименьший четный элемент:", min_even)
print("Преобразованный список, сначала нулевые:", B)

# Задание 2. Задачи на многомерные списки
# 1. В матрице найти номер строки, сумма чисел в которой максимальна.
def main():
    print("Введите матрицу построчно, разделяя элементы пробелами. Для завершения ввода введите пустую строку.")
    matrix = []
    while True:
        line = input()
        if not line:
            break
        row = list(map(int, line.split()))
        matrix.append(row)

    # Проверка, что матрица не пустая
    if not matrix:
        print("Матрица пуста.")
        return

    # Поиск номера строки с максимальной суммой
    max_sum = float('-inf')
    max_row_index = -1

    for i, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
            max_row_index = i
    print(f"Номер строки с максимальной суммой элементов: {max_row_index + 1} (сумма = {max_sum})")
if __name__ == "__main__":
    main()