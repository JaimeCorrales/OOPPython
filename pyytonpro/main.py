import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import oop_module
import ood_module
from QuizWindow import QuizWindow
import metaprogramming_module
import design_patterns_module

def open_oop():
    oop_module.oop_window()

def open_ood():
    ood_module.ood_window()

def open_metaprogramming():
    metaprogramming_module.metaprogramming_window()

def open_design_patterns():
    design_patterns_module.design_patterns_window()

def open_quiz():
    QuizWindow(main_window)

main_window = ThemedTk()
main_window.set_theme("adapta")
main_window.title("Educational Platform - OOP, OOD, Metaprogramming & Design Patterns")
main_window.geometry("800x800")

background_image = Image.open("bgApp.jpg")
background_image = background_image.resize((800, 800), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(main_window, width=800, height=800, highlightthickness=0)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=background_photo, anchor="nw")

canvas.create_text(400, 80, text="Choose an Option", font=("Helvetica Neue", 24, "bold"), fill="white")

def create_button(text, command, normal_bg, hover_bg, y_pos):
    button = ttk.Button(main_window, text=text, command=command)
    
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

    canvas.create_window(400, y_pos, window=button)

create_button("OOP", open_oop, "#4CAF50", "#388E3C", 200)
create_button("OOD", open_ood, "#007BFF", "#005BB5", 270)
create_button("METAPROGRAMMING", open_metaprogramming, "#FF9800", "#F57C00", 340)
create_button("DESIGN PATTERNS", open_design_patterns, "#9C27B0", "#7B1FA2", 410)
create_button("QUIZ", open_quiz, "#FF5722", "#D84315", 480)

main_window.mainloop()
