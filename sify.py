#print("hello")
#print(2+3)
#x=10
#y=20
#print(type(x))
#list=['John',678,20.4,'Peter']
#list1=[456,'Andrew']    
#print(list)    
#print(list + list1)
#Data= input("")
#list=Data.split(",")
#tuple=tuple(list)
#print(list)
#print(tuple)
#dict = {'name': 'Pater', 'Age':18,'Roll_nu':101}  
#print(dict)
#color= ["Red","Green","White" ,"Black"]
#print(color[0],color[-1])
#from datetime import date
#date1 = date(2014, 7, 2)
#date2 = date(2014, 7, 11)
#days = date2 - date1
#print(days.days)
#char = input("")
#vowels=['a','e','i','o','u']
#if char in vowels:
 #   print("vowels")
#else:
 #   print("Not a Vowel")      

#class employee:  
   # def __init__(self, id, name,salary):  
      #  self.id=id
       # self.name = name    
       # self.salary = salary    
   # def details(self):  
        ### print(self.salary)
#employee1 = employee(1,"Ayan", 20000) 
#employee2=employee(2,"ben",30000)
#employee1.details() 
#employee2.details()
def division(dividend, divisor):
    try:
        
        result = dividend / divisor
        
        print("Result", result)
    except ArithmeticError:
        
        print("Arithmetic error ")

division(9,0)

