#inherit the class through the object
class Test(object):
    """docstring for ."""

    def __init__(self, name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+'is now sitting')
    def sit2(self):
        print(self.name.title(),str(self.age))
persion1=Test('ali',30)
persion1.sit()
persion1.sit2()

###Example-2
print('###Example-2')

class Car(object):
    """docstring for constructor."""

    def __init__(self,name,model,year):
         self.name=name
         self.model=model
         self.year=year
         self.km_reading=0
    def get_det(self):
            long_name=str(self.year)+' '+self.name+' '+self.model
            return long_name.title()
    def read_km(self):
        """print about km reading"""
        print('This car has '+str(self.km_reading)+' km on it')


    def update_km(self,km):
        """print the update_km"""
        if km>=self.km_reading:
            self.km_reading = km
        else :
            print('you canot roll back km..')

my_new_car=Car('audi','a41',2013)

print(my_new_car.get_det())
my_new_car.update_km(100)
print(my_new_car.read_km())

##parent and child class... Example 3

class Parent():
    def __init__(self,name,age=23):
        self.name=name
        self.age=age
    def print_info(self):
        full_name=self.name+' '+str(self.age)
        print(full_name)
class Child(Parent):
    def _init_(self,name,age):
        super()._init_(name,age)

m=Parent('guddu')
m.print_info()

n=Child('Rohan',31)
n.print_info()


####List use in class...
class List():
    def __init__ (self,list1):
        self.list1=[]
        self.list2=list1
    def print_list(self):
        for i in self.list1:
            print('_',i)
    def print_list2(self):
        for i in self.list2:
            print('_',i)
    def append_list(self,l):
        for i in l:
            self.list1.append(i)
my_list=List(['guddu','patel','rohit','sayam'])
my_list.append_list(['wefwf','gtggt','jhrjwh'])
my_list.print_list()

###splitclass...
class Split():
    def __init__(self,l):
        self.l=l
    def print_l(self):
        if type(self.l)==type(''):
            s=(self.l).Split()
            print(s,'is string')
            for i in l:
                print('_',i)
        elif type(self.l)==type([]):
            print(self.l,'is list')
            for i in self.l:
                print('_',i)
split=Split(['hi','this','is','python'])
split.print_l()
