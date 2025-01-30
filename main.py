import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from PIL import Image, ImageTk

class OOPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OOP & SOLID Educational App")
        self.root.geometry("750x550")
        self.root.configure(bg="#e0f7fa")
        
        # Load icon
        self.icon_img = Image.open("icon.png")
        self.icon_img = self.icon_img.resize((50, 50))
        self.icon = ImageTk.PhotoImage(self.icon_img)
        self.icon_label = tk.Label(root, image=self.icon, bg="#e0f7fa")
        self.icon_label.pack(pady=5)
        
        # Title Label
        self.label = tk.Label(root, text="Learn OOP with SOLID Principles", font=("Arial", 16, "bold"), bg="#e0f7fa", fg="#004d40")
        self.label.pack(pady=10)
        
        # Frame for Buttons
        self.buttons_frame = tk.Frame(root, bg="#e0f7fa")
        self.buttons_frame.pack(pady=10)
        
        principles = ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism"]
        for principle in principles:
            btn = ttk.Button(self.buttons_frame, text=principle, command=lambda p=principle: self.show_example(p))
            btn.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Display area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Courier", 10), bg="#ffffff", fg="#000000", insertbackground="black", borderwidth=2, relief="solid")
        self.text_area.pack(pady=10, padx=10)
        
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
