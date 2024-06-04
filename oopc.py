'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hi(self):
        print('hello,my name is ',self.name,'and age is',self.age)
p=Person('Manish',20)
p.say_hi()'''


# in oops 
# attribute=variables
# methods=functions

# oops in python
# class Person:
    # def _init_(venkat,name): 'constructor'
#         venkat.name=name      
#     def say_hi(venkat):       'method' 
#         print('hello,my name is',venkat.name)
# p=Person("subhan")   'object'
# p.say_hi()     'accessing method using object

# class Person:
#     def _init_(venkat,name,age): #'constructor'
#         venkat.name=name
#         venkat.age=age     
    
#     def say_hi(venkat):       #'method' 
#         print('hello,my name is',venkat.name)
#         print('my age is',venkat.age)
# p=Person("subhan", 30)   #'object'
# p.say_hi()    # 'accessing method using object'

# 4 pillars of oops
# 1.inheiritance
# 2.data encapsulation
# 3.data abstraction
# 4.polymorphism

class Test:
    def __init__(self):
        self.x=0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y=1
def main():
    b= Derived_Test()
    print(b.x,b.y)
main()

# class Animals:
#     def _init_(self,name,species,sound):
#         self.name=name
#         self.species=species
#         self.sound=sound
#     def make_sound(self):
#         print(f"The {self.species} named {self.name} sounds {self.sound} ")
# class Lion(Animals):
#     def get_info(self):
#         print("lions are the kings of the jungle")
# class Elephant(Animals):
#     def get_info(self):
#         print("Elephants are the largest land animals")
# class Snake(Animals):
#     def get_info(self):
#         print("Snakes can be found on every continent except antartica")

# obj=Animals('lion', 'leo', 'roar')
# obj.make_sound()
# li=Lion(Animals)
# li.get_info(self)

# class Animals:
#     def init(self,name,species,sound):
#         self.name=name
#         self.species=species
#         self.sound=sound
#     def make_sound(self):
#         print(f"The {self.species} named {self.name} sounds '{self.sound}' ")
# class Lion(Animals):
#     def _init_(self,name):
#         super()._init_(name, "Lion","roar")
#     def get_info(self):
#         print("lions are the kings of the jungle")
# class Elephant(Animals):
#     def _init_(self,name):
#         super()._init_(name, "Elephant","Trumpet")
#     def get_info(self):
#         print("Elephants are the largest land animals")
# class Snake(Animals):
#     def _init_(self,name):
#         super()._init_(name, "Snake","Hiss")
#     def get_info(self):
#         print("Snakes can be found on every continent except antartica")

# leo = Lion("Leo")
# ellie = Elephant("Ellie")
# slyther = Snake("Slyther")

# leo.make_sound()
# leo.get_info()
# print()

# ellie.make_sound()
# ellie.get_info()
# print()

# slyther.make_sound()
# slyther.get_info()
# print()
