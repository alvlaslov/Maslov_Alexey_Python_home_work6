# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import choice

def polynomials(k: int):
    if k < 1:
        return 0

    result = ''
    numbers = range(0, 101)

    with open('polynomials.txt', 'a', encoding='utf-8') as data:
        for i in range(k, 0, -1):
            num = choice(numbers)
            if num:
                result += f"{num}*x^{i} {choice('+-')}"
        data.write(f"{result}{choice(numbers)} = 0\n")

for i in range (2):
    polynomials(int(input('Input a natural degree k: ')))