from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    try:
        with open("entries.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="File not found")
    else:
        if search_input.get() in data:
            messagebox.showinfo(title="Info", message=f"For {search_input.get()}, the password is {data[search_input.get()]['password']}")
        else:
            messagebox.showinfo(title="ERROR", message="Key not found")

def save_password():
    email = user_input.get()
    password = password_input.get()
    new_data = {
        website_input.get(): {
            "email": email,
            "password": password
        }
    }

    try:
        with open("entries.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("entries.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("entries.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
canvas.create_image(200, 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

search_lbl = Label(text="Search:")
search_lbl.grid(row=1, column=0)
search_input = Entry()
search_input.config(width=21)
search_input.grid(row=1, column=1, columnspan=2)
search_btn = Button(text="Search", command=search)
search_btn.grid(row=1, column=2)

website_lbl = Label(text="Website:")
website_lbl.grid(row=2, column=0)
website_input = Entry()
website_input.grid(row=2, column=1, columnspan=2)
website_input.config(width=41)
website_input.focus()

user_lbl = Label(text="Email/Username:")
user_lbl.grid(row=3, column=0)
user_input = Entry()
user_input.grid(row=3, column=1, columnspan=2)
user_input.config(width=41)
user_input.insert(0, "atalavera86@gmail.com")

password_lbl = Label(text="Password:")
password_lbl.grid(row=4, column=0)
password_input = Entry()
password_input.config(width=21)
password_input.grid(row=4, column=1)
generate_password_btn = Button(text="Generate Password")
generate_password_btn.grid(row=4, column=2)

add_btn = Button(text="Add", command=save_password)
add_btn.grid(row=5, column=1, columnspan=2)
add_btn.config(width=36)

window.mainloop()

