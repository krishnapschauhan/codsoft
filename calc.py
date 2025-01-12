import tkinter as tk

def button_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

for i, button in enumerate(buttons):
    action = lambda value=button: button_click(value)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), command=action)\
        .grid(row=(i // 4) + 1, column=i % 4)

root.mainloop()
