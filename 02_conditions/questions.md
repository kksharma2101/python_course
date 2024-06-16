# Quetions on conditionals

1.  Age group categorization
    Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

    Ans. defineAge = input("Write your age : ")
    age = int(defineAge)
    if age <= 13:
    print("child")
    elif age <= 20:
    print("teenager")
    elif age <= 59:
    print("adult")
    else: print("senior")

2.  Movie Ticket Pricing
    Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

    Ans. price = 12 if age >= 18 else 8
    day = "wednesday"
    if day == "wednesday":
    price -= 2
    print("Ticket price for you $", price)

3.  Grade Calculator
    Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

    Ans. defineScore = input("Write your score : ")
    score = int(defineScore)
    if score >= 100:
    print("Your score must be less then and equal 100")
    exit()
    elif score >= 90:
    grade = "A"
    elif score >= 80:
    grade = "B"
    elif score >= 70:
    grade = "C"
    elif score >= 60:
    grade = "D"
    else: grade = "F"
    print(grade)

4.  Fruit Ripeness Checker
    Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe).

    Ans. color = input("Give a color name : ")
    fruit = "banana"

    if fruit == "banana":
    if color == "green":
    print("unripe")
    elif color == "yellow":
    print("Ripe")
    elif color == "brown":
    print("Overripe")

5.  Weather Activity Suggestion
    Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

    Ans. weather = input("give the weather value : ")

    if weather == "sunny":
    print("Go for a walk")
    elif weather == "rainy":
    print("Read a book")
    elif weather == "snowy" or weather == "Snowy":
    print("Build a snowman")

6.  Transportation Mode Selection
    Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

    Ans. transportation = input("Give distance : ")
    transportation_val = int(transportation)

    if transportation_val < 3:
    print("Walk")
    elif transportation_val < 15:
    print("Bike")
    elif transportation_val > 15:
    print("Car")

7.  Coffee Customization
    Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

    Ans. extra_shot = True
    order_size = "Medium"
    if extra_shot :
    coffee = order_size + " coffee with extra shot"
    else:
    coffee = order_size + " coffee"
    print(coffee)

8.  Password Strength Checker
    Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

    Ans. password = "123456789054"

    if len(password) < 6:
    print("Week")
    elif len(password) <= 10:
    print("Medium")
    else:
    print("Strong")

9.  Leap Year Checker
    Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

    Ans. year = 2001

    if( year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("This is leap year")
    else:
    print(year,"This is not leap year")

10. Pet Food Recommendation
    Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

    Ans. species = "dog"
    age = 1
    convert_to_lowercase = species.lower()

    if convert_to_lowercase == "dog" and age < 2:
    print("This is puppy food")
    elif convert_to_lowercase == "cat" and age >= 5:
    print("senior cat food")
    else:
    print("something is worng, please check it")
