import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog


root = tk.Tk()
root.title("Шишкин Ярослав Александрович")  
root.geometry("500x400")


notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)


calc_frame = tk.Frame(notebook)
notebook.add(calc_frame, text="Калькулятор")


tk.Label(calc_frame, text="Число 1:").pack(pady=5)
num1_entry = tk.Entry(calc_frame)
num1_entry.pack(pady=5)

tk.Label(calc_frame, text="Число 2:").pack(pady=5)
num2_entry = tk.Entry(calc_frame)
num2_entry.pack(pady=5)


tk.Label(calc_frame, text="Операция:").pack(pady=5)
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(calc_frame, operation_var, *operations)
operation_menu.pack(pady=5)


def calculate():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        op = operation_var.get()
        
        if op == "+": result = a + b
        elif op == "-": result = a - b
        elif op == "*": result = a * b
        elif op == "/": 
            if b == 0:
                messagebox.showerror("Ошибка", "Нельзя делить на ноль!")
                return
            result = a / b
        
        messagebox.showinfo("Результат", f"Ответ: {result}")
    except:
        messagebox.showerror("Ошибка", "Проверьте введенные числа")

tk.Button(calc_frame, text="Вычислить", command=calculate).pack(pady=10)


check_frame = tk.Frame(notebook)
notebook.add(check_frame, text="Чекбоксы")


var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

tk.Checkbutton(check_frame, text="Первый", variable=var1).pack(pady=10)
tk.Checkbutton(check_frame, text="Второй", variable=var2).pack(pady=10)
tk.Checkbutton(check_frame, text="Третий", variable=var3).pack(pady=10)


def show_choice():
    choices = []
    if var1.get(): choices.append("первый")
    if var2.get(): choices.append("второй")
    if var3.get(): choices.append("третий")
    
    if choices:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(choices)}")
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

tk.Button(check_frame, text="Показать выбор", command=show_choice).pack(pady=10)


text_frame = tk.Frame(notebook)
notebook.add(text_frame, text="Текст")


text_area = tk.Text(text_frame, height=15)
text_area.pack(fill='both', expand=True, padx=10, pady=10)


def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())

tk.Button(text_frame, text="Загрузить из файла", command=load_file).pack(pady=5)


root.mainloop()
