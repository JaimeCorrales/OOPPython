import tkinter as tk
from tkinter import scrolledtext, messagebox
from ttkthemes import ThemedTk
from tkinter import ttk
from PIL import Image, ImageTk

def ood_window():
    OODApp()

class OODApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("OOD Learning Menu")
        self.geometry("1000x780")
        self.configure(bg="#f4f4f4")

        self.bg_image = Image.open("bgApp.jpg").resize((1000, 780), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.canvas = tk.Canvas(self, width=1000, height=780, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        self.canvas.create_text(500, 50, text="Learn OOD Concepts", font=("Helvetica Neue", 28, "bold"), fill="white")

        options = [
            "SRP - Single Responsibility Principle",
            "OCP - Open-Closed Principle",
            "LSP - Liskov Substitution Principle",
            "ISP - Interface Segregation Principle",
            "DIP - Dependency Inversion Principle"
        ]
        
        button_frame = tk.Frame(self, bg="#f4f4f4")
        button_frame.pack(pady=20)
        
        for index, option in enumerate(options):
            self.create_button(option, lambda opt=option: self.show_concept(opt), 200 + (index * 60))

        tk.Button(self, text="Back", font=("Arial", 14), width=20, bg="#d9534f", fg="white", command=self.destroy).pack(pady=20)

    def create_button(self, text, command, y_pos):
        button = ttk.Button(self, text=text, command=command)
        
        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=("Helvetica Neue", 16),
                        padding=12,
                        width=30,
                        relief="flat",
                        anchor="center",
                        foreground="black")

        style.map("Custom.TButton",
                  background=[("active", "grey"), ("!active", "blue")],
                  foreground=[("active", "black"), ("!active", "black")])

        button.config(style="Custom.TButton")
        self.canvas.create_window(500, y_pos, window=button)

    def show_concept(self, concept):
        ConceptWindow(self, concept)

class ConceptWindow(tk.Toplevel):
    def __init__(self, parent, concept):
        super().__init__(parent)
        self.title(concept)
        self.geometry("1000x780")
        
        self.explanations = {
            "SRP - Single Responsibility Principle":
                "A class should have one and only one reason to change, meaning that a class should have only one job. "
                "By focusing on a single responsibility, it becomes easier to maintain and understand the class, and "
                "it helps avoid making changes that affect multiple parts of the system. This principle advocates for better cohesion and less coupling.",

            "OCP - Open-Closed Principle":
                "Objects or entities should be open for extension but closed for modification. "
                "This means that you should be able to extend the functionality of a class without modifying its existing code. "
                "In practice, you should design your software to allow behavior to be added via extensions or new implementations rather than altering existing code, ensuring the stability of the original codebase.",
                
            "LSP - Liskov Substitution Principle":
                "Subtypes must be substitutable for their base types. In other words, if class B is a subclass of class A, "
                "then objects of class A should be replaceable with objects of class B without affecting the correctness of the program. "
                "This principle ensures that derived classes extend the behavior of a base class without changing the intended functionality or breaking the code.",
                
            "ISP - Interface Segregation Principle":
                "A client should never be forced to implement an interface it doesn’t use or depend on methods it does not need. "
                "This principle encourages small, specific interfaces rather than large, general ones. "
                "It helps avoid bloated interfaces and promotes creating focused interfaces that can be easily implemented by clients that need them. "
                "This leads to cleaner code and reduced dependency between classes.",
                
            "DIP - Dependency Inversion Principle":
                "Abstractions should not depend on details. Details should depend on abstractions. This principle encourages high-level modules to depend on abstractions, not concrete implementations. "
                "By relying on abstract classes or interfaces instead of concrete implementations, you make your code more flexible and easier to extend, test, and maintain. "
                "This also decouples your code, making it easier to swap implementations as long as they adhere to the same abstractions."
        }

        self.good_examples = {
            "SRP - Single Responsibility Principle": """from pathlib import Path
from zipfile import ZipFile

# Split the class into two smaller, more focused classes, each with its own specific concern
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()""",
            "OCP - Open-Closed Principle": """from abc import ABC, abstractmethod
from math import pi


# This class provides the required interface (API) for any shape that you’d like to define.
# This type of inheritance is called interface inheritance.
# This update closes the class to modifications.
# Now you can add new shapes to your class design without the need to modify Shape.
# In every case, you’ll have to implement the required interface, which also makes your classes polymorphic.
class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2""",
            "LSP - Liskov Substitution Principle": """from abc import ABC, abstractmethod


# With this implementation in place, you can use the Shape type interchangeably
# with its Square and Rectangle subtypes when you only care about their common behavior.
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


# This function is polymorphic because it can accept any shape type.
def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)


if __name__ == "__main__":
    get_total_area([Rectangle(10, 5), Square(5)])""",
            "ISP - Interface Segregation Principle": """from abc import ABC, abstractmethod


# Now Printer, Fax, and Scanner are base classes that provide specific interfaces with a single responsibility each.
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

if __name__ == "__main__":
    old_printer = OldPrinter()
    old_printer.print("hello.txt")

    modern_printer = NewPrinter()
    modern_printer.print("hello.txt")
    modern_printer.fax("hello.txt")
    modern_printer.scan("hello.txt")""",
            "DIP - Dependency Inversion Principle": """from abc import ABC, abstractmethod


# Make your classes depend on abstractions rather than on concrete implementations like BackEnd.
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"


class FrontEnd:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


if __name__ == "__main__":
    database = Database()
    front_end = FrontEnd(database)
    front_end.display_data()

    api = API()
    front_end = FrontEnd(api)
    front_end.display_data()"""
        }
        
        self.bad_examples = {
            "SRP - Single Responsibility Principle": """from pathlib import Path
from zipfile import ZipFile

# This class violates the single-responsibility principle because it has two 
# reasons for changing its internal implementation.
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()""",
            "OCP - Open-Closed Principle": """from math import pi

# This violates the OCP principle because we must modify this code
# to add a new shape, rather than being able to extend it.
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def calculate_area(self):
        if self.shape_type == "circle":
            return pi * self.radius**2
        elif self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "square":
            return self.side**2""",
            "LSP - Liskov Substitution Principle": """class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_area(self):
        return self.side * self.side
# The LSP problem occurs here when we subclass Rectangle into Square,
# breaking the Liskov Substitution Principle.""",
            "ISP - Interface Segregation Principle": """class Printer:
    def print(self, document):
        print(f"Printing {document}")

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class MultiFunctionPrinter(Printer):
    def fax(self, document):
        print(f"Faxing {document}")

    def scan(self, document):
        print(f"Scanning {document}")""",
            "DIP - Dependency Inversion Principle": """class Database:
    def get_data(self):
        return "Data from the database"


class API:
    def get_data(self):
        return "Data from the API"


class FrontEnd:
    def display_data(self):
        data = Database().get_data()  # Direct dependency on Database
        print("Display data:", data)

# This violates the DIP principle because the FrontEnd is directly dependent
# on a concrete class (Database), which makes it harder to replace or extend""",
        }

        explanation = self.explanations[concept]
        good_example = self.good_examples[concept]
        bad_example = self.bad_examples[concept]

        frame = tk.Frame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(frame, text=concept, font=("Helvetica Neue", 22, "bold")).pack(pady=10)
        
        tk.Label(frame, text="Explanation:", font=("Helvetica Neue", 14, "bold")).pack(pady=5)
        tk.Label(frame, text=explanation, font=("Helvetica Neue", 12), wraplength=1000).pack(pady=5)
        
        tk.Label(frame, text="Good Example:", font=("Helvetica Neue", 14, "bold")).pack(pady=5)
        scrolled_good_example = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=120, height=18, font=("Courier New", 10))
        scrolled_good_example.insert(tk.END, good_example)
        scrolled_good_example.config(state=tk.DISABLED)
        scrolled_good_example.pack(pady=5)
        
        tk.Label(frame, text="Bad Example:", font=("Helvetica Neue", 14, "bold")).pack(pady=5)
        scrolled_bad_example = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=120, height=18, font=("Courier New", 10))
        scrolled_bad_example.insert(tk.END, bad_example)
        scrolled_bad_example.config(state=tk.DISABLED)
        scrolled_bad_example.pack(pady=5)
