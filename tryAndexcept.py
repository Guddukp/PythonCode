n=int(input('Enter the first num :'))
n2=int(input('Enter the another Num :'))
try:
    print(n/n2)
except ZeroDivisionError:
    print('the Answer is Zero')

##2nd ex...
print('\nGive me two numbers :')
print('\nIf you want to quit than press "q" ')
while True:
    first_num=input('\nFirst Number :')
    if first_num=='q':
        break
    second_num=input('Second Number :')
    if second_num=='q':
        break
    try:
        answer=int(first_num)/int(second_num)
    except ZeroDivisionError:
        print('Answer is 0 or Zero')
    else:
        print(answer)
def my_func(x):
    assert x>0,'error'
    print(x)
my_func(-2)
