import json
import os
import tkinter as tk

from PIL import Image, ImageTk

from canvas import app
from helpers import clean_screen

base_folder = os.path.dirname(__file__)


def update_current_user(username, product_id):
    with open("db/users.txt", "r+", newline="\n") as f:
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                f.seek(0)
                f.truncate(0)
                f.writelines([json.dumps(u) + "\n" for u in users])
                return


def purchase_product(product_id):
    with open("db/products.txt", "r+") as f:
        products = [json.loads(p.strip()) for p in f if p.strip()]
        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                f.seek(0)
                f.truncate(0)
                f.writelines([json.dumps(p) + "\n" for p in products])


def buy_product(product_id):
    clean_screen()

    with open("db/current_user.txt") as file:
        username = file.read()

        if username:
            update_current_user(username, product_id)
            purchase_product(product_id)

    render_products_screen()


def add_product(name, img_path, count):
    with open("db/products.txt", "r+") as f:
        products = [json.loads(p.strip()) for p in f if p.strip()]
        count = int(count)
        new_id = max([p["id"] for p in products]) + 1 if products else 1
        new_products = {
            "id": new_id,
            "name": name,
            "img_path": img_path,
            "count": count
        }

        products.append(new_products)
        f.seek(0)
        f.truncate()
        f.writelines([json.dumps(p) + "\n" for p in products])
    render_products_screen()


def render_add_product_screen():
    clean_screen()

    tk.Label(app,
             text="Name: ").grid(row=0, column=0)
    name = tk.Entry(app)
    name.grid(row=0, column=1)

    tk.Label(app, text="Image path: ").grid(row=1, column=0)
    img_path = tk.Entry(app)
    img_path.grid(row=1, column=1)

    tk.Label(app, text="Count: ").grid(row=2, column=0)
    count = tk.Entry(app)
    count.grid(row=2, column=1)

    tk.Button(app,
              text="Add",
              command=lambda: add_product(name.get(), img_path.get(), count.get())
              ).grid(row=3, column=0, columnspan=2)
    tk.Button(app,
              text="Back",
              command=lambda: render_products_screen()
              ).grid(row=4, column=0, columnspan=2)



def render_products_screen():
    clean_screen()

    with open("db/current_user.txt") as file:
        username = file.read()

    with open("db/users.txt") as f:
        users = [json.loads(u.strip()) for u in f if u.strip()]
        for user in users:
            if user["username"] == username and user["is_admin"]:
                tk.Button(app,
                          text="Add product",
                          command=lambda: render_add_product_screen()
                          ).grid(row=0, column=0)

    with open("db/products.txt", "r") as file:
        products = [json.loads(p.strip()) for p in file if p.strip()]
        products = [p for p in products if p["count"] > 0]

        products_per_line = 6
        lines_per_product = len(products[0])

        for i, product in enumerate(products):
            row = i // products_per_line * lines_per_product + 1
            column = i % products_per_line

            tk.Label(app,
                     text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, "db/images", product["img_path"])).resize((120, 120))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1,
                             column=column)

            tk.Label(app, text=product["count"]).grid(row=row + 2, column=column)
            tk.Button(app,
                      text=f"Buy {product["id"]}",
                      command=lambda p=product["id"]: buy_product(p)
                      ).grid(row=row + 3, column=column)
