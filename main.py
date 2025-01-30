import tkinter as tk
from tkinter import scrolledtext

class OOPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OOP & SOLID Educational App")
        self.root.geometry("600x400")
        
        self.label = tk.Label(root, text="Learn OOP with SOLID Principles", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)
        
        # Buttons for each principle
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()
        
        principles = ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism"]
        for principle in principles:
            btn = tk.Button(self.buttons_frame, text=principle, command=lambda p=principle: self.show_example(p))
            btn.pack(side=tk.LEFT, padx=5)
        
        # Display area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
        self.text_area.pack(pady=10)
        
    def show_example(self, principle):
        examples = {
            "Encapsulation": """
Encapsulation: Restricting direct access to object data.

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age  # Private variable
    
    def get_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"

p = Person("Alice", 25)
print(p.get_info())  # Works fine
print(p.__name)  # Error! Private attribute
            """,
            
            "Abstraction": """
Abstraction: Hiding implementation details, exposing only necessary parts.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

d = Dog()
print(d.make_sound())
            """,
            
            "Inheritance": """
Inheritance: One class acquires the properties of another.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

d = Dog("Buddy")
print(d.name, d.speak())
            """,
            
            "Polymorphism": """
Polymorphism: Same method name, different implementations.

class Bird:
    def make_sound(self):
        return "Chirp"

class Dog:
    def make_sound(self):
        return "Bark"

def animal_sound(animal):
    print(animal.make_sound())

b = Bird()
d = Dog()
animal_sound(b)
animal_sound(d)
            """,
        }
        
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, examples[principle])

if __name__ == "__main__":
    root = tk.Tk()
    app = OOPApp(root)
    root.mainloop()
