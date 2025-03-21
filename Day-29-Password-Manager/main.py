import tkinter as tk
from tkinter import messagebox
import config
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    rand_letters = random.choices(config.letters, k=nr_letters)
    rand_symbols = random.choices(config.symbols, k=nr_symbols)
    rand_numbers = random.choices(config.numbers, k=nr_numbers)

    random_list = rand_letters + rand_symbols + rand_numbers
    random.shuffle(random_list)

    password = "".join(random_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if len(website.strip()) == 0 or len(user.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo(title="OOPS!", message="Make sure no fields are empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user} \nPassword: "
                                       f"{password} \nOk to save?")
    if is_ok:
        with open("data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {user} | {password}\n")
        website_input.delete(0, tk.END)
        password_input.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# --- LABELS ---
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1, sticky=tk.E)
user_label = tk.Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky=tk.E)
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3, sticky=tk.E)

# --- BUTTONS ---
generate_button = tk.Button(text="Generate", command=generate)
generate_button.grid(column=2, row=3)
add_button = tk.Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=tk.EW)

# --- ENTRIES ---
website_input = tk.Entry()
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky=tk.EW)
user_input = tk.Entry()
user_input.insert(0, "example@gmail.com")
user_input.grid(column=1, row=2, columnspan=2, sticky=tk.EW)
password_input = tk.Entry()
password_input.grid(column=1, row=3, sticky=tk.EW)



root.mainloop()
