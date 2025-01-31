import tkinter as tk
from tkinter import scrolledtext, ttk
import sys
import io
from PIL import Image, ImageTk
from abc import ABC, abstractmethod 

def oop_window():
    OOPApp()

class OOPApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("OOP Learning Menu")
        self.geometry("1000x780")
        
        self.bg_image = Image.open("bgApp.jpg").resize((1000, 780), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.canvas = tk.Canvas(self, width=1000, height=780, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        self.canvas.create_text(500, 50, text="Learn OOP Concepts", font=("Helvetica Neue", 24, "bold"), fill="white")
        
        options = ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"]
        y_pos = 150
        
        for option in options:
            self.create_button(option, lambda opt=option: self.show_concept(opt), y_pos)
            y_pos += 70
        
        self.create_button("Back", self.destroy, 450, "#d9534f")
    
    def create_button(self, text, command, y_pos, normal_bg="#4CAF50"):
        button = ttk.Button(self, text=text, command=command, style="Custom.TButton")
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Helvetica Neue", 16), padding=12, width=19, relief="flat", foreground="black")
        style.map("Custom.TButton", background=[("active", "grey"), ("!active", normal_bg)])
        self.canvas.create_window(500, y_pos, window=button)
    
    def show_concept(self, concept):
        ConceptWindow(self, concept)

class ConceptWindow(tk.Toplevel):
    def __init__(self, parent, concept):
        super().__init__(parent)
        self.title(concept)
        self.geometry("1000x780")
        
        self.bg_image = Image.open("bgApp.jpg").resize((1000, 780), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.canvas = tk.Canvas(self, width=1000, height=780, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        explanations = {
            "Inheritance": "Inheritance allows one class to acquire the properties and methods of another.",
            "Encapsulation": "Encapsulation restricts direct access to some of an object's components.",
            "Polymorphism": "Polymorphism allows methods to do different things based on the object it is acting upon.",
            "Abstraction": "Abstraction hides the complexity and only exposes the essential parts."
        }
        
        examples = {
            "Inheritance": """
class User:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("Name =", self.name)

class Programmer(User):
    def doPython(self):
        print("Programming Python")

brian = User("Brian")
brian.printName()

diana = Programmer("Diana")
diana.printName()
diana.doPython()
            """,
            "Encapsulation": """
class Mobile:
    def __init__(self):
        self.__os = 'android'
    def switch_on(self):
        print('Mobile OS is', self.__os)
    def set_os(self, os):
        self.__os = os

smobile = Mobile()
smobile.switch_on()
smobile.set_os('ios')
smobile.switch_on()
            """,
            "Polymorphism": """
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
            """,
            "Abstraction": """
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 10)
circle = Circle(7)

print("Rectangle area:", rectangle.area())
print("Circle area:", circle.area())
            """
        }
        
        self.canvas.create_text(500, 50, text=concept, font=("Helvetica Neue", 20, "bold"), fill="white")
        self.canvas.create_text(500, 100, text=explanations[concept], font=("Helvetica Neue", 14), fill="white", width=600)
        
        self.code_area = scrolledtext.ScrolledText(self, width=70, height=12, wrap=tk.WORD, font=("Courier", 12))
        self.canvas.create_window(500, 250, window=self.code_area)
        self.code_area.insert(tk.END, examples[concept])
        
        self.run_button = ttk.Button(self, text="Run Code", command=self.run_code)
        self.run_button.place(x=500, y=400, anchor="center")
        
        self.output_area = scrolledtext.ScrolledText(self, width=70, height=12, wrap=tk.WORD, font=("Courier", 12))
        self.canvas.create_window(500, 550, window=self.output_area)
        
        back_button = ttk.Button(self, text="Back To Menu", command=self.destroy)
        back_button.place(x=500, y=700, anchor="center")
    
    def run_code(self):
        code = self.code_area.get("1.0", tk.END)
        self.output_area.delete("1.0", tk.END)
        
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()
        
        try:
            exec_globals = {}
            exec(code, exec_globals)
            output = sys.stdout.getvalue()
            self.output_area.insert(tk.END, output)
        except Exception as e:
            self.output_area.insert(tk.END, f"Error: {e}\n")
        finally:
            sys.stdout = stdout_backup
