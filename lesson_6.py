#функция - functions             внутри функций можно все писать
# print('geeks')
# def hello_world():
#     print("hello world")
# hello_world()

# def add():
#     num1 = int(input("Number1: "))
#     num2 = int(input("number2: "))
#     print(num1 + num2)n
# add()

# def count_numbers():
#     numbers = [1,2,3,4,5,6,7,8,9,10]
#     for number in numbers:
#         if number % 2 == 0:
#             print(number,"четный")
#         else:
# #             print(number,"нечетный")
# # count_numbers()

# def reverse_word(word):
#     print(word[::-1])
# reverse_word("geeks")
# reverse_word("python")
# reverse_word("Django")

# def hello(name):
#     print("Привет",name)
# hello("Kurmanbek")
# hello("Beksultan")

#вы функции нужно писть в первый очередь def
# def test(word:str) ->str:
#     "My testing function "            #не обязательно писать так 
#     print(word+word)
# test("geeks")
# test(10)

# def mult(num1:int=1, num2:int=1) ->int:
#     print("Ответ",num1*num2)
# mult(10,10)
# mult(10,20)

# def calculator(num1:int=1,num2:int=1,operator:str='+') -> int:
#     "Simple calculator Python with function def"
#     if operator =='+':
#         print("ответ:",num1+num2)
#     elif operator =='-':
#         print("ответ:",num1-num2)
#     elif operator =='*':
#         print("ответ:",num1*num2)
#     elif operator =='/':
#         print("Ответ:",num1/num2)
#     else:
#         print("Такого оператора нету")
# calculator(10,10,"*")
# calculator(10,10,"/")
# calculator(10,10,"-")
# calculator(10,10,"+")
# calculator(10,0,"/")

# print(10 / 0)                 #на пайтоне нельзя делить на ноль

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Деление на ноль")

# try:
#     print(10+'5')
# except TypeError:
#     print("Ошибка типа данных")

# try:
#     print(10+10)
# except BaseException:               #можно написать это им все                   
#     print("code error")
    
# while True:
#         try :
#                 num1 = int(input("Number1:"))
#                 operator = input("Operator1:")
#                 num2 = int(input("Number2: "))      
#                 if operator =='+':
#                         print("ответ:",num1+num2)
#                 elif operator =='-':
#                         print("ответ:",num1-num2)
#                 elif operator =='*':
#                         print("ответ:",num1*num2)
#                 elif operator =='/':
#                         try:
#                                 print("Ответ:",num1/num2)
                        
#                         except ZeroDivisionError:
#                                 print("Деление на ноль")
#                 else:
#                         print("Такого оператора нету")

#         except ValueError:
#                 print("Введите цифры")
