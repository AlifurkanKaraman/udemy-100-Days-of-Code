from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_textbox.delete(0, 'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_textbox.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # To get data from text boxes
    website = website_textbox.get()
    email = email_textbox.get()
    password = password_textbox.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            # To save our data inside a file
            f = open("data.txt", 'a')
            f.write(f"{website} | {email} | {password}\n")
            f.close()

            website_textbox.delete(0, 'end')
            email_textbox.delete(0, 'end')
            password_textbox.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website text box
website_textbox = Entry(width=51)
website_textbox.grid(column=1, row=1, columnspan=2)

# Email/Username label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# Email text box
email_textbox = Entry(width=51)
email_textbox.grid(column=1, row=2, columnspan=2)

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password text box
password_textbox = Entry(width=33)
password_textbox.grid(column=1, row=3)

# Generate Password button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()