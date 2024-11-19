# 1.	Используя функцию map() переписать функцию
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

# Решение:
def square(x):
    return x ** 2
items = [1, 2, 3, 4, 5]
squared = list(map(square, items))
print(squared)

# lambda
squared = list(map(lambda x: x**2, items))
print(squared)

# 2.	Используйте функцию reduce() и перепишите код
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# Решение:
from functools import reduce
def multiply(x, y):
    return x * y
numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)
print(product)

# lambda
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# 4.	Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
# Решение:
x = [1, 2, 3]
y = [4, 5, 6]

zipped = list(zip(x, y))
print(zipped)

# 5.	Используйте функцию zip() чтобы преобразовать код:
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

for i in range(len(name_hero)):
    print(name_hero[i], '-', name_real[i])

# Решение:
for hero, real_name in zip(name_hero, name_real):
    print(hero, '-', real_name)

# 6.	С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.
# Решение:
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

def is_odd(x):
    return x % 2 != 0

odd_numbers = list(filter(is_odd, numbers))
print(odd_numbers)

# lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
