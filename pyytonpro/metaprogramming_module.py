import tkinter as tk
from tkinter import scrolledtext, ttk
from PIL import Image, ImageTk

def metaprogramming_window():
    MetaprogrammingApp()

class MetaprogrammingApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Metaprogramming Learning Section")
        self.geometry("1000x780")
        
        canvas = tk.Canvas(self, width=1000, height=780, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        background_image = Image.open("bgApp.jpg")
        background_image = background_image.resize((1000, 780), Image.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)

        canvas.create_image(0, 0, image=background_photo, anchor="nw")
        self.background_photo = background_photo

        canvas.create_text(500, 80, text="Metaprogramming: Decorators, type() & Metaclasses", font=("Helvetica Neue", 24, "bold"), fill="white")

        content_text = """
        In Python, metaprogramming refers to writing code that manipulates code itself.
        Let's dive into three important metaprogramming concepts: Metaclasses, Decorators, and the type() function.

        1. Metaclasses in Python:
        - A metaclass is a class of a class. In Python, classes are instances of metaclasses.
        - You can define a metaclass by inheriting from the 'type' class.
        - Metaclasses control the behavior of classes during their creation.

        Example of a simple metaclass:
        ```
        class MyMeta(type):
            def __new__(cls, name, bases, dct):
                dct['created_by'] = 'Metaclass'
                return super().__new__(cls, name, bases, dct)
        
        class MyClass(metaclass=MyMeta):
            pass
        
        obj = MyClass()
        print(obj.created_by)  # Output: Metaclass
        ```

        2. Decorators in Python:
        - A decorator is a function that wraps another function or method to modify its behavior.
        - Decorators are widely used in Python for various purposes such as logging, memoization, and access control.

        Example of a decorator:
        ```
        def my_decorator(func):
            def wrapper():
                print("Before function execution")
                func()
                print("After function execution")
            return wrapper
        
        @my_decorator
        def say_hello():
            print("Hello!")
        
        say_hello()  # Output: Before function execution, Hello!, After function execution
        ```

        3. The type() Function:
        - The type() function is used to return the type of an object.
        - It can also be used to dynamically create classes in Python.

        Example of using type():
        ```
        x = 10
        print(type(x))  # Output: <class 'int'>
        
        # Dynamically creating a class using type()
        MyClass = type('MyClass', (object,), {'greet': lambda self: 'Hello, world!'})
        obj = MyClass()
        print(obj.greet())  # Output: Hello, world!
        ```
        """
        
        text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Helvetica Neue", 12), height=15, width=90)
        text_box.insert(tk.END, content_text)
        text_box.config(state=tk.DISABLED)
        text_box.place(x=50, y=150)

        self.create_button("Back to Main Window", self.destroy, "#9C27B0", "#7B1FA2", 700)
        
    def create_button(self, text, command, normal_bg, hover_bg, y_pos):
        button = ttk.Button(self, text=text, command=command)

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

        canvas = self.winfo_children()[0]
        canvas.create_window(500, y_pos, window=button)