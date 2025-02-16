from tkinter import Tk
from hoofdmenu import maak_hoofdmenu_aan
from opstartscherm import task


def main():
    root = Tk()
    root.attributes('-fullscreen', True)
    root.title("Lord of The Rings game")
    root.configure(background='grey')
    maak_hoofdmenu_aan(root)
    root.after(100, task)
    root.mainloop()


if __name__ == '__main__':
    main()
