# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""

try:
    weight = input()
    height = input()


    #Ваш код
    height = float(height) / 100
    weight = float(weight)

    BMI = weight/(height**2)

    print("Индекс массы тела при весе в {0} кг и росте в {1} см равен {2:.2f}".format(weight,height,BMI))
except:
    print("Необходимо вводить числа")