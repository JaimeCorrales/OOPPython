import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
import io
import random

def oop_window():
    OOPApp()

class OOPApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("OOP Learning Menu")
        self.geometry("600x500")
        self.configure(bg="#f4f4f4")
        
        tk.Label(self, text="Learn OOP Concepts", font=("Arial", 18, "bold"), bg="#f4f4f4").pack(pady=20)
        
        options = ["Inheritance", "Encapsulation", "Method Overloading", "Multiple Inheritance"]
        
        button_frame = tk.Frame(self, bg="#f4f4f4")
        button_frame.pack(pady=20)
        
        for option in options:
            tk.Button(button_frame, text=option, font=("Arial", 14), width=25, bg="#4CAF50", fg="white", 
                      command=lambda opt=option: self.show_concept(opt)).pack(pady=10)
        
        tk.Button(self, text="Take OOP Quiz", font=("Arial", 14), width=25, bg="#007BFF", fg="white", command=self.start_quiz).pack(pady=10)
        
        tk.Button(self, text="Back", font=("Arial", 14), width=20, bg="#d9534f", fg="white", command=self.destroy).pack(pady=20)
    
    def show_concept(self, concept):
        ConceptWindow(self, concept)
    
    def start_quiz(self):
        QuizWindow(self)

class QuizWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("OOP Quiz")
        self.geometry("600x500")
        self.configure(bg="#f4f4f4")
        
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
            {"question": "What does Encapsulation achieve?", "options": ["Hiding implementation details", "Allowing a class to inherit from another", "Using the same method multiple times"], "answer": "Hiding implementation details"}
        ]
        
        random.shuffle(self.questions)
        self.score = 0
        self.current_question = 0
        self.display_question()
    
    def display_question(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        if self.current_question < 10:
            question_data = self.questions[self.current_question]
            tk.Label(self, text=question_data["question"], font=("Arial", 14), wraplength=550, bg="#f4f4f4").pack(pady=10)
            
            self.selected_answer = tk.StringVar()
            for option in question_data["options"]:
                tk.Radiobutton(self, text=option, variable=self.selected_answer, value=option, font=("Arial", 12), bg="#f4f4f4").pack(anchor="w")
            
            tk.Button(self, text="Next", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.check_answer).pack(pady=20)
        else:
            self.show_result()
    
    def check_answer(self):
        if self.selected_answer.get() == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.display_question()
    
    def show_result(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        result_text = "Congratulations! You passed the OOP Quiz!" if self.score >= 6 else "You didn't pass. Try again!"
        
        tk.Label(self, text=f"Your Score: {self.score}/10", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=20)
        tk.Label(self, text=result_text, font=("Arial", 14), bg="#f4f4f4").pack(pady=10)
        
        tk.Button(self, text="Close", font=("Arial", 12), bg="#d9534f", fg="white", command=self.destroy).pack(pady=20)

class ConceptWindow(tk.Toplevel):
    def __init__(self, parent, concept):
        super().__init__(parent)
        self.title(concept)
        self.geometry("600x550")
        
        explanations = {
            "Inheritance": "Inheritance allows one class to acquire the properties and methods of another.",
            "Encapsulation": "Encapsulation restricts direct access to some of an object's components.",
            "Method Overloading": "Method overloading allows multiple methods with the same name but different parameters.",
            "Multiple Inheritance": "Multiple inheritance allows a class to inherit from more than one base class."
        }
        
        examples = {
            "Inheritance": "class User:\n    name = \"\"\n\n    def __init__(self, name):\n        self.name = name\n\n    def printName(self):\n        print(\"Name  = \" + self.name)\n\nclass Programmer(User):\n    def __init__(self, name):\n        self.name = name\n\n    def doPython(self):\n        print(\"Programming Python\")\n\nbrian = User(\"brian\")\nbrian.printName()\n\ndiana = Programmer(\"Diana\")\ndiana.printName()\ndiana.doPython()",
            
            "Encapsulation": "class Mobile:\n\n    __os = 'andriod'\n    __name = \"\"\n\n    def __init__(self):\n        self.__os = 'andriod'\n        self.__name = \"Supercar\"\n\n    def switch_on(self):\n        print('Mobile Os is ' + str(self.__os))\n\n    def set_os(self, os):\n        self.__os = os\n\nsmobile = Mobile()\nsmobile.switch_on()\nsmobile.set_os('ios')\nsmobile.switch_on()\n\nprint('-'*100)",
            
            "Method Overloading": "class Mobile:\n\n    def get_brand(self, brand=None):\n\n        if brand is not None:\n            print(brand)\n        else:\n            print('Generic ')\n\n# Create instance\nobj = Mobile()\n\n# Call the method\nobj.get_brand()\n\n# Call the method with a parameter\nobj.get_brand('Samsung')",
            
            "Multiple Inheritance": "class A:\n    def method(self):\n        return 'A method'\n\nclass B:\n    def method(self):\n        return 'B method'\n\nclass C(A, B):\n    pass\n\nc = C()\nprint(c.method())  # Calls method from class A first"
        }
        
        tk.Label(self, text=concept, font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text=explanations[concept], wraplength=500, font=("Arial", 12)).pack(pady=5)
        
        self.code_area = scrolledtext.ScrolledText(self, width=70, height=10)
        self.code_area.pack(pady=10)
        self.code_area.insert(tk.END, examples[concept])
        
        tk.Button(self, text="Run Code", command=self.run_code).pack(pady=5)
        
        self.output_area = scrolledtext.ScrolledText(self, width=70, height=10)
        self.output_area.pack(pady=10)
        
        tk.Button(self, text="Back to Menu", command=self.destroy).pack(pady=10)
    
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


