# Object type / Data type

- Number : 1234, 3.142, 3+4j, 0b111, Decimal(), Frection()

- String : "abc", 'kamal's", b'cd3/1y0'

- List : [2,[5,"kamal"], 9, "radhey", 5.5], list(range(10))

- Tuple : (1, "spam", 8, "k"), tuple('spam'), namedtuple

- Dictionary : {'food': "chapati", "age": 24, }, dict(hours=10)

- Set : set('abc'), {"a", 'v', 'c'} // this method keep only common values;

- File : open('eggs.txt'), open(r'C:/ham.bin', wb);

- Boolean : True / False;

- None : None;

- Functions, Modules, Classes;

- Advance : Decorators, Generators, Iterators, MetaPrograming ;

# Quetions on conditionals

1. Age group categorization
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

2. Movie Ticket Pricing
   Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

   Ans. price = 12 if age >= 18 else 8
   day = "wednesday"
   if day == "wednesday":
   price -= 2
   print("Ticket price for you $", price)

3. Grade Calculator
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

4. Fruit Ripeness Checker
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

5. Weather Activity Suggestion
   Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

6. Transportation Mode Selection
   Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

7. Coffee Customization
   Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

8. Password Strength Checker
   Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

9. Leap Year Checker
   Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

10. Pet Food Recommendation
    Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
