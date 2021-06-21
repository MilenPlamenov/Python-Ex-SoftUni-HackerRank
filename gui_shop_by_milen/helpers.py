from gui_shop_by_milen.canvas import tk


def clean_screen():
    for el in tk.grid_slaves():
        el.destroy()