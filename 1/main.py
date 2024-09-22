import tkinter as tk
from tkinter import messagebox

# Функция для обработки нажатия на кнопку
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Ошибка", "Неверное выражение")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор")

# Настройка общего стиля окна
root.configure(bg="#1e1e1e")
root.geometry("400x500")
root.resizable(False, False)

# Создание поля для ввода выражений
entry = tk.Entry(root, font=("Arial", 24), bg="#292929", fg="white", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Список кнопок
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Функция для создания кнопки с настройками стиля
def create_button(text):
    return tk.Button(
        root, text=text, font=("Arial", 18), fg="white", bg="#3b3b3b",
        width=5, height=2, bd=0, activebackground="#555555", activeforeground="white"
    )

# Создание и размещение кнопок
row = 1
col = 0
for button in buttons:
    btn = create_button(button)
    btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    btn.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Настройка гибкости рядов и колонок
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Запуск основного цикла приложения
root.mainloop()
