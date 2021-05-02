# Уточнение корней уравнения методом касательных
'''
Для выбора крайней точки диапазона от которой будем строить касательные,
найдем вторую производную функции т.к. для определения этой точки должны
соблюдаться условия f(x)*f"(x) > 0
Производная исходной функции: 387*sin(387*x/1000)/1000 + 1/(2*sqrt(x))
'''
from math import sqrt, cos, sin

def Uravnenie(x, accuracy):
    global count

    pribl = (sqrt(x) - cos(0.387 * x))/(387*sin(387*x/1000)/1000 + 1/(2*sqrt(x)))  # вычисляем значение отношения функции к ее производной
    if abs(pribl) > accuracy:
        x1 = x - pribl
        count += 1
        print('Строим очередную касательную в точке', x1)
        Uravnenie(x1, accuracy)
    elif abs(pribl) < accuracy:
        print('Приближение:', pribl)
        print('Корень уравнения:', x)
        print('Количество итераций:', count)

accur = 0.001       # точность
count = 0
Uravnenie(1, accur)

accur = 0.000001      # точность
count = 0
Uravnenie(1, accur)

accur = 0.000000001      # точность
count = 0
Uravnenie(1, accur)
