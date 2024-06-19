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

def sum(num):
    return (num * (num + 1)) / 2

print(sum(4))    