# print('Hello world')

def first(n):
    print(n);
# first('Krishna')

chai_one = "masala chai"
chai_two = "ginger tea"

# chai_one.lower()

# chai_one.upper()

# chai_one.strip()   // Remove first and last white spaces

# print(chai_one.replace("masala", "ginger"))  // Replace charachater

# chai_one.split(", ")   // Split seperate character list

# chai_two.find("tea")    // Find starting position of character

# chai_two.count("tea")    // Count character repeating


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

# for letter in movies_list: print(letter)   // This is loop 


# ======******=======

quotes = "He said, \"Artical-370 is awesome\" "
# print(quotes)

movie = "Nagraaj\n7Go"
# print(movie)

movie_two = r"Nagraaj\n7Go"   
# print(movie_two)     // r means row, this method give the row string


# ======= LIST ========

my_list = ["Ganesh","Ram", "Krishna", "Shiv", "Mahadev", "Hanuman"]
# my_list_copy = my_list.copy()
# my_list_copy.append("hello")
# print(my_list)
# print(my_list_copy)

# print(my_list[1:2])
# my_list[2:3] = "Radha" // Replace character but give the different result   - This is slice method
# my_list[2:3] = ["Radha"]   // Replace single char
# my_list[2:4] = ["Radha", "Sita"]   // Replace single char
# my_list[-1] = "Kamal"
# my_list.pop()  // Remove last element
# my_list.remove("element_name")   // Remove element by the name
# my_list.insert(position, "element_name")  // Add element espesfic position

# my_list_copy = my_list.copy()  // This copy method is give the another method


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