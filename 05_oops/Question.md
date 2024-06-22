# learn about Object Oriented Programming by answering these questions

1. Basic Class and Object
   Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

   Ans. class Car:
   def **init**(self, brand, model):
   self.brand = brand
   self.model = model

   my_car = Car("Toyota", "kia")
   print(my_car.brand)

2. Class Method and Self
   Problem: Add a method to the Car class that displays the full name of the car (brand and model).

   Ans. class Car:
   def **init**(self, brand, model):
   self.brand = brand
   self.model = model
   def full_name(self):
   return f"{self.brand} {self.model}"

   my_car = Car("Toyota", "kia")
   print(my_car.full_name())

3. Inheritance
   Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

   Ans. class Car:
   def **init**(self, brand, model):
   self.brand = brand
   self.model = model
   def full_name(self):
   return f"{self.brand} {self.model}"

   class ElectricCar(Car):
   def **init**(self, brand, model, battery_size):
   super().**init**(brand, model)
   self.battery_size = battery_size

   my_tesla = ElectricCar("Tesla", "Model S", "152kwh")
   print(my_tesla.model)
   print(my_tesla.full_name())

4. Encapsulation
   Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

   Ans.

5. Polymorphism
   Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

   Ans.

6. Class Variables
   Problem: Add a class variable to Car that keeps track of the number of cars created.

   Ans.

7. Static Method
   Problem: Add a static method to the Car class that returns a general description of a car.

   Ans.

8. Property Decorators
   Problem: Use a property decorator in the Car class to make the model attribute read-only.

   Ans.

9. Class Inheritance and isinstance() Function
   Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

   Ans.

10. Multiple Inheritance
    Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
