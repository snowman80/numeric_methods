# Уточнение корней уравнения методом половинного деления
from math import sqrt, cos

def Uravnenie(x1, x2, accuracy):
    global count
    y1 = sqrt(x1) - cos(0.387 * x1)  # вычисляем значение функции для левой границы
    y2 = sqrt(x2) - cos(0.387 * x2)  # вычисляем значение функции для правой границы
    if y1 * y2 < 0 and abs(y1) > accuracy:
        count += 1
        new_x = (x1 + x2)/2  # находим середину диапазона
        print('Новый диапазон:', x1, new_x)
        Uravnenie(x1, new_x, accuracy)
        Uravnenie(new_x, x2, accuracy)
    elif y1 * y2 < 0 and (abs(y1) < accuracy or abs(y2) < accuracy):
        print('Найден корень в диапазоне:', x1, x2)
        print('Точность:', accuracy)
        print('Значения у1 и у2:', y1, y2)
        print('Количество итераций:', count)
        print('*' * 30)

def Uravnenie2(x1, x2, accuracy):
    global count
    y1 = x1 ** 3 - 3 * x1 ** 2 + 6 * x1 + 3 # вычисляем значение функции для левой границы
    y2 = x2 ** 3 - 3 * x2 ** 2 + 6 * x2 + 3  # вычисляем значение функции для правой границы
    if y1 * y2 < 0 and abs(y1) > accuracy:
        count += 1
        new_x = (x1 + x2) / 2  # находим середину диапазона
        print('Новый диапазон:', x1, new_x)
        Uravnenie2(x1, new_x, accuracy)
        Uravnenie2(new_x, x2, accuracy)
    elif y1 * y2 < 0 and (abs(y1) < accuracy or abs(y2) < accuracy):
        print('Найден корень в диапазоне:', x1, x2)
        print('Точность:', accuracy)
        print('Значения у1 и у2:', y1, y2)
        print('Количество итераций:', count)
        print('*' * 30)


left_border = 0.75  # левая граница интервала
right_border = 1    # правая граница интервала
count = 0
accur = 0.001       # точность

Uravnenie(left_border, right_border, accur)

left_border = 0.75
right_border = 1
count = 0
accur = 0.000001

Uravnenie(left_border, right_border, accur)

left_border = 0.75
right_border = 1
count = 0
accur = 0.000000001

Uravnenie(left_border, right_border, accur)

left_border = -0.5
right_border = 0
count = 0
accur = 0.001

Uravnenie2(left_border, right_border, accur)

left_border = -0.5
right_border = 0
count = 0
accur = 0.000001

Uravnenie2(left_border, right_border, accur)
left_border = -0.5
right_border = 0
count = 0
accur = 0.000000001

Uravnenie2(left_border, right_border, accur)

input('Press any key ...')