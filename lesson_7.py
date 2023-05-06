#повторение
# def hello_world(name:str):
#     print("Hello wworld and hello",name)
# hello_world("Nurbolot")

# def div(num1:int = 1,num2:int=1) ->float:
#     return num1/num2                                     #нужно обязательно писать return в конце 
# print(div(5,2))

# def reverse_name(name:str="Alihan") ->str:
#     return name[::-1]
# print(reverse_name())
# print(reverse_name("Nurbolot"))

# def hello(word:str="Python") -> str:
#     print("Geeks")
#     return "Alihan"
#     print(word)
# print(hello())

# def calculator(num1:int=1,operator:str="+",num2:int=1) ->int:
#     "Базовая функция калькулятор на Python"
#     if operator == "+":
#         return num1 + num2
#     elif  operator == "-":
#         return num1 - num2
#     elif  operator == "*":
#         return num1 * num2
#     elif  operator == "/":
#         return num1 / num2
#     else:
#         return "Такого оператора нету"
# print(calculator(10,'*',10))
# print(calculator(10,"/",3))
# print(calculator(1,"Alihan",2))

################################################Args - kwargs
# print('hello','world','and','Python')

# def welcome(name,name2,name3):
#     print("Добро пожаловать",name)
#     print("Добро пожаловать",name2)
#     print("Добро пожаловать",name3)                   #args- помогает что бы не писать так много
# welcome("Nurbolot","Alihan","Kurmanbek")

# def args_welcome(*args):
#     print(type(args))                                   # так можно сокрашять
# args_welcome("Nurbolot","Alihan","Kurmanbek","Beksultan")

# def args_welcome(*args):                       #не обязательно писать args можно и другое что то писать
#     for name in args:
#         print("Добро пожаловать",name)           
# args_welcome("Nurbolot","Alihan","Kurmanbek","Beksultan","Askhat")

# def ang_student(name:str="Askhat",*points) ->str:
#     print(name,sum(points)/len(points),round(sum(points)/len(points)))
# ang_student('Alihan',3,3,3,3,3,4,4,4,4,4,5,2)
# ang_student('Askhat',2,2,2,2,2,2,2,2,2,2,2,2)
# ang_student("Nurbolot",5,5,5,5,5,5,5,5,5,5,5,5)

# def transleta(**words)->dict:
#     print(words)
# transleta(USA="США", Apple="яблоко",car='машина',phone="телефон")                           #нету ограниченчение

#lambda функция

# def simple_function(num:int) ->int:
#     return num * num 
# print(simple_function(20))

# lambda_fuction = lambda num:num*num
# print(lambda_fuction(20))

# print((lambda num:num*num)(25)                      # можно писать в одну строчку

#Пример 2

# def add(num1:int=10,num2:int=10) -> int:
#     return num1 + num2
# print(add(20,20))

# add_lambda = lambda num1,num2:num1 +num2             #нельзя указать типы данных
# print(add_lambda(20,20))

# print((lambda num1 ,num2:num1 + num2)(20,20))

#Пример 3
# numbers = [10,20,30,40,50]
# new_numbers = []
# def mult_two(nums:list) -> list:
#     for n in nums:
#         new_numbers.append(n*2)
#     return new_numbers
# print(mult_two(numbers))

# numbers = [10,20,30,40,50]
# new_numbers = list(map(lambda nums:nums *2,numbers))
# print(new_numbers)

# numbers = [10,20,30,40,50]
# print(list(map(lambda nums:nums*2,numbers)))

# print(list(map(lambda nums:nums *2 , [10,20,30,40,50])))

# Пример 4

# numbers = [10,3,4,5,6,555,333,1001,1002,1114]
# chet = []
# def check_chet(nums:list) -> list:
#     for num in nums:
#         if num % 2 == 0:
#             chet.append(num)
#     return chet 
# print(check_chet(numbers))

# numbers = [10,3,4,5,6,555,333,1001,1002,1114]
# chet = list(filter(lambda nums: nums % 2 == 0,numbers))
# print(chet)

# numbers = [10,3,4,5,6,555,333,1001,1002,1114]
# print(list(filter(lambda nums:nums % 2 == 0, numbers)))

# print(list(filter(lambda nums:nums % 2 == 0,  [10,3,4,5,6,555,333,1001,1002,1114])))
 