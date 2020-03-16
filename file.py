f = open('file.txt','w')
f.write('hello world')##write the text...
f.close()
f=open('files.txt','r')##Read the text...
print(f.read())

###2nd method..
with open('file.txt','w') as f:
    f.write('my name is khan')
f.close()
with open('file.txt','r') as f:
    f=f.read()
print(f)
print(f.rstrip())

###file paths... and readlines()....and rstrip()
file_path='C:/Users/guddu/AppData/Local/atom/app-1.42.0/programess/file.txt'
with open(file_path,'w') as f:
    f.write('my name is khan \n what is your name \n thats goood')
f.close()
with open(file_path,'r') as f:
    line=f.readlines()
string=''
for i in line:
    string+=i
    print(i.rstrip())### rstrip(). it removes trailing spaces.
if 'khan' in string:
    print('Yes')
else:
    print('No')
