import json
def greet_user():
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
greet_user()

##2nd ex....
def road_user():
    file_name='username.json'
    try:
        with open(file_name)as file:
            user_Name=json.laod(file)
    except FileNotFoundError:
        return none
    else:
        return user_Name
def store_user():
    user_Name=greet_user()
    if user_Name:
        print('Welcome back '+user_Name)
    else:
        user_Name=input('whats your username? ')
        file_name='username.json'
        with open(file_name,'w')as file:
            json.dump(user_Name,file)
            print(f'well remember you when you come back '+user_Name+' !')
store_user()
##3rd .....
def get_store_username():
    """If username available"""
    filename1='username.json'
    try:
        with open(filename1)as file:
            username1=json.load(file)
    except FileNotFoundError:
        return none
    else:
        return username1
def get_new_user():
    """If New Username prompt.."""
    username1=input('whats your username ')
    filename1='username.json'
    with open(filename1,'w')as file:
        json.dump(username1,file)
    return username1

def greet_user1():
    """Printing Username """
    username1=get_new_user()
    if username1:
        print('welcome back '+username1+' !')
    else:
        username1=get_store_username()
        print('well remember you when you come back'+username1+' !')
greet_user1()
