from sys import argv
s,user_name = argv
p='>'
print(f'hi {user_name}')
print(f'i like to ask you a few question {user_name}')
print(f'where do you live {user_name}')
like=input(p)
print(f'so you live in {like}\n')

###2nd Example..
script,file_name=argv
print(f'so your file is {file_name}')
f=open(file_name,'w')
f.truncate()
p=input('> ')
print('here is your file name :\n')
print(f.write(p))
f.close()
f=open(file_name,'r')
print(f.read())

##3rd...
scripts,file_name=argv
prompt='>'
print(f'files {file_name}',f'file_scripts {scripts}')

## 4th ....
