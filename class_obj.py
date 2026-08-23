# class Collage:
#     clgname="SMIT"
#     name="Annonymus"
#     def __init__(self,name,marks):
#         self.marks=marks
#         self.name=name
#         print("Hello Student")
#     @staticmethod
#     def welcome():
#         print("Welcome Student")
#     def get_marks(self):
#         return self.marks
# s1=Collage("Tirtho",98)
# print(s1.name,s1.clgname)
# print(s1.get_marks())
# s1.welcome()

# class Student:
#     def __init__(self,sub1,sub2,sub3,m1,m2,m3):
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         print(self.sub1,self.m1)
#         print(self.sub2,self.m2)
#         print(self.sub3,self.m3)
#         print("Avg",(self.m1+self.m2+self.m3)/3)

# s1=Student("Maths","Phy","Chem",98,97,84) 
# s1.avg()

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print("Average score of ",self.name,"is",sum/3 )

# s1=student("Steve",[98,97,99])
# s1.get_avg()

# class Bank:
#     def __init__(self,acc,bal):
#         self.account_no=acc
#         self.balance=bal
    
#     def get_bal(self):
#         return self.balance
    
#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount,"was credited")
#         print("Total Balance=",self.get_bal())
    
#     def debit(self,amount):
#             self.balance-=amount
#             print("Rs.",amount,"was debited")
#             print("Total Balance=",self.get_bal())
# s1=Bank(202600282,1000000)
# s1.credit(5000)
# s1.debit(6000)
# print("The account no.",s1.account_no)
# s2=Bank(202600368,10000)
# s2.credit(5000)
# s2.debit(6000)
# print("The account no.",s2.account_no)

# class rectangle:
#     def prop(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         self.area=self.length*self.breadth
#         print(self.area)
#     def perimeter(self):
#         self.perimeter=2*(self.length+self.breadth)
#         print(self.perimeter)
# rec1=rectangle()
# rec1.prop(4,3)
# rec1.area()
# rec1.perimeter()
# rec2=rectangle()
# rec2.prop(5,6)
# rec2.area()
# rec2.perimeter()

# class circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         self.area=3.141*self.radius**2
#         print(self.area)
#     def cir(self):
#         self.cir=2*3.141*self.radius
#         print(self.cir)

# cir1=circle(5)
# cir1.area()
# cir1.cir()

# class cart:
#     def __init__(self,name):
#         self.name=name
#     def addd_item(self,item):
#         self.name.append(item)
#         print(self.name)
#     def remove_item(self,item):
#         self.name.remove(item)
#         print(self.name)

# c1=cart(["apple","banana","can of soda","charger"])
# c1.addd_item("mobile")
# c1.remove_item("apple")

# class circle:
#     def __init__(self, r):
#         self.radius=r
#     def area(self):
#         return self.radius**2 * 3.141
#     def perimeter(self):
#         return 2*3.141*self.radius
# r1=circle(5)
# print(r1.area(),r1.perimeter())

# class Employee:
#     def __init__(self, role, dept, sal):
#         self.role = role
#         self.dept = dept
#         self.sal = sal

#     def show(self):
#         print("Role:", self.role)
#         print("Department:", self.dept)
#         print("Salary:", self.sal)
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "100000")
# e2 = Engineer("Bobby Deol", 56)
# e2.show()

# class order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
#     def __gt__(self,odr):
#         return self.price > odr.price
# odr2=order("coffee",80)
# odr1=order("chips",20)
# print(odr2.__gt__(odr1))

# class employee :
#     def __init__(self,name,sal,per):
#         self.name=name
#         self.sal=sal
#         self.per=per
#     def increase_sal(self):
#         self.sal=self.sal + (self.sal*self.per/100)
#     def show(self):
#         self.increase_sal()
#         print("Name",self.name)
#         print("Salary",self.sal)
# e1=employee("Rahul",7000,10)
# e1.show()

# class counter:
#     def __init__(self,count):
#         self.count=count
#     def incremeant(self):
#         self.count+=1
#     def decreament(self):
#         self.count-=1
#     def show(self):
#         print(self.count)
# c1=counter(0)
# c1.incremeant()
# c1.incremeant()
# c1.show()

# class circle:
#     def __init__(self,rad):
#         self.rad=rad

#     def area(self):
#         return self.rad**2*(22/7)
# c1=circle(10)
# c2=circle(20)
# state= "True" if (c1.area()>c2.area()) else "False"
# print(state)

# class shopping_cart:
#     def __init__(self,cart,item_add,item_rem):
#         self.item_add=item_add
#         self.cart=cart
#         self.item_rem=item_rem
#     def add(self):
#         self.cart=self.cart.union(self.item_add)
#     def rem(self):
#         self.cart=self.cart-self.item_rem
#     def show(self):
#         print("Cart",self.cart)
# c1=shopping_cart({"Apple","Banana","Grapes","Eggs","Milk","Chicken","Battery"},{"Water","flour"},{"Banana","Grapes"})
# c1.add()
# c1.rem()
# c1.show()

# class dunder:
#     def __init__(self,odr,prc):
#         self.odr=odr
#         self.prc=prc
#     def __gt__(self,odr2):
#         return self.prc>odr2.prc
# odr1=dunder("Chips",20)
# odr2=dunder("Water",15)
# print(odr2.__gt__(odr1))

# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def __add__(self,p2):
#         return complex(self.real+p2.real,self.img+p2.img)
# p1=complex(1,4)
# p2=complex(3,5)
# p3=p2 + p1
# print(p3.real,"+",p3.img,"i") 

# class representation:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __str__(self):
#         return f"Name:{self.name}\nMarks:{self.marks}"
# s1=representation("Tirtho",98)
# print(s1)

