#Множечства set , frozenset
# numbers = {1,2,3,4,5}
# print(numbers)
# print(numbers[0])    #нету индекса и срезов в set:кроме цифры все меняется по местами и это нормально

# company  = {"Google","Meta","Space X"}
# print(company)         
# company.add("Tesla")    #set изменяемая типа данных
# print(company)
# company.remove("Google")
# print(company)
# company.pop()
# print(company)

# st = {1,0.1,"hello",False,(1,2,3,4)}      #set, list нельзя хронить
# print(st)

# num1 = [1,2,3,4,5]
# num2 = [3,4,5,6,7]
# num3 = num1 + num2
# print(list(set(num3)))

# cars = {"bmw","dodge","tesla","honda"}
# for car in cars:
#     print(car)                               # цикл for можно добавлять

# numbers = {1,0.1,100,4,99,1111,9,8,34}
# print(sorted(numbers))

# st = {1,1.0,True,"1"}
# print(st)
# print(True + 1)

# Frozenset ни как нельзя добавить или же удалить,можно писать на любые скобки
# frozen_set = frozenset({1,2,3,4,5,5,5,5})               #удаляеть все похожие цифры
# print(frozen_set)
# frozen_set.add("tesla")

#Dict 9 типы данных        #Dict-отличие от set это двое точее в скобках
# student = {'name': 'askhat','age':18}
#            #ключ     от них  #ключ
# print(len(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('language','python')
# print(student)                                #setdefault добавление
# student.pop('age')                            #pop удаляет
# print(student)
# student['language'] = 'Java'
# print(student)                                #можно обновлять

# tesla = {
#     'brand' : 'tesla',
#     'model' : 'model x',
#     'year'  : 2022,
#     'price' : '46000$',
#     'color' : 'white'
#     }
# print(tesla['model'])
# print(tesla.keys())                    #ключ 
# print(tesla.values())                  #значение
# print(tesla.items())                   #одновременна ключ и  значение


# tesla = {
#     'brand' : 'tesla',
#     'model' : 'model x',
#     'year'  : 2022,
#     'price' : '46000$',
#     'color' : 'white'
    # }

# for key, value in tesla.items():
#     print(key, value)



# todo_list = {
#     '03:00' : 'Проснуться'
# }
# while True:
#     command = int(input("Введите команду, 1 - посмотреоть список дел, 2 - добавить, 3 - удалить:"))
#     if command == 1: 
#         print("Список дел:")
#         for time , task in todo_list.items():
#             print(time, task) 
#         print("----------------------------------------")
#     elif command == 2:
#         add_time = input("Время:")
#         add_task = input("Задание:")
#         todo_list.setdefault(add_time, add_task)
#         print("Задание", add_task,"успешно добавлена на ",add_time)
#         print("----------------------------------------")
#     elif command == 3:
#         delete_time = input("Введите время для удаление: ")
#         todo_list.pop(delete_time)
#         print("Задание удаленно")
#         print("----------------------------------------")
#     elif command ==0:
#         print("EXIT TODO")
#         break 
#     else:
#         print("Такой команды не существует")





