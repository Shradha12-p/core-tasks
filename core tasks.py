#CREATE CUSTOM CLASSES
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Example usage
book1 = Book("Atomic Habits", "James Clear", 320)
print(book1.display_info())


#INHERITANCE AND ACCESS MODIFIERS(Vehicle Management system)
class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand            # protected
        self.__model = model           # private

    def show_details(self):
        return f"Brand: {self._brand}, Model: {self.__model}"

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def show_details(self):
        base_details = super().show_details()
        return f"{base_details}, Fuel Type: {self.fuel_type}"

# Example usage
car = Car("Toyota", "Innova", "Diesel")
print(car.show_details())


#FILE-BASED DATA STORAGE(User Feedback Collector )
def collect_feedback():
    feedback = input("Enter your feedback: ")
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")
    print("Thanks for your feedback!")

def read_feedback():
    print("Previous Feedbacks:")
    with open("feedback.txt", "r") as file:
        for line in file:
            print("-", line.strip())

# Example usage
collect_feedback()
read_feedback()


#EXCEPTION-SAFE CODE(Safe calculator )
def safe_calculator():
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        else:
            raise ValueError("Invalid operator")

        print("Result:", result)

    except ValueError as ve:
        print("Value Error:", ve)
    except ZeroDivisionError as zde:
        print("Math Error:", zde)
    except Exception as e:
        print("Unexpected Error:", e)

# Example usage
safe_calculator()
