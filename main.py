#10.	Написать функцию, которая принимает переменную char, если она оказывается цифрой, то возвращает ее значение типа integer.
#19.	Вывести ФИО, предметы и оценки студента с самой худшей успеваемостью
import pandas as pd
import ast

func_num = input('Выберете номер функции (1, 2): ')

if func_num == '1':
    def func(symb):
        if symb in '1234567890':
            return ord(symb)
        else:
            return symb

    input = str(input('Введите char: '))
    if len(input) == 1:
        print(func(input))
    else:
        print("Ошибка в вводе")

elif func_num == '2':
    student_ind = -1
    min_score = 5
    data = pd.read_csv('file.csv', sep=";")
    for i, student in enumerate(data.values):
        score = list()
        for predmet in ast.literal_eval(student[3]):
            score.append(predmet[2])
        score = sum(score)/len(score)
        if score < min_score:
            student_ind = i
            min_score = score

    if student_ind >= 0:
        print(data.loc[[student_ind]])

else:
    print('Ошибка при выборе функции')




