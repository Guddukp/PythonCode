#use of good function that exit...
def Test(name):
    print('hi',name)
Test('guddu');Test('patel')

print()
print('ex-2')
def Tests(a,b):
    c=a*b
    return c
print(f'c = {Tests(2,5)}')

print()
print('example - 3')
def sum_num(a,b):
    c=a+b
    print('sum Answer is'+' '+str(c))
def sub_num(a,b):
    c=a-b
    print('sub Answer is'+' '+str(c))
def mul_num(a,b):
    c=a*b
    print('Mul Answer is'+' '+str(c))
def div_num(a,b):
    c=a/b
    print('div Answer is'+' '+str(c))
sum_num(20,23)
sub_num(39,34)
mul_num(24,38)
div_num(234,34)

print()
print('Example -4 for phone Num-')
def isphonenum(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
message='  415-555-0403 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    test=message[i:i+12] #i:i+12 using for index
    if isphonenum(test):
        print('phone num found '+test)
print('done')
print()

#Function all about decor lambda...
print('decoration(decor) function print..')
def apply_one(func,arg):
    return func(arg)
def add_five(x):
    return x+5
print('apply_one-',apply_one(add_five,10)) ##o/p=15

print()
def apply_twice(func,arg):
    return func(func(func(arg)))
###decoration function
def add_five(x):
    return x/3+x*8-x/25
print('apply_twice-',apply_twice(add_five,13))
print()
####anonymous(lambda) Function..
print('anonymous(lambda) Function..print')
def test(f,arg):
    return f(arg)
print('test-',test(lambda x:x/3,24)) ###def lambda(x):
                                                #return x/3
                                                #lambda(24) same chise in using lambda function
print()
print('example-2')
###normal function..
def test(x):
    return x**4+x*5+6
print('normal Function=',test(7))
###lambda function..
print('lambda function--',(lambda x:x**4+x*5+6)(7))
print()
##example-3
print('example-3')
triple=(lambda x:x**4)
add=(lambda x,y:x*y)
print('lambda=',triple(7))
print('Add=',add(23,34))
print()
##Function and all about map,filter..
print('#Function and all about map,filter..')

##function and map command. decor function
def add_five(x):
    return x+5
num=[12,14,16,17,19]#function and genrator or yield...
result1=list(map(add_five,num))
print('Result1=',result1)
##lambda...
num=[13,5,667,8,86]
result2=list(map(lambda x:x+34,num))
print('Result2=',result2)
##filter comand..using in function..
print()
print('##filter comand..using in function..')
def test(x):
    if x%2==0:
        return x
num=[22,34,55,66,77,88]
result3=list(filter(test,num))
print('Result3=',result3)

#ysing lambda in filter command..
num=[11,32,33,45,66,77,67,66]
result4=list(filter(lambda x:x%2!=0,num))
print('Result4=',result4)
print()

##function and genrator or yield... and itration will happand here
print('#function and genrator or yield...')
def countdown(x):
    while x>0:
        x-=1
        yield x

for i in countdown(20):
    print(i)
###genrator function create
print()
print('###genrator function create some condtion:')
def countdown(x):
    for i in range(x):
        if i%2==0:
            yield i
print('list=',list(countdown(20)))
for i in countdown(20):
    print(i)
print()

##create word..
print('create word..')
def  make_word():
    word=''
    for x in 'guddu':

        word+=x
        yield word
list_1=list(make_word())
print(list_1)
print()
###prime num..
print('prime num--')
def prime_num(n):
    prime =True
    for i in range(2,n):
        if n%i==0:
            prime=False
    return prime
sum=0
for i in range(2,30):
    if prime_num(i):
        print('prime number--',i)
        sum+=1
    else:
        print('non prime number--',i)
print('no of prime number=',sum)

print()
##Fabonice Series..1,2,3,5,8...
print('##Fabonice Series..1,2,3,5,8...')
first=1
second=2
while first <20:
    print(first)
    new=first+second
    first=second
    second=new
##function another example (first_name or last_name)
print()
print('##function another example (first_name or last_name)')
def get_format_name(first_name,last_name):
    """print fullName..."""
    full_name=first_name+' '+last_name
    return full_name.title()

d={
'actor':get_format_name('salman','khan'),
'cricketer':get_format_name('virat','kohali')
}

print('full Name actor :',d['actor'])
print('full Name cricketer :',d['cricketer'])
def Test(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name
print(Test('guddu','kumar'))
print(Test('rohan','nayak','kumar'))

##use while loop in function..
print()
print('##use while loop in function..')

while True:
    print('please Enter your name ')
    print('please Enter exit or e to exit')
    f_name=input('Enter First name :')
    if f_name=='exit'or f_name=='e':
        break
    l_name=input('Enter Last name :')
    if l_name=='exit' or l_name=='e':
        break
    fullName=get_format_name(f_name,l_name)
    print(fullName)
    repeat=input('You want to repeat Enter Yes and no Enter No')
    if repeat=='no':
        break

####for,list and list wit while in function...
print()
print('###for,list and list wit while in function...')
def user(names):
    for name in names:
        msg ='hello'+name.title()+'!'
        print(msg)
user_name=['guddu','patel','rohan']
user(user_name)
print()
##ex-1 use while loop in function
print('ex-1 use while loop in function')
def car(colors):
    cars=[]
    color=0
    max_index=len(colors)-1
    while color <=max_index:
        color+=1
        cars.append(colors)
    print('cars colection :',cars)

cars_list=['black car','blue car','yellow car']
car(cars_list)
#ex-2 use while loop in function
print()
print('ex-2 use while loop in function')
def Test(list1,list2):
    while list1:
        p=list1.pop()
        list2.append(p)
        print(list2)
    return list2
l1=['list1','list2','list3','list4','list4']
l2=['s1','s2','s3','s4','s5']
Test(l1,l2)

#universal function parameter..function(*abc)..
print()
print('#universal function parameter..function(*abc)..')
def test(*t):
    print(t)
test('2323',23,'guddujhjh','10-02-1998')

##universal function parameter..function(*abc).. for pizza example..
print()
print('#universal function parameter..function(*abc)..for pizza example..')
def pizza(size,*toppibgs):
    print('\n making a '+str(size)+'cmm pizza with folowing toppings ')
    for topping in toppibgs:
        print('-',topping.title())
pizza(200,'blackbery','panir','felfel')

##Dictionary use in function.....
print()
print('##Dictionary use in function.....')
def build_profile(first,last,**user_info):
    p={}
    p['first_name']=first
    p['last_name']=last
    for k,v in user_info.items():
        p[k]=v
    return p
m=build_profile('guddu','kumar',location='chennai',field='computer')
print(m)
