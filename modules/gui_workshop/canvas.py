import tkinter as tk


def create_app():
    root = tk.Tk()
    root.geometry("700x600+100+100")
    root.title("GUI Product Shop")
    return root

app = create_app()