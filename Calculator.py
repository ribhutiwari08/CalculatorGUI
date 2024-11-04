import tkinter as tk
from tkinter import font


window = tk.Tk()
window.title("Ribhu Calculator")
window.geometry("400x600")
window.configure(bg="#333333")  


expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception as e:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")


equation = tk.StringVar()
entry_field = tk.Entry(window, textvariable=equation, font=('Helvetica', 24), fg="#ffffff", bg="#666666",
                       justify='right', bd=15, relief="flat", insertwidth=4)
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=20)


button_font = font.Font(family='Helvetica', size=18, weight='bold')
button_bg = "#4d4d4d"
button_fg = "#ffffff"
highlight_color = "#ff9500"


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, col) in buttons:
   
    if text == '=':
        button = tk.Button(window, text=text, font=button_font, fg="#ffffff", bg=highlight_color, height=2, width=5,
                           command=equalpress)
    else:
        button = tk.Button(window, text=text, font=button_font, fg=button_fg, bg=button_bg, height=2, width=5,
                           command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5)


clear_button = tk.Button(window, text='C', font=button_font, fg="#ffffff", bg="#ff3b30", height=2, width=5,
                         command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


quit_button = tk.Button(window, text='Quit', font=button_font, fg="#ffffff", bg="#007aff", height=2, width=5,
                        command=window.quit)
quit_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)


window.mainloop()
