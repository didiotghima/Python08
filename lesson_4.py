                                #Тема
#Tuple - Кортежи.Циклы for и while
#int, str, float, bool,  tuple - неизмен
#list измен

#tuple 

# names = ('Kurmanbek', 'Beksultan',' Nurbolot')
# print(names)
# print(names[0])
# print(names[1:3])
# print(names[::2])

# names.add('askhat')
# print(names)             #tuple 


# names.pop(0)
# names.remove('nurbolot')
# names[0]= "python"


# lst = ['hello']
# print(type(lst))              #type определяет типы данных


# tup = ('hello')
# print(type(tup))


# tup = ('hello', 10,0.1, True,[1,2,3,4,5],(1,2,3,4,5))
# print(tup)
# print(tup[4][0])

# cars = ('bmw','mersedes','audi')
# print(cars)
# lst_cars = list(cars)
# print(lst_cars)
# lst_cars.append('tesla')
# cars = tuple(lst_cars)
# print(cars)

# import dis 
# lst = [1,2,3,4,5]
# tup = (1,2,3,4,5)

# dis.dis('lst')
# dis.dis('tup')

                                                       #Циклы for u while

# for num in range(1001):
#     print(num, "geeks")

# for i in range(10,51):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for n in range(1000001):
#             print(n)

# numbers = [10,11,100,333,445,34,45,67,2,101,102]
# print(numbers)
# for n in numbers:
#     if n % 2 == 0:
#         print(n,"четный")
#     else:
#         print(n,"нечетный")

# it = ["geeks","meta","google","neobis"]
# for  i in it:
#     print(i)
#     if i =="meta":
#         break  #до срочно прерывает цикл,    contunie 


# name = "Nurbolot"
# for n in name:
#     print(n)

######################################################################while

# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 +=1
#     print(num1)

# n =0
# while True:
#     n += 1
#     print("geeks",n)


# while True:
#     num1 = int(input("number1: "))
#     operator = input("+,-,*,/ :")
#     num2 = int(input("number2: "))
#     if operator == "+":
#         print("Ответ: ", num1 + num2)
#     elif operator == "-":
#         print("Ответ:",num1-num2)
#     elif operator == "*":
#         print("Ответ:",num1*num2)
#     elif operator == "/":
#         print("Ответ:",num1/num2)
#     elif num1 == 0 and num2 == 0 and operator == "0":
#         print("Stop")
#         break
#     else:
#         print("Такого оператора не существует")


# import random

# # print(random.randint(1,10))
# random_number = random.randint(1,10)
# attempt = 0
# while True:
#     input_number = int(input("введите число от 1 до 10: "))
#     if input_number >= 1 and input_number <=10:    
#         attempt += 1
#         if input_number == random_number:
#             print("Вы выиграли!Поздравляем!")
#             break
#         elif attempt == 5:
#             print("вы проиграли")
#             break
#         else:
#             print("Неправльно у вас", 5 - attempt, "Попыток")
#     else:
#         print("Введите число от 1 до 10!")