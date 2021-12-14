def zapolnenie():
    global arr
    arr = []
    for i in range(50000):
        a = input()
        if a != '':
            arr.append(a)
        else:
            break



index = []
print('Олимпиада по МАТЕМАТИКЕ\n')
print('Введите участников и баллы: ')
#заполняет список и убирает повторы
zapolnenie()
arr_math = set(arr)
arr_math = list(arr_math)

#разбивает внутри списка имена, фамилии и баллы через пробелы
arr_math1 = []
for i in range(0, len(arr_math)):
    arr_math1.append(arr_math[i].split())

#делает копию списка без баллов
arr_all_copy = []
for i in range(len(arr_math1)):
    arr_all_copy.append((arr_math1[i][0], arr_math1[i][1]))

#закидывает баллы в отдельный список
arr_math_bal = []
for i in range(0, len(arr_math1)):
    arr_math_bal.append(arr_math1[i][2].split())

# перевод в баллы
arr_math_bal = [[int(x[0])] for x in arr_math_bal]

#print(arr_math_bal)


#создает словарь
arr_math_bal = [j for i in arr_math_bal for j in i]
arr_math_dict = dict(zip(arr_all_copy, arr_math_bal))

#print(arr_math_dict)

#Создает индексы
for i in range(len(arr_all_copy)):
    index_arr_all_copy = (f'{i+1}_{arr_all_copy[i][0][0]}_{len(arr_all_copy[i][1])},')
    index.append(index_arr_all_copy)

#создает словарь с именами и индексами
index_dict = dict(zip(arr_all_copy, index))

#вывод данных
print("\nВсего участников:", len(arr_math_dict))
print("\nНаибольшее число баллов набрал(а) -", *max(arr_math_dict, key=arr_math_dict.get), '(', arr_math_dict[max(arr_math_dict, key=arr_math_dict.get)], ')')
print('\nИндексы:')
for i in arr_all_copy:
    print(index_dict[i], "\n")


'''
степухина катя 2
петрова анастасия 73
смирнов даниил 80
кадетов кирилл 100
морозов олег 40
подушко даниил 70
никалаев максим 60
'''
