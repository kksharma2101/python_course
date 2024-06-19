# Basic Function Syntax
#    Problem: Write a function to calculate and return the square of a number.

def find_square(number):
    return number ** 2

result = find_square(5)
# print(result)


# ========= ++++++ ========

# Function with Multiple Parameters
#    Problem: Create a function that takes two numbers as parameters and returns their sum.

def sum_of_numbers(num1, num2):
    return num1 + num2

# print(sum_of_numbers(15,30))


# ========= ++++++ ========

#  Polymorphism in Functions
#    Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# def multiply(num_one,num_two):
#     return num_one * num_two
# print(multiply(20,5))
# print(multiply(8,"k"))
# print(multiply("8", 6))


# ========= ++++++ ========

# Function Returning Multiple Values
#    Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
# circumference = 2 * pi * r
# area = pi * r ** 2
def area_of_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = area_of_circumference(2)
# print("area: ", a, "circumference: ", c)
# print(area_of_circumference(4))


# ========= ++++++ ========

# Default Parameter Value
#    Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greeting(greet = "Hello"):
    return greet

# print(greeting("Users"))


# ========= ++++++ ========

# Lambda Function
#    Problem: Create a lambda function to compute the cube of a number.

cube = lambda number: number ** 3  # This function use only one time

# print(cube(4))


# ========= ++++++ ========

# Function with \*args
#    Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    return sum(args)

# print(sum_all(4,2,3))    
# print(sum_all(4,2,3,5,3))    
# print(sum_all(4,2,3,5,3,65,7))    


# ========= ++++++ ========

# Function with \*\*kwargs
#    Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwarg(**kwargs) :
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_kwarg(name = "kamal", value = "sharma")
# print_kwarg(name = "pandit", power = "natural", enemy = "people")


# ========= ++++++ ========

#  Generator Function with yield
#    Problem: Write a generator function that yields even numbers up to a specified limit.

def generate_even(num):
    for i in range(2, num + 1, 2):
        yield i

# for num in generate_even(20):
    # print(num)    


# ========= ++++++ ========

# Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def calculate_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)

# print(calculate_factorial(5))