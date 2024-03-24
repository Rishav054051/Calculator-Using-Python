import customtkinter as ct

ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("dark")

root=ct.CTk()
#ct.set_widget_scaling(1)  # widget dimensions and text size
#ct.set_window_scaling(1)  # window geometry dimensions

root.geometry("400x600")


f1=ct.CTkFrame(root,width=400,height=80,fg_color="black")
f1.pack(fill="both",pady=5)
f2=ct.CTkFrame(root,width=400,height=800,fg_color="black")
f2.pack(expand=True,fill="both")


# Define buttons for operators and additional functionalities
buttons = [
    ("C", 0, 0), ("⌫", 0, 1), ("%", 0, 2), ("/", 0, 3),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("X", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
    ("e", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3)
]

# Create buttons
for text, row, column in buttons:
    if (row == 0 and (column >=0 and column < 4)):
        button = ct.CTkButton(f2, text=text, width=20, height=20,fg_color="black",text_color="orange", font=('Arial', 30))
        button.grid(row=row, column=column, padx=5, pady=10)
    elif ((row>=1 and row<5) and (column==3)):
        button = ct.CTkButton(f2, text=text, width=20, height=20,fg_color="black",text_color="orange", font=('Arial', 30))
        button.grid(row=row, column=column, padx=5, pady=10)
    else:
        button = ct.CTkButton(f2, text=text, width=20, height=20,fg_color="black", font=('Arial', 30))
        button.grid(row=row, column=column, padx=5, pady=10)

for i in range(4):
    f2.grid_rowconfigure(i+1, weight=1)
    f2.grid_columnconfigure(i, weight=1)

root.mainloop()
