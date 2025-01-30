import tkinter as tk
import oop_module
import ood_module

def open_oop():
    oop_module.oop_window()

def open_ood():
    ood_module.ood_window()

# Main window
main_window = tk.Tk()
main_window.title("Educational Platform - OOP & OOD")

tk.Label(main_window, text="Choose an Option", font=("Arial", 20)).pack()

tk.Button(main_window, text="OOP", font=("Arial", 14), command=open_oop).pack(pady=10)
tk.Button(main_window, text="OOD", font=("Arial", 14), command=open_ood).pack(pady=10)

main_window.mainloop()