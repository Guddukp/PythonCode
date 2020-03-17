import json
file_name='username.json'
try:
    with open(file_name,'r')as file:
        user_Name=json.load(file)
except FileNotFoundError:
    user_Name=input('what is your username :')
    with open(file_name,'w')as file:
        json.dump(user_Name,file)
        print('well remember you when you come back '+user_Name+' !')
else:
    print('welcome back '+user_Name+' !')


##simple try and except error..
try:
    a=10
    print(a+b)
except ZeroDivisionError:
    print('Zerro Division error')
except NameError:
    print('name error.')

try:
    num=29
    print(num/0)
except (ZeroDivisionError,TypeError):
    print('Except Statement')

try:
    name='Guddu'
    print(name+kumar)
except:
    print('except statment without error')
finally:
    print('Finally statment.')
