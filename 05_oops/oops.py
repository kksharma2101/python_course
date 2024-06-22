# Basic Class and Object
#    Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota", "kia")
# print(my_car.brand)


# ========== +++++++ ===========

# Class Method and Self
#    Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def full_name(self):
#         return f"{self.brand} {self.model}"


# my_car = Car("Toyota", "kia")
# print(my_car.brand)
# print(my_car.full_name())



# ========== +++++++ ===========

#  Inheritance
#    Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
# my_tesla = ElectricCar("Tesla", "Model S", "152kwh")
# print(my_tesla.model)
# print(my_tesla.full_name())


# ========== +++++++ ===========

# Encapsulation
#    Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
        
#     def get_brand(self):
#         return self.__brand + "true"
        
#     def full_name(self):
#         return f"{self.__brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
# my_tesla = ElectricCar("Tesla", "Model S", "152kwh")
# print(my_tesla.model)
# print(my_tesla.brand)



# ========== +++++++ ===========

# Polymorphism
    # Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
    
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
        
#     def get_brand(self):
#         return self.__brand , "true"
    
#     def fuel_type(self):
#         return "This is a Fuel car"
        
#     def full_name(self):
#         return f"{self.__brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#         return "This is a Electric car"    
        
# check = Car("tata", "Punch")
# print(check.fuel_type())

# electric = ElectricCar("Tesla", "jaguar", "670 kwh")
# print(electric.fuel_type())


# ========== +++++++ ===========

# 6.  Class Variables
    # Problem: Add a class variable to Car that keeps track of the number of cars created.

# class Car:
#     total_car = 0
    
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1
        
#     def get_brand(self):
#         return self.__brand , "true"
    
#     def fuel_type(self):
#         return "This is a Fuel car"
        
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
          
# Car("Tata", "Safari")  
# Car("Tata", "nexon")  
# print(Car.total_car)


# ========== +++++++ ===========

# Static Method
    # Problem: Add a static method to the Car class that returns a general description of a car.

# class Car:
#     total_car = 0
    
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1
        
#     def get_brand(self):
#         return self.__brand , "true"
    
#     def fuel_type(self):
#         return "This is a Fuel car"
        
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
     
#     @staticmethod    # Decorators
#     def general_description():
#          return "There is good Car Transport company"
     
# print(Car.general_description())
# check = Car("tata", "Punch")
# print(check.general_description())


# ========== +++++++ ===========

# Property Decorators
    # Problem: Use a property decorator in the Car class to make the model attribute read-only.

# class Car:
#     total_car = 0
    
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1
        
#     def get_brand(self):
#         return self.__brand , "true"
    
#     def fuel_type(self):
#         return "This is a Fuel car"
        
#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
     
#     @staticmethod    # Decorators , this is inhence the functionality
#     def general_description():
#          return "There is good Car Transport company"
    
#     @property   # This decorators change tha functionality we read the value
#     def model(self):
#         return self.__model
    
# cars = Car("Tata", "Audi")    
# # cars.model = "Scorpio"
# print(cars.model)


# ========== +++++++ ===========

# Class Inheritance and isinstance() Function
    # Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
    
# my_tesla = ElectricCar("Tesla", "Model S", "152kwh")

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))


# ========== +++++++ ===========

# Multiple Inheritance
    # Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is attery"
    
class Engine:
    def engine_info(self):
        return "This is Car Engine"
    
class ElectricCarTwo(Battery, Engine):
    pass

my_new_car = ElectricCarTwo()
print(my_new_car.battery_info())
print(my_new_car.engine_info())