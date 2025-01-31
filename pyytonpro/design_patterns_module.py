import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type!")

class Subject:
    def __init__(self):
        self._observers = []
        
    def attach(self, observer):
        self._observers.append(observer)
        
    def detach(self, observer):
        self._observers.remove(observer)
        
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name
        
    def update(self, message):
        print(f"{self._name} received message: {message}")

class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

def design_patterns_window():
    window = tk.Toplevel()
    window.title("Design Patterns")

    canvas = tk.Canvas(window, width=1000, height=780, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    background_image = Image.open("bgApp.jpg")
    background_image = background_image.resize((1000, 780), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    canvas.create_image(0, 0, image=background_photo, anchor="nw")
    window.background_photo = background_photo

    canvas.create_text(500, 80, text="Design Patterns: Singleton, Factory, Observer & Decorator", font=("Helvetica Neue", 24, "bold"), fill="white")

    content_text = """
    Singleton Pattern:
    - Ensures a class has only one instance and provides a global point of access to it.
    - Example: Only one instance of a logging service is needed.

    Factory Pattern:
    - Provides an interface for creating objects in a super class, but allows subclasses to alter the type of created objects.
    - Example: AnimalFactory creates different types of animals like Dog and Cat.

    Observer Pattern:
    - Defines a one-to-many dependency relationship where a change in one object (subject) notifies all dependent objects (observers).
    - Example: StockMarket notifying investors when prices change.

    Decorator Pattern:
    - Allows behavior to be added to an individual object dynamically without affecting the behavior of other objects from the same class.
    - Example: Adding milk or sugar to a basic coffee.
    """
    
    text_box = tk.Text(window, wrap=tk.WORD, font=("Helvetica Neue", 12), height=15, width=90)
    text_box.insert(tk.END, content_text)
    text_box.config(state=tk.DISABLED)
    canvas.create_window(500, 250, window=text_box)

    def create_button(text, command, normal_bg, hover_bg, y_pos):
        button = ttk.Button(window, text=text, command=command)
        
        style = ttk.Style()
        
        style.configure("Custom.TButton",
                        font=("Helvetica Neue", 16),
                        padding=12,
                        width=19,
                        relief="flat",
                        anchor="center",
                        foreground="black")
        
        style.map("Custom.TButton",
                  background=[("active", "grey"), ("!active", "blue")],
                  foreground=[("active", "black"), ("!active", "black")])

        button.config(style="Custom.TButton")

        canvas.create_window(500, y_pos, window=button)

    create_button("Singleton Pattern Example", lambda: show_singleton_example(window), "#4CAF50", "#388E3C", 500)
    create_button("Factory Pattern Example", lambda: show_factory_example(window), "#007BFF", "#005BB5", 570)
    create_button("Observer Pattern Example", lambda: show_observer_example(window), "#FF9800", "#F57C00", 640)
    create_button("Decorator Pattern Example", lambda: show_decorator_example(window), "#9C27B0", "#7B1FA2", 710)

    window.mainloop()

def show_singleton_example(window):
    singleton1 = Singleton()
    singleton2 = Singleton()
    result = "Same" if singleton1 is singleton2 else "Different"
    result_label = tk.Label(window, text=f"Singleton Pattern: {result} instances", font=("Helvetica", 12))
    result_label.pack()

def show_factory_example(window):
    animal1 = AnimalFactory.create_animal("dog")
    animal2 = AnimalFactory.create_animal("cat")
    result_label = tk.Label(window, text=f"Factory Pattern: Dog says '{animal1.speak()}', Cat says '{animal2.speak()}'", font=("Helvetica", 12))
    result_label.pack()

def show_observer_example(window):
    subject = Subject()
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")
    subject.attach(observer1)
    subject.attach(observer2)
    subject.notify("New update available!")
    observer_label = tk.Label(window, text="Observer Pattern: Both observers were notified.", font=("Helvetica", 12))
    observer_label.pack()

def show_decorator_example(window):
    basic_coffee = Coffee()
    milk_coffee = MilkDecorator(basic_coffee)
    sugar_milk_coffee = SugarDecorator(milk_coffee)
    result_label = tk.Label(window, text=f"Decorator Pattern: Basic coffee cost: ${basic_coffee.cost()}. Milk coffee cost: ${milk_coffee.cost()}. Sugar + Milk coffee cost: ${sugar_milk_coffee.cost()}.", font=("Helvetica", 12))
    result_label.pack()
