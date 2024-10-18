import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def Password_Generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    Password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        messagebox.showinfo(title=Website_input.get(), message="Email: " + data[Website_input.get()]["email"] + "\nPassword: " + data[Website_input.get()]["password"])

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message="No such data saved!")


def save():

    new_data = {
        Website_input.get(): {
            "email": Email_input.get(),
            "password": Password_input.get()
        }
    }
    if len(Website_input.get()) == 0 or len(Password_input.get()) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                data_data = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            data_data.update(new_data)

            with open("data.json", "w") as data:
                json.dump(data_data, data, indent=4)

        finally:
            Website_input.delete(0, tkinter.END)
            Password_input.delete(0, tkinter.END)
            Website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_png = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

Website_Label = tkinter.Label(text="Website:")
Website_Label.grid(column=0, row=1)

Website_input = tkinter.Entry(width=34)
Website_input.grid(column=1, row=1)
Website_input.focus()

Search_Button = tkinter.Button(text="Search", command=find_password, width=13)
Search_Button.grid(column=2, row=1)

Email_Label = tkinter.Label(text="Email/Username:")
Email_Label.grid(column=0, row=2)

Email_input = tkinter.Entry(width=53)
Email_input.insert(0, "atharvmitt@gmail.com")
Email_input.grid(column=1, row=2, columnspan=2)

Password_Label = tkinter.Label(text="Password:")
Password_Label.grid(column=0, row=3)

Password_input = tkinter.Entry(width=34)
Password_input.grid(column=1, row=3)

Generate_Password_Button = tkinter.Button(text="Generate Password", command=Password_Generator)
Generate_Password_Button.grid(column=2, row=3)

Add_Button = tkinter.Button(text="Add", width=45, command=save)
Add_Button.grid(column=1, row=4, columnspan=2)
window.mainloop()
