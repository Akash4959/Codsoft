import tkinter as tk


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")


input_text = tk.StringVar()


input_frame = tk.Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) 


expression = ""


def press_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)


def clear_input():
    global expression
    expression = ""
    input_text.set("")


def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))  
        input_text.set(result)
        expression = result 
    except:
        input_text.set("Error")
        expression = ""

# Create the buttons
button_frame = tk.Frame(root, width=400, height=450, bg="grey")
button_frame.pack()

# First row of buttons
clear = tk.Button(button_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=clear_input).grid(row=0, column=0, columnspan=3)
divide = tk.Button(button_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: press_button("/")).grid(row=0, column=3)

# Second row of buttons
seven = tk.Button(button_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(7)).grid(row=1, column=0)
eight = tk.Button(button_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(8)).grid(row=1, column=1)
nine = tk.Button(button_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(9)).grid(row=1, column=2)
multiply = tk.Button(button_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: press_button("*")).grid(row=1, column=3)

# Third row of buttons
four = tk.Button(button_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(4)).grid(row=2, column=0)
five = tk.Button(button_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(5)).grid(row=2, column=1)
six = tk.Button(button_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(6)).grid(row=2, column=2)
minus = tk.Button(button_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: press_button("-")).grid(row=2, column=3)

# Fourth row of buttons
one = tk.Button(button_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(1)).grid(row=3, column=0)
two = tk.Button(button_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(2)).grid(row=3, column=1)
three = tk.Button(button_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(3)).grid(row=3, column=2)
plus = tk.Button(button_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: press_button("+")).grid(row=3, column=3)

# Fifth row of buttons
zero = tk.Button(button_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(0)).grid(row=4, column=0, columnspan=2)
decimal = tk.Button(button_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press_button(".")).grid(row=4, column=2)
equals = tk.Button(button_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=evaluate_expression).grid(row=4, column=3)

# Start the GUI event loop
root.mainloop()
