import json
import tkinter as tk
from email.utils import specialsre

from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from canvas import app
from helpers import clean_screen
from products import render_products_screen


def login(username, password):
    with open('db/user_credentials_db.txt') as file:
        data = file.readlines()
        for line in data:
            name, pwd = line.strip().split(", ")
            if name == username and pwd == password:
                with open("db/current_user.txt", "w") as f:
                    f.write(name)
                render_products_screen()
                return
    render_login_screen(error="Invalid username/password")



def render_login_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0,
                  column=0
                  )
    password = tk.Entry(app)
    password.grid(row=1,
                  column=0)

    tk.Button(app,
              text = "Enter",
              bg = "green",
              fg = "black",
              command = lambda: login(username.get(), password.get())
              ).grid(row=2,
                     column=0)

    if error:
        tk.Label(app,
                 text = error,
                 ).grid(row=3,
                        column=0
                        )


def register(**user): # username, password, first_name, last_name
    # TODO: Validations

    if user["username"] == '' or user["password"] == "" or user["first_name"] == "" or user["last_name"] == "":
        render_register_screen(error="All fields must be filled!")
        return

    if len(user["username"]) < 5:
        render_register_screen(error="Username must contain at least 5 characters.")
        return

    if len(user["password"]) < 5:
        render_register_screen(error="Password must contain at least 5 characters.")
        return

    pass_validation_mapper = {"upper": False,
                              "lower": False,
                              "digit": False,
                              "special": False
                              }
    for char in user["password"]:
        if char in ascii_uppercase:
            pass_validation_mapper["upper"] = True
        elif char in ascii_lowercase:
            pass_validation_mapper["lower"] = True
        elif char in digits:
            pass_validation_mapper["digit"] = True
        elif char in punctuation:
            pass_validation_mapper["special"] = True
    if not all(pass_validation_mapper.values()):
        render_register_screen(error="Password must contain at least one uppercase,"
                                     " lowercase, digit and/or a special "
                                     "character")
        return

    if len(user["first_name"]) < 3:
        render_register_screen(error="Name must be at least 3 characters long.")
        return
    if len(user["last_name"]) < 3:
        render_register_screen(error="Last name must be at least 3 characters long.")
        return


    user.update({"products": []})

    with open("db/user_credentials_db.txt", "r+", newline="\n") as file:
        users = [line.strip().split(", ")[0] for line in file]
        if user["username"] in users:
            render_register_screen(error="User already exists!")
            return
        file.write(f"{user['username']}, {user['password']}\n")
    with open("db/users.txt", "a", newline= "\n") as file:
        file.write(json.dumps(user) + "\n")
    render_login_screen()

def render_register_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row= 0,
                  column= 0)
    password = tk.Entry(app)
    password.grid(row= 1,
                  column= 0)
    first_name = tk.Entry(app)
    first_name.grid(row=2 ,
                    column= 0)
    last_name = tk.Entry(app)
    last_name.grid(row=3,
                   column= 0)
    button = tk.Button(app,
                       text= "Register",
                       bg= "green",
                       fg= "black",
                       command= lambda: register(
                           username= username.get(),
                           password= password.get(),
                           first_name= first_name.get(),
                           last_name= last_name.get()
                       ))
    button.grid(row=4,
                column=0)

    if error:
        tk.Label(app,
                 text = error,
                 ).grid(row=5,
                        column=0
                        )

def render_main_enter_screen():
    tk.Button(
        app,
        text="Login",
        background="green",
        foreground='white',
        command = render_login_screen
        ).grid(row=0,
               column=0)
    tk.Button(
        app,
        text="Register",
        background="yellow",
        foreground="black",
        command = render_register_screen
        ).grid(row=0, column=1)

