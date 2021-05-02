# Уточнение корней уравнения методом хорд

from math import sqrt, cos, sin

def Uravnenie(x1, x2, accuracy):
    global count
    y1 = sqrt(x1) - cos(0.387 * x1)  # вычисляем значение функции для левой границы
    print('y1:', y1)
    y2 = sqrt(x2) - cos(0.387 * x2)  # вычисляем значение функции для правой границы
    print('y2', y2)
    # new_x = x - ((b - x)*y)/(f(b) - y)

    if y1 * y2 < 0 and abs(y2) > accuracy:
        count += 1
        new_x = x1 - ((x2 - x1)*y1)/(y2 - y1)
        print('Новый диапазон:', new_x, x2)
        print('Итерация:', count)
        Uravnenie(x1, new_x, accuracy)
        Uravnenie(new_x, x2, accuracy)
    elif y1 * y2 < 0 and (abs(y1) < accuracy or abs(y2) < accuracy):
        print('Найден корень:', x2)
        print('Точность:', accuracy)
        print('Значения у1 и у2:', y1, y2)
        print('Количество итераций:', count)
        print('*' * 30)
    else:
        print('В данном диапазоне не может быть корней.')


left_border = 0.75  # левая граница интервала
right_border = 1  # правая граница интервала
count = 0
accur = 0.001  # точность

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