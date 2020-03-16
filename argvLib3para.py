from sys import argv,exit
script,from_file,to_file = argv
print(f'copying from {from_file} to {to_file}')
print('If you don,t want to press e and exit')
i=input('! yes/no > ')
if i=='e' or i=='exit':
    exit(0)
file_1=open(from_file)
file_1.read()
print(f'jkhjkhkv vjnfvjfn {len(file_1)}')

file_2=open(to_file,'w')
file_2.write(file_1)
print('print all name: ')
file_2.close()
file_1.close()
