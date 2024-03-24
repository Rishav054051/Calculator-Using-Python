import customtkinter as ct

ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("dark")

root=ct.CTk()
#ct.set_widget_scaling(1)  # widget dimensions and text size
#ct.set_window_scaling(1)  # window geometry dimensions

root.geometry("400x600")


f1=ct.CTkFrame(root,width=400,height=80,fg_color="black")
f1.pack(expand=True,fill="both",pady=5)
f2=ct.CTkFrame(root,width=400,height=800,fg_color="black")
f2.pack(expand=True,fill="both")


# Define buttons for digits (0-9)
for i in range(10):
    if i == 0:
        button = ct.CTkButton(f2, text="0", width=5, height=2, font=('Arial', 14))
        button.grid(row=4, column=1, padx=5, pady=5)
    else:
        button = ct.CTkButton(f2, text=str(i), width=5, height=2, font=('Arial', 14))
        button.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

for i in range(3):
    f2.grid_rowconfigure(i, weight=1)
    f2.grid_columnconfigure(i, weight=1)

root.mainloop()
