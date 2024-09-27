import tkinter as tk
from tkinter import ttk
import re

root = tk.Tk()
root.title("Registration")

# The code which opens the window in the middle of the screen.
window_width = 470
window_height = 395

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
# ........................................................

### List maker and lists.
# Made list of numbers.
numbers_list = list(range(1, 32))

# Made list of years.
years_list = list(range(1900, 2024))

# Month list.
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# ...................................

# Labels for entry titles.
first_name_ttl = tk.Label(root, text="First Name", font=("Arial", 12))
first_name_ttl.place(x=10, y=10)

last_name_ttl = tk.Label(root, text="Last Name", font=("Arial", 12))
last_name_ttl.place(x=10, y=60)

email_ttl = tk.Label(root, text="Email Address", font=("Arial", 12))
email_ttl.place(x=10, y=110)

password_ttl = tk.Label(root, text="Password", font=("Arial", 12))
password_ttl.place(x=10, y=160)

password_repeat_ttl = tk.Label(root, text="Repeat Password", font=("Arial", 12))
password_repeat_ttl.place(x=10, y=210)

date_ttl = tk.Label(root, text="Date Of Birth", font=("Arial", 20))
date_ttl.place(x=245, y=10)

numbers_ttl = tk.Label(root, text="Choose number", font=("Arial", 12))
numbers_ttl.place(x=247, y=60)

month_ttl = tk.Label(root, text="Choose Month", font=("Arial", 12))
month_ttl.place(x=247, y=110)

years_ttl = tk.Label(root, text="Choose Year", font=("Arial", 12))
years_ttl.place(x=247, y=160)
# .........................................

# Entries.
first_name_ent = tk.Entry(root, width=30)
first_name_ent.place(x=13, y=33)

last_name_ent = tk.Entry(root, width=30)
last_name_ent.place(x=13, y=83)

email_ent = tk.Entry(root, width=30)
email_ent.place(x=13, y=133)

password_ent = tk.Entry(root, show="*", width=30)
password_ent.place(x=13, y=183)

password_repeat_ent = tk.Entry(root, show="*",width=30)
password_repeat_ent.place(x=13, y=233)

numbers_dropbox = ttk.Combobox(root, state="readonly", values=numbers_list)
numbers_dropbox.place(x=250, y=83)

month_dropbox = ttk.Combobox(root, state="readonly", values=months_list)
month_dropbox.place(x=250, y=133)

years_dropbox = ttk.Combobox(root, state="readonly", values=years_list)
years_dropbox.place(x=250, y=183)
# .....................................

# This is the main function which contains every function together and prints the final label.
def main():
    answer = final_checker()
    final_label.config(text=answer)
    final_label.place(x=20, y=260)
# .....................................................................................

# First name and last name getter and validator functions.
def get_names():
    try:
        first_name = first_name_ent.get().strip().title()
        last_name = last_name_ent.get().strip().title()
        return first_name, last_name
    except Exception as e:
        return "There is a problem."

def validate_name():
    if get_names() != "There is a problem.":
        first_name, last_name = get_names()

        if first_name.isalpha() and last_name.isalpha() and first_name not in ["", " "] and last_name not in ["", " "]:
            return True
        else:
            return False
    else:
        return False
# ......................................................

# Password and repeated password getter and validator functions.
def get_password():
    try:
        password = password_ent.get()
        repeated_password = password_repeat_ent.get()
        return password, repeated_password
    except Exception as e:
        return "There is a problem."

def validate_password():
    if get_password() != "There is a problem.":
        password, repeated_password = get_password()
        if len(password) >= 8 and repeated_password == password:
            return True
        else:
            return False
    else:
        return False
# .......................................

# Number, month, and year getter and validator functions.
def get_date():
    try:
        number = numbers_dropbox.get()
        month = month_dropbox.get()
        year = years_dropbox.get()
        return number, month, year
    except Exception as e:
        return "There is a problem."

def validate_date():
    if get_date() != "There is a problem.":
        number, month, year = get_date()
        if (number.isdigit() and 1 <= int(number) <= 31) and month in months_list and (year.isdigit() and 1900 <= int(year) <= 2024):
            return True
        else:
            return False
    else:
        return False
# .....................................................

# Email getter and validator functions.
def get_email():
    try:
        email = email_ent.get()
        return email
    except Exception as e:
        return "There is a problem."

def validate_email():
    if get_email() != "There is a problem.":
        email = get_email()
        if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            return True
        else:
            return False
    else:
        return False
# ....................................

# Final checker function.
def final_checker():
    errors = []

    if not validate_name():
        errors.append("There is a problem with the names. Please ensure both names are alphabetic and not empty.")

    if not validate_password():
        errors.append("There is a problem with the password. Ensure it is at least 8 characters long and both passwords match.")

    if not validate_date():
        errors.append("There is a problem with the date. Ensure the day, month, and year are selected correctly.")

    if not validate_email():
        errors.append("There is a problem with the email. Ensure the email is in the correct format.")

    if errors:
        return "\n".join(errors)
    else:
        return "Everything is valid, your account was created successfully."
# ....................................................

# Label to display error or success messages.
final_label = tk.Label(root, font=("Arial", 10), wraplength=400)
final_label.place(x=20, y=270)

# Button to create account
create_acc_btn = tk.Button(root,
                           width=10,
                           padx=10,
                           text="Create Account",
                           fg="White",
                           bg="Black",
                           font=("Arial", 10),
                           command=main
                           )
create_acc_btn.place(x=265, y=225)
# .........................

root.mainloop()
