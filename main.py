from tkinter import *
from tkinter import messagebox
import generate_the_password

root = Tk()
root.title("Password Generator")
root.geometry("310x350+575+200")
root.resizable(False, False)
#make the plus and minus function
chart_n = 0
use_b = None
number_of_passwords = 0
with open("passwords.txt", "w") as f:
    f.write("")
#make the generate function
def generate_pass():
    global chart_n
    global use_b
    global number_of_passwords
    if chart_n == 0:
        use_b = True
        value = chart_n_entry.get()
    else:
        use_b = False

    if chart_n and chart_n_entry.get() == 0:
        messagebox.showerror("Error", "Please enter a chart number")
    else:
        if use_b == False:
            if chart_n == 0 or chart_n == None:
                messagebox.showerror("Error", "Please enter a chart number")
            elif chart_n > 0:
                password = generate_the_password.generate_random_string(chart_n)
                messagebox.showinfo("Password", password)
                #the password will be shown in the label
                password_label = Label(root, text=password, font=("Arial", 12))
                password_label.place(x=95, y=200, width=150)
                number_of_passwords = number_of_passwords + 1
                with open("passwords.txt", "a") as  f:
                    f.write(f"password {number_of_passwords}: {password}\n")

        elif use_b == True:
            if value == 0 or value == None:
                messagebox.showerror("Error", "Please enter a chart number")
            elif int(value) > 0:
                password = generate_the_password.generate_random_string(int(value))
                messagebox.showinfo("Password", password)
                #the password will be shown in the label
                password_label = Label(root, text=password, font=("Arial", 12))
                password_label.place(x=95, y=200, width=150)
                number_of_passwords = number_of_passwords + 1
                with open("passwords.txt", "a") as  f:
                    f.write(f"password {number_of_passwords}: {password}\n")
def plus():
    global chart_n
    chart_n += 1
    chart_n_entry.delete(0, END)
    chart_n_entry.insert(0, chart_n)

def minus():
    global chart_n
    chart_n -= 1
    chart_n_entry.delete(0, END)
    chart_n_entry.insert(0, chart_n)

#make the chart number label
chart_n_label = Label(root, text="Chart number", font=("Arial", 12))
chart_n_label.place(x=10, y=50)
#make the chart number entry
chart_n_entry = Entry(root, font=("Arial", 12),textvariable=chart_n)
chart_n_entry.place(x=130, y=50, width=50)
#make the plus and minus button
plus_button = Button(root, text="⬆", font=("Arial", 12),bg = "light green",relief=FLAT,command = plus)
plus_button.place(x=190, y=45)

minus_button = Button(root, text="⬇", font=("Arial", 12),bg = "red",relief=FLAT,command = minus)
minus_button.place(x=230, y=45)

#make the generate button
generate_button = Button(root, text="Generate", font=("Arial", 12),bg = "orange",relief=FLAT,command = generate_pass)
generate_button.place(x=95, y=130, width=150)

#make the notes label
notes_label = Label(root, text="Note: Passwords will be saved in passwords.txt", font=("Arial", 10,"bold"),bg = "yellow")
notes_label.place(y=325)


root.mainloop()