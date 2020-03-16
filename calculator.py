while True:
    print('Please Enter num to calc')
    a=int(input('Please Enter First Num :'))
    b=int(input('Please Enter second Num :'))
    print('Enter "sum" to addtion ')
    print('Enter "sub" to Subtraction')
    print('Enter "mul" to Multipliction')
    print('Enter "div" to Division')
    print('press exit or e to finish the calc')
    user_input=input('>')
    if user_input=='exit' or user_input=='e':
        break
    elif user_input=='sum':
        c=a+b
    elif user_input=='sub':
        c=a-b
    elif user_input=='mul':
        c=a*b
    elif user_input=='div':
        c=a/b
    print(f'Answer of {user_input} is {c}')
    print('You want to continue press "yes" and Not press "no" ')
    user_input=input('>')
    if user_input=='no':
        break
print('finish')


print('Example No -2 for calculator--')
while True:
    print('Please Enter num to calc')

    print('Enter "sum" to addtion ')
    print('Enter "sub" to Subtraction')
    print('Enter "mul" to Multipliction')
    print('Enter "div" to Division')
    print('press exit or e to finish the calc')
    user_input=input('>')
    if user_input=='exit' or user_input=='e':
        break
    elif user_input=='sum':
        a=int(input('Please Enter First Num :'))
        b=int(input('Please Enter second Num :'))
        c=a+b
    elif user_input=='sub':
        a=int(input('Please Enter First Num :'))
        b=int(input('Please Enter second Num :'))
        c=a-b
    elif user_input=='mul':
        a=int(input('Please Enter First Num :'))
        b=int(input('Please Enter second Num :'))
        c=a*b
    elif user_input=='div':
        a=int(input('Please Enter First Num :'))
        b=int(input('Please Enter second Num :'))
        c=a/b
    else:
        print('Select sum or sub or div or mul ')
        print()
        print('Now Countinue')
        continue
    print(f'Answer of {user_input} is {c}')
print('finish')
