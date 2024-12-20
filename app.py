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

