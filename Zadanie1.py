#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.

if __name__ == '__main__':
    school = {'1а': 26, '1б': 23, '1в': 24, '2а': 20, '2б': 24, '3а': 19, '3б': 16, '3в': 18, '4а': 23, '4б': 20, '5а': 22, '5б': 21, '5в': 24, '6а': 19, '6б': 17, '7а': 21, '7б': 17, '8а': 20, '8б': 22, '9а': 19, '9б': 20,  '10а': 16, '10б': 19, '11а': 20, '11б': 17}

    school['3а'] = 21
    school['6в'] = 15
    del school['5в']

    students = 0
    for i, k in enumerate(school):
        students += school[k]
    print("Общее число учащихся в школе: ", students)
