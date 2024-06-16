# print('Hello world')

def first(n):
    print(n);
# first('Krishna')

chai_one = "masala chai"
chai_two = "ginger tea"

# chai_one.lower()

# chai_one.upper()

# chai_one.strip()   # Remove first and last white spaces

# print(chai_one.replace("masala", "ginger"))  # Replace charachater

# chai_one.split(", ")   # Split seperate character list

# chai_two.find("tea")    # Find starting position of character

# chai_two.count("tea")    # Count character repeating


# =====****=====
chai_type = "masala"
quantity = 2
order = "I have ordered {} cups {} chai"

# print(order.format(quantity, chai_type))


# =====****=====
movies_list = ["Nagraaj", "Bahubali", "3-adiots", "artical-370"]

# print(" ".join(movies_list))
# print("-".join(movies_list))

# print(len(movies_list))

# for letter in movies_list: print(letter)   # This is loop 


# ======******=======

quotes = "He said, \"Artical-370 is awesome\" "
# print(quotes)

movie = "Nagraaj\n7Go"
# print(movie)

movie_two = r"Nagraaj\n7Go"   
# print(movie_two)     # r means row, this method give the row string


# ======= LIST ========

my_list = ["Ganesh","Ram", "Krishna", "Shiv", "Mahadev", "Hanuman"]

# my_list_copy = my_list.copy()
# my_list_copy.append("hello")
# print(my_list)
# print(my_list_copy)

# print(my_list[1:2])
# my_list[2:3] = "Radha" # Replace character but give the different result   - This is slice method
# my_list[2:3] = ["Radha"]   # Replace single char
# my_list[2:4] = ["Radha", "Sita"]   # Replace single char
# my_list[-1] = "Kamal"
# my_list.pop()  # Remove last element
# my_list.remove("element_name")   # Remove element by the name
# my_list.insert(position, "element_name")  # Add element espesfic position

# my_list_copy = my_list.copy()  # This copy method is give the another method


# == loop functions
# for item in my_list:print(item)

# for item in my_list:print(item, end=" - ")

# Comprihension loop in
my_squared = [x ** 2 for x in range(10)];
# print(my_squared)

# == Conditions 

# if "HariOm" in my_list: print(my_list)

# my_list.append("HariOm")

# if "HariOm" in my_list: print(my_list)



# ======= DICTIONARY ========

my_data = {"firstName": "kamal", "lastName": "sharma", "age": "24", "city": "bsr", "state": "UP"}
my_data["city"] = "noida"
# my_data.get("firstName")

# print(my_data["city"])
# print(my_data)

# === loop

# for data in my_data: print(data)
# for data in my_data: print(data,my_data[data])

# for key, value in my_data.items(): print(key, value)

# if "lastName" in my_data: print('I am a genius')

# my_data["dateOfBith"] = "12/12/1912"   # Add item
# my_data.update({"fullName": "jagira"})  #  Add new item

# my_data.pop("lastName") # Remove item
# my_data.popitem()  # Remove last item

del my_data["lastName"]  # Delete element in memory with reference

# print(my_data)

tea_shop = {"tea": {"masala":"spicy", "lemon": "tart"}, "tea_usa": {"oolang": "sweet", "ginger": "zesty"} }

# print(tea_shop["tea_usa"]["ginger"])

# squared_num = {x:x ** 2 for x in range(8)}

# print(squared_num)


keys = ["fullname", "age", "city"]

default_value = "kamal sharma"

new_dict = dict.fromkeys(keys, default_value)

# print(new_dict)


# ===== Tupal ======= > # this is immutable

num = (21,42,59,30,40)
tea_type = ("herbal", "Oolong", "herbal", "green")

merge = num + tea_type
counting = tea_type.count("herbal")
# print(counting)
# print(merge)


# Quetions on conditionals

# userscore = input("Give me a value: ")

# get_val = userscore / 2
# get_value = int(userscore)  # convert value string to number
# print(get_value/2)
# print(userscore)ss

# Age group categorization
#    Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# defineAge = input("Write your age : ")

# age = int(defineAge)

# if age <= 13:
#     print("child")
# elif age <= 20:
#      print("teenager")
# elif age <= 59:
#     print("adult")
# else: print("senior")

# Movie Ticket Pricing
#    Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# price = 12 if age >= 18 else 8

# day = "wednesday"

# if day == "wednesday":
#     price -= 2
# print("Ticket price for you $", price)


# Grade Calculator
#    Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# defineScore = input("Write your score : ")

# score = int(defineScore)

# if score >= 100:
#     print("Your score must be less then and equal 100")
#     exit()
# elif score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else: grade = "F"

# print(grade)


# Fruit Ripeness Checker
#    Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe).

# color = input("Give a color name : ")
# fruit = "banana"

# if fruit == "banana":
#     if color == "green":
#        print("unripe")
#     elif color == "yellow":
#        print("Ripe")
#     elif color == "brown":
#        print("Overripe")


#  Weather Activity Suggestion
#    Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
