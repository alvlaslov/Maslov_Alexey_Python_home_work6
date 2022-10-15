# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.

from random import choice

def sum(first: str, second: str):
    with open(first, 'r', encoding='utf8') as data1, \
            open(second, 'r', encoding='utf8') as data2:
        string1 = data1.readlines()
        string2 = data2.readlines()

        if len(string1) == len(string2):
            with open('sum.txt', 'a', encoding='utf-8') as data3:
                for i, k in enumerate(string1):
                    data3.write(f'{k[:-5]} + {string2[i]}')   # -5 - without 5 last symbols includes '\n'
        else:
            print('Error. The files do not match')

sum('1.txt', '2.txt') # 

