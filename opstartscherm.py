import tkinter as tk
from PIL import Image, ImageTk
from time import sleep


def task():
    root.destroy()


def laadbalk_updaten():
    for laden in range(101):
        canvas.coords(progress_rect, 0, 0, laden * 4, 20)
        root.update_idletasks()
        sleep(0.02)


root = tk.Tk()
root.title("Lord of The Rings game")

logo_plaatje = "bestanden/Sauron_logo_hsl.png"
plaatje = Image.open(logo_plaatje)
plaatje = plaatje.resize((400, 400))
foto = ImageTk.PhotoImage(plaatje)
plaatje_label = tk.Label(root, image=foto)
plaatje_label.pack()

scherm_breedte = root.winfo_screenwidth()
scherm_hoogte = root.winfo_screenheight()

x = (scherm_breedte - 400) // 2
y = (scherm_hoogte - 400) // 2

root.geometry("400x430+{}+{}".format(x, y))

canvas = tk.Canvas(root, width=400, height=20)
canvas.pack()

progress_rect = canvas.create_rectangle(0, 0, 0, 20, fill="black")

root.after(200, laadbalk_updaten)
root.after(2200, task)
root.mainloop()
