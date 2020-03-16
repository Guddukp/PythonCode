import json
import sys
file_name=sys.argv[1]
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
