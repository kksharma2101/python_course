# Loops Questions

1.  Counting Positive Numbers
    Problem: Given a list of numbers, count how many are positive.
    numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

    Ans. positive_num_count = 0
    for num in numbers:
    if num > 0:
    positive_num_count += 1
    print(positive_num_count)

2.  Sum of Even Numbers
    Problem: Calculate the sum of even numbers up to a given number n.

    Ans. n = 10;
    sum_of_even = 0

    for i in range(1, n+1):
    if i % 2 == 0:
    sum_of_even += i
    print(sum_of_even)

3.  Multiplication Table Printer
    Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

    Ans. number = 4
    for i in range(1, 11):
    if i == 5:
    continue

        print(number, "X", i, "=", number * i)

4.  Reverse a String
    Problem: Reverse a string using a loop.

    Ans. string = "kamal sharma"

        reverse_str = ''
        for char in string:
        reverse_str = char + reverse_str
        print(reverse_str)

5.  Find the First Non-Repeated Character
    Problem: Given a string, find the first non-repeated character.

    Ans. input_str = "python_code"

    for char in input_str:
    if input_str.count(char) == 1:
    print("Non-Repeated character is : ", char)
    break

6.  Factorial Calculator
    Problem: Compute the factorial of a number using a while loop.

    Ans. factorial = 1
    num = 1

    while num <= 5:
    factorial \*= num
    num = num+1
    print(factorial)

7.  Validate Input

    Ans. while True:
    number = int(input("Give a number between 1 to 10 : "))
    if 1 <= number <= 10:
    print("Thanks for give the number ", number)
    break
    else:
    print("You give the wrong number")

8.  Prime Number Checker
    Problem: Check if a number is prime.

    Ans. number = int(input("Give a prime number: "))

    if number > 1:
    for i in range(2, number):
    if (number % i) == 0:
    print(number, "is not a prime number and divisble by", i)
    break
    else:
    print("This is a prime number")
    break

9.  List Uniqueness Checker
    Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
    items = ["apple", "banana", "orange", "apple", "mango"]

    Ans. items = ["apple", "banana", "orange", "apple", "mango"]

    for i in items:
    if items.count(i) > 1:
    print(i, "is a duplicate")
    break

10. Exponential Backoff
    Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

    Ans. import time

    wait_time = 1
    max_retries = 5
    attempt = 0

    while attempt < max_retries:
    print("Attempt",attempt + 1, "wait time is", wait_time)
    time.sleep(wait_time)
    wait_time \*= 2
    attempt += 1
