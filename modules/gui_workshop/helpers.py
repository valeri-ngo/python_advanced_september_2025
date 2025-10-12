from canvas import app


def clean_screen():
    for ele in app.grid_slaves():
        ele.destroy()