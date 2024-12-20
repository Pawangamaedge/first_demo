def greeting(first_name,last_name):
     print(f"your first name is: {first_name}\n last name is:{last_name}")
# greeting('akash','sharma')

def default_fun(city='indore'):
     print(f'this is {city} city')
# default_fun()
# default_fun('ajmer')

lst=[2,3,4,5,6,8,10]
filter_method=print(filter([num for num in lst if num%2==0],lst))

print(filter_method)



def generate_squares(n):
    for i in range(n):
        yield i**2

squares = generate_squares(5)

# for square in squares:
#      print(square)
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))

def even_gen(num):
     for i in range(num):
          if i % 2 == 0:
               yield i

pr=even_gen(100)
# print(next(pr))
# print(next(pr))
# print(next(pr))
# print(next(pr))


class Person:
     def __init__(self, name, idnumber):
          self.name=name
          self.idnumber=idnumber

     def display(self):
          print(f"the names are: {self.name}\n and their id numbers: {self.idnumber}")
          
class Employee(Person):
     def __init__(self, name, idnumber, salary):
          super().__init__(name, idnumber)
          self.salary=salary

     def increment_hike(self, in_hike):
          self.n=in_hike
          salary_hike=self.salary*(self.n/100)
          self.salary=self.salary+salary_hike
          print(f"salary after hike: {self.salary}")

     def employe_display(self):
          print(f"the original salary is: {self.salary}")

E=Employee("ajay",10120121,25000)