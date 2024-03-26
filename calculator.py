import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

total_expression = ""
current_expression = ""

def create_display_frame(root):
    frame=tk.Frame(root,height=221,bg=LIGHT_GRAY)
    frame.pack(expand=True,fill="both")
    return frame

def create_display_label(display_frame):
    global label
    global total_label

    total_label=tk.Label(display_frame,text=total_expression,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
    total_label.pack(expand=True,fill="both")

    label=tk.Label(display_frame,text=current_expression,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
    label.pack(expand=True,fill="both")

    return total_label,label


def add_to_expression(value):
    global current_expression
    current_expression += str(value)
    update_label()

def create_digit_buttons(buttons_frame):
    digits = {
        7: (1, 1), 8: (1, 2), 9: (1, 3),
        4: (2, 1), 5: (2, 2), 6: (2, 3),
        1: (3, 1), 2: (3, 2), 3: (3, 3),
        0: (4, 2), '.': (4, 1)
    }
    for digit, grid_value in digits.items():
        global button
        button = tk.Button(buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                           borderwidth=0, command=lambda x=digit: add_to_expression(x))
        button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

def append_operator(operator):
    global current_expression, total_expression
    current_expression += operator
    total_expression += current_expression
    current_expression = ""
    update_total_label()
    update_label()

def create_operator_buttons(buttons_frame):
    operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
    i = 0
    for operator, symbol in operations.items():
        button = tk.Button(buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda x=operator: append_operator(x))
        button.grid(row=i, column=4, sticky=tk.NSEW)
        i += 1
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

def clear():
    global current_expression, total_expression
    current_expression = ""
    total_expression = ""
    update_label()
    update_total_label()

def create_clear_button(buttons_frame):
    button = tk.Button(buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                       borderwidth=0, command=clear)
    button.grid(row=0, column=1, sticky=tk.NSEW)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

def evaluate():
    global current_expression, total_expression
    total_expression += current_expression
    update_total_label()
    try:
        current_expression = str(eval(total_expression))
        total_expression = ""
    except Exception as e:
        current_expression = "Error"
    finally:
        update_label()

def create_equals_button(buttons_frame):
    button = tk.Button(buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                       borderwidth=0, command=evaluate)
    button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

def create_square_button(buttons_frame):
    button = tk.Button(buttons_frame, text="(", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                       borderwidth=0, command=lambda : append_operator('('))
    button.grid(row=0, column=2, sticky=tk.NSEW)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

def create_sqrt_button(buttons_frame):
    button = tk.Button(buttons_frame, text=")", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                       borderwidth=0, command=lambda : append_operator(')'))
    button.grid(row=0, column=3, sticky=tk.NSEW)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

def update_total_label():
    global total_expression
    expression = total_expression
    operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
    for operator, symbol in operations.items():
        expression = expression.replace(operator, f' {symbol} ')
    total_label.config(text=expression)

def update_label():
    label.config(text=current_expression[:11])

def on_enter(event):
    event.widget.config(bg="lightblue", fg="black")

def on_leave(event):
    if event.widget["text"] == "=":  # Check if the widget is the equals button
        event.widget.config(bg=LIGHT_BLUE, fg=LABEL_COLOR)
    else:
        event.widget.config(bg=WHITE, fg=LABEL_COLOR)

def key_press(event):
    """Function to handle keyboard key press events."""
    key = event.char
    if key.isdigit() or key == '.':
        add_to_expression(key)
    elif key in {'+', '-', '*', '/'}:
        append_operator(key)
    elif key == '=' or key == '\r':
        evaluate()
    elif key == '\x08':
        clear()

def run():
    root=tk.Tk()
    root.geometry("375x667")
    root.minsize(200,300)
    root.iconphoto(False, tk.PhotoImage(file="D:\GIT\Calculator-Using-Python\icons8-calculator-48.png"))
    root.title("Calculator GUI")

    display_frame=create_display_frame(root)
    total_label,label=create_display_label(display_frame)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(expand=True, fill="both")

    buttons_frame.rowconfigure(0, weight=1)
    for x in range(1, 5):
        buttons_frame.rowconfigure(x, weight=1)
        buttons_frame.columnconfigure(x, weight=1)

    # Bind keyboard events
    root.bind('<Key>', key_press)

    create_digit_buttons(buttons_frame)
    create_operator_buttons(buttons_frame)
    create_clear_button(buttons_frame)
    create_equals_button(buttons_frame)
    create_square_button(buttons_frame)
    create_sqrt_button(buttons_frame)

    root.mainloop()

if __name__=="__main__":
    run()