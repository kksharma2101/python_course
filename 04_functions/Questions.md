1. Basic Function Syntax
   Problem: Write a function to calculate and return the square of a number.

   Ans. def find_square(number):
   return number \*\* 2
   result = find_square(5)
   print(result)

2. Function with Multiple Parameters
   Problem: Create a function that takes two numbers as parameters and returns their sum.

   Ans. def sum_of_numbers(num1, num2):
   return num1 + num2
   print(sum_of_numbers(15,30))

3. Polymorphism in Functions
   Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

   Ans. def multiply(num_one,num_two):
   return num_one \* num_two
   print(multiply(20,5))
   print(multiply(8,"k"))
   print(multiply("8", 6))

4. Function Returning Multiple Values
   Problem: Create a function that returns both the area and circumference of a circle given its radius.

   Ans. import math
   circumference = 2 _ pi _ r
   area = pi \_ r \*\* 2

   def area*of_circumference(radius):
   area = math.pi * radius \*_ 2
   circumference = 2 _ math.pi \* radius
   return area, circumference

   a, c = area_of_circumference(2)
   print("area: ", a, "circumference: ", c)

   print(area_of_circumference(4))

5. Default Parameter Value
   Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

   Ans. def greeting(greet = "Hello"):
   return greet

   print(greeting("Users"))

6. Lambda Function
   Problem: Create a lambda function to compute the cube of a number.

   Ans. cube = lambda number: number \*\* 3 # This function use only one time

   print(cube(4))

7. Function with \*args
   Problem: Write a function that takes variable number of arguments and returns their sum.

   Ans. def sum_all(\*args):
   return sum(args)

   print(sum_all(4,2,3))  
   print(sum_all(4,2,3,5,3))  
   print(sum_all(4,2,3,5,3,65,7))

8. Function with \*\*kwargs
   Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

   Ans. def print_kwarg(\*\*kwargs) :
   for key, value in kwargs.items():
   print(f"{key}: {value}")

   print_kwarg(name = "kamal", value = "sharma")
   print_kwarg(name = "pandit", power = "natural", enemy = "people")

9. Generator Function with yield
   Problem: Write a generator function that yields even numbers up to a specified limit.

   Ans. def generate_even(num):
   for i in range(2, num + 1, 2):
   yield i

   for num in generate_even(20):
   print(num)

10. Recursive Function
    Problem: Create a recursive function to calculate the factorial of a number.

    Ans. def calculate_factorial(num):
    if num == 0:
    return 1
    else:
    return num \* calculate_factorial(num - 1)

    print(calculate_factorial(5))
