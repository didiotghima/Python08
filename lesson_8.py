# #Модули,работа с файлами
# def add(num1:int=10,num2:int=10) -> int:
#     return num1 +num2 

# def hello_word():
#     return "Hello world and Python"

# def welcome(name:str = "Nurbolot") -> str:
#     return "Hello" + name

# numbers = [1,2,3,4,5]

# it = 'geeks'

# f = open('hello.txt','w')
# f.write("Hello Geeks and Python!")
# f.close()

# r = open('hello.txt','r')
# print(r.read())
# r.close()

# py = open('test.txt','w')
# py.write("Hello word and test code")                       #создает пайтон файл
# py.close()

# read_code = open('moduls.py','r')
# print(read_code.read())
# read_code.close()

# test = open('kg.txt','w',encoding='utf-8')
# test.write('Привет Кыргызстан!Geeks Python')
# test.close()

# read_text = open('kg.txt','r',encoding='utf-8')
# print(read_text.read())
# read_text.close()

# numbers = open('numbers.txt','w',encoding='utf-8')
# numbers.write("0558486448\n")
# numbers.write("0706990208\n")
# numbers.write("0550135656\n")
# numbers.close()

# new_numbers = open('numbers.txt','a+',encoding='utf-8')
# new_numbers.write("0999887766\n")
# new_numbers.close()

# with open('wiki.txt','w',encoding='utf-8') as wiki:
#     wiki.write('Hello wiki')

# with open('wiki.txt','r',encoding='utf-8') as wiki_read:
#     print(wiki_read.read()) 

# name = "Askhat"
# surname = "Kydyrov"
# age = 18
# language = "python"
# is_learn = True
# print(f"Hello! I'm {name} {surname}.My age {age} and language {language}.Is learn {is_learn}")


# def func_contact():
#     with open('contact.txt','a+',encoding='utf-8')as c:
#         c.write("МЧС 112\n")
#     while True:
#         commands = input("1-посмотреть контакт,2-добавить,3-удалить")
#         if commands == "1":
#             with open('contact.txt','r',encoding='utf-8') as read_contact:
#                 print(read_contact.read())
#         elif commands == '2':
#             add_name = input("Имя:")
#             add_number = input("Номер:")
#             with open('contact.txt','a+',encoding='utf-8')as write_contact:
#                 write_contact.write(f"{add_name}{add_number}\n")
#             print(f"Контакт{add_name} успешно добавлено")
#         elif commands == '3':
#             delete_name = input("Имя которую вы хотите удалить:")
#             with open ('contact.txt','r+')as delete_contact:
#                 d = delete_contact.readlines()
#                 delete_contact.seek(0)
#                 for i in d:
#                     if i !=1:
#                         delete_contact.write(i)
#                 delete_contact.truncate()        
#         else:
#             print("Такой команнды нету") 
# func_contact()