# Задание 1
# Написать консольную программу. По номеру месяца напечатать пору года.

month = int(input("Введите номер месяца (1-12): "))

if 1 <= month <= 2 or month == 12:
    season = "Зима"
elif 3 <= month <= 5:
    season = "Весна"
elif 6 <= month <= 8:
    season = "Лето"
elif 9 <= month <= 11:
    season = "Осень"
else:
    season = "Некорректный номер месяца"

print("Пора года:", season)

# Задание 2
# Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
# Могут ли два билета подряд быть удачными?
# 609999 и 610000 - удачные.

ticket1 = int(input("Введите номер первого билета: "))
ticket2 = ticket1 + 1

#Первый билет
a1 = ticket1 // 100000
b1 = (ticket1 // 10000) % 10
c1 = (ticket1 // 1000) % 10
d1 = (ticket1 // 100) % 10
e1 = (ticket1 // 10) % 10
f1 = ticket1 % 10

sum1 = a1 + b1 + c1 + d1 + e1 + f1

# Проверка 1 билета
is_lucky1 = (sum1 % 7 == 0)

# Второй билет
a2 = ticket2 // 100000
b2 = (ticket2 // 10000) % 10
c2 = (ticket2 // 1000) % 10
d2 = (ticket2 // 100) % 10
e2 = (ticket2 // 10) % 10
f2 = ticket2 % 10

sum2 = a2 + b2 + c2 + d2 + e2 + f2

# Проверка 2 билета
is_lucky2 = (sum2 % 7 == 0)

print("Билет", ticket1, "удачный:", is_lucky1)
print("Билет", ticket2, "удачный:", is_lucky2)

# Проверка
if is_lucky1 and is_lucky2:
    print("Оба билета удачные.")
else:
    print("Оба билета не могут быть удачными одновременно.")

# Задание 3
# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры.
# Найти значение максимального элемента списка.

import random
n = int(input("Введите размер списка: "))
A = [0] * n
for i in range(n):
    A[i] = random.randint(0, 99)

print("Сгенерированный список:", A)

max_value = A[0] # Первый элемент max

for i in range(1, n):
    if A[i] > max_value:
        max_value = A[i]

print("Максимальное значение в списке:", max_value)