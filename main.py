from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ------------------------- PASSWORD GENERATOR -------------------------#
def password_generator():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbol_list = [choice(symbols) for char in range(randint(2, 4))]
    number_list = [choice(numbers) for char in range(randint(2, 4))]
    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password_s = "".join(password_list)
    pwd_entry.insert(0, password_s)

    pyperclip.copy(password_s)


# ------------------------- SAVE PASSWORD ------------------------------#

def save_pwd():
    website = web_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Something went wrong!!😶", message="Please don't leave any field empty!!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                                      f" \n Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("passwordManager", "a") as file:
                file.write(f"{website} | {email} | {password} \n")

            web_entry.delete(0, END)
            email_entry.delete(0, END)
            pwd_entry.delete(0, END)


# ------------------------- UI SETUP -----------------------------------#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Adding images
canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=2)

# Making Labels
web_label = Label(text="Website: ")
web_label.grid(row=2, column=1)

email_label = Label(text="Email/Username: ")
email_label.grid(row=3, column=1)

pwd_label = Label(text="Password:  ")
pwd_label.grid(row=4, column=1)

# Entry
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=2, column=2, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "abc@example.com ")
email_entry.grid(row=3, column=2, columnspan=2)

pwd_entry = Entry(width=35)
pwd_entry.grid(row=4, column=2, columnspan=2)

# Buttons
pwd_button = Button(text="Generate Password", command=password_generator)
pwd_button.grid(row=4, column=3)

add_button = Button(text="Add", command=save_pwd, width=36)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
