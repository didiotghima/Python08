#Условия if,elif,else.List - Списки
# number = int(input("введите число:"))
# if number % 2 == 0:
#     print(number, "четный")
# else:
#     print(number,"нечетный")

# age = int(input("введите свой возраст: "))
# if age < 13:
#     print("Вы не можете пользоваться нашей программой")
# elif age >=13 and age <=40:
#     print("Добро пожаловать")
# else:
#     print("Error")

#Логические операторы or, and, in, not in
# login = input("Login: ")
# password = input("Password: ")
# if login == 'geeks' and password == 'geeks2023':       #строго нужно писать правильно   :and 
#     print("Welcome")
# else:
#     print("incorrect login in password")

# login = input("Login: ")
# password = input("Password: ")
# if login == 'geeks' or password == 'geeks2023':          #совпадает один тогда все выходит     :or
#     print("Welcome")
# else:
#     print("incorrect login in password")


# word = 'geeks'
# letter = 'a'
# if letter in word:                                          #:in точно должно совпадать
#     print(letter, "есть в слове" ,word)
# else:
#     print(letter, "нету в слове",word)

# names = 'Nurbolot Adilet Nursultan Beka'
# find_name = input("Find: ")
# if find_name not in names:                                    #:not in точное имя 
#     print(find_name, 'не найден')
# else:
#     print(find_name,"найден")

#List-списки
#int,srt,float,bool,list.

# name1 = 'Nurbolot'
# name2 = 'Beksultan'
# name3 = 'Askhat'
# name4 = 'kurmanbek'

# names = ['nurbolot','kurmanbek','askhat','beka']
#             #0          #1        #2       #3              #индексы
# print(names)
# print(names[2][0])
# print(names[1])
# print(names[1:3])
# print(names[::2])                #шаги

# numbers = [1,2,3,4,5,6,7]
# print(numbers)
# numbers.append(8)
# print(numbers)                                 #В конец можно добавлять все типы данных
# numbers.append(9)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# numbers[0] = 'one'      # переименовать
# print(numbers)

# it_company = ['google', 'meta','microsoft']
# it_company.append('tesla')
# print(it_company)
# it_company.insert(0,'geeks')
# print(it_company)
# it_company.pop(2)       # удаляет только по одному
# print(it_company)
# print(it_company.index('tesla'))

# nums = [10,1,2,222,3,4,5,11]
# nums.sort()
# print(nums)

# cars = ['bmw','mersedes','tesla','honda','toyota','acura']
# cars.sort()
# cars.sort(reverse=True)
# # print(cars[::-1])
# del cars [1:4]               #удаляет по индексам
# print(cars)

# numbers = [10,100,1000,1,2,3,4,5,50,60,70,80,90]
# print(max(numbers))      #максимальная значение
# print(min(numbers))      #минимальная значение
# print(sum(numbers))      #Общая сумма
# print(sum(numbers) / len(numbers))    #Среднее арифмитическое значение


