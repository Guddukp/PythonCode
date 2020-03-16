import json
num=[1,2,3,4,5]
filename='num.json'
with open(filename,'w')as file:
    json.dump(num,file)

fileName='username.json'
username=input('please enter your username :')
with open(fileName,'w')as file:
    json.dump(username,file)
    print(f'well remember you when you come back {username} !')
 
