import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

class QuizWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("OOP & OOD Quiz")
        self.geometry("800x600")
        self.configure(bg="#f4f4f4")

        self.bg_image = Image.open("bgApp.jpg").resize((800, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.background_label = tk.Label(self, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.questions = [
            {"question": "Which OOP pillar allows a class to inherit from another?", "options": ["Encapsulation", "Inheritance", "Polymorphism"], "answer": "Inheritance"},
            {"question": "Which OOP concept restricts direct access to an object's data?", "options": ["Inheritance", "Encapsulation", "Overloading"], "answer": "Encapsulation"},
            {"question": "What does method overloading allow?", "options": ["Multiple methods with the same name but different parameters", "Using a method from a superclass", "Accessing private variables"], "answer": "Multiple methods with the same name but different parameters"},
            {"question": "Which OOP pillar allows a class to inherit from multiple base classes?", "options": ["Method Overloading", "Multiple Inheritance", "Encapsulation"], "answer": "Multiple Inheritance"},
            {"question": "Does this code follow Encapsulation?\n\nclass A:\n    def __init__(self):\n        self.__private_var = 42", "options": ["Yes", "No"], "answer": "Yes"},
            {"question": "What keyword is used to inherit from a class in Python?", "options": ["extends", "inherits", "class SuperClass"], "answer": "class SuperClass"},
            {"question": "Which of the following best describes inheritance?", "options": ["Hiding data from users", "Sharing properties and behaviors with derived classes", "Overriding methods only"], "answer": "Sharing properties and behaviors with derived classes"},
            {"question": "What does 'super()' do in Python?", "options": ["Calls a method from the superclass", "Creates a new object", "Accesses private variables"], "answer": "Calls a method from the superclass"},
            {"question": "Does this code follow Multiple Inheritance?\n\nclass A:\n    def method(self):\n        return 'A method'\n\nclass B:\n    def method(self):\n        return 'B method'\n\nclass C(A, B):\n    pass", "options": ["Yes", "No"], "answer": "Yes"},
            {"question": "What does Encapsulation achieve?", "options": ["Hiding implementation details", "Allowing a class to inherit from another", "Using the same method multiple times"], "answer": "Hiding implementation details"},

            {"question": "What does the Single Responsibility Principle (SRP) state?", "options": ["A class should have one reason to change", "A class should inherit from multiple classes", "A class should hide its data"], "answer": "A class should have one reason to change"},
            {"question": "Which design pattern allows a class to be responsible for the creation of its objects?", "options": ["Factory Pattern", "Observer Pattern", "Decorator Pattern"], "answer": "Factory Pattern"},
            {"question": "What is the purpose of abstraction in OOD?", "options": ["To hide the implementation details from the user", "To reduce the size of the code", "To create more complex objects"], "answer": "To hide the implementation details from the user"},
            {"question": "Which principle ensures that subclasses can be used interchangeably with their parent class?", "options": ["Liskov Substitution Principle", "Dependency Inversion Principle", "Open/Closed Principle"], "answer": "Liskov Substitution Principle"},
            {"question": "Which OOD principle encourages the use of interfaces or abstract classes to define behavior?", "options": ["Abstraction", "Encapsulation", "Inheritance"], "answer": "Abstraction"},
            {"question": "Which design pattern involves a method that wraps another method?", "options": ["Decorator Pattern", "Observer Pattern", "Singleton Pattern"], "answer": "Decorator Pattern"},
            {"question": "What does the Open/Closed Principle state?", "options": ["Software entities should be open for extension but closed for modification", "Classes should be able to inherit from multiple classes", "Encapsulation should be applied in every class"], "answer": "Software entities should be open for extension but closed for modification"},
            {"question": "What does the Dependency Inversion Principle aim to achieve?", "options": ["High-level modules should not depend on low-level modules", "Software should be designed in such a way that everything is inherited", "Inheritance should be avoided"], "answer": "High-level modules should not depend on low-level modules"},
            {"question": "Which design pattern is used to allow an object to take on multiple forms?", "options": ["Factory Pattern", "Proxy Pattern", "Strategy Pattern"], "answer": "Strategy Pattern"},
            {"question": "What does the Interface Segregation Principle encourage?", "options": ["Clients should not be forced to depend on interfaces they do not use", "Interfaces should be publicly accessible", "Interfaces should have all methods defined"], "answer": "Clients should not be forced to depend on interfaces they do not use"},
            {"question": "What is the primary purpose of the Singleton Pattern?", "options": ["To allow only one instance of a class", "To create multiple instances of a class", "To define a method that can be called without an instance"], "answer": "To allow only one instance of a class"},
            {"question": "Which design pattern allows objects to communicate with each other without knowing each other's details?", "options": ["Observer Pattern", "Mediator Pattern", "Strategy Pattern"], "answer": "Mediator Pattern"},
            {"question": "What is the purpose of the Adapter Pattern?", "options": ["To allow incompatible interfaces to work together", "To ensure that objects are interchangeable", "To provide a flexible and reusable implementation"], "answer": "To allow incompatible interfaces to work together"},
            {"question": "What does the Composite Pattern allow?", "options": ["To treat individual objects and compositions of objects uniformly", "To handle the behavior of objects in isolation", "To define abstract behaviors for subclasses"], "answer": "To treat individual objects and compositions of objects uniformly"}
        ]
        
        self.selected_questions = random.sample(self.questions, 10)
        
        self.score = 0
        self.current_question = 0
        self.display_question()

    def display_question(self):
        for widget in self.winfo_children():
            widget.destroy()

        if self.current_question < len(self.selected_questions):
            question_data = self.selected_questions[self.current_question]
            
            question_label = tk.Label(self, text=question_data["question"], font=("Helvetica Neue", 14), wraplength=650, bg="#f4f4f4", fg="black")
            question_label.pack(pady=20)

            self.selected_answer = tk.StringVar()


            # RADIO TO CHANGE#
            for option in question_data["options"]:
                rb = tk.Radiobutton(self, text=option, variable=self.selected_answer, value=option, font=("Helvetica Neue", 12), bg="#f4f4f4", fg="black")
                rb.pack(anchor="w", padx=20, pady=5)

            question_number_label = tk.Label(self, text=f"Question {self.current_question + 1} of 10", font=("Helvetica Neue", 14), bg="#f4f4f4", fg="black")
            question_number_label.pack(pady=10)

            style = ttk.Style()
            style.configure("Custom.TButton",
                            font=("Helvetica Neue", 12),
                            padding=12,
                            relief="flat",
                            foreground="black")
            style.map("Custom.TButton", background=[("active", "grey"), ("!active", "blue")])

            next_button = ttk.Button(self, text="Next", command=self.check_answer, style="Custom.TButton")
            next_button.pack(pady=20)

        else:
            self.show_result()

    def check_answer(self):
        if self.selected_answer.get() == self.selected_questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.display_question()

    def show_result(self):
        for widget in self.winfo_children():
            widget.destroy()

        result_text = "Congratulations! You passed the OOP & OOD Quiz!" if self.score >= 6 else "You didn't pass. Try again!"

        score_label = tk.Label(self, text=f"Your Score: {self.score}/10", font=("Helvetica Neue", 16, "bold"), bg="#f4f4f4", fg="black")
        score_label.pack(pady=20)

        result_label = tk.Label(self, text=result_text, font=("Helvetica Neue", 14), bg="#f4f4f4", fg="black")
        result_label.pack(pady=10)

        close_button = ttk.Button(self, text="Close", command=self.destroy, style="Custom.TButton")
        close_button.pack(pady=20)