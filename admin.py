from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from admin_verhaal import Verhaal1, Verhaal2, Verhaal3


verhaal1 = Verhaal1()
verhaal2 = Verhaal2()
verhaal3 = Verhaal3()


def admin_laat_pagina_zien(root):
    root.configure(bg="grey")

    for widget in root.winfo_children():
        widget.destroy()

    achtergrond_plaatje_laden(root)

    titel_font = Font(family="Aniron", size=24, weight="bold")
    titel_label = Label(root, text="Admin menu", font=titel_font, bg="grey")
    titel_label.pack(pady=20)

    knop_omlijning = Frame(root, bg="grey")
    knop_omlijning.pack(expand=True)

    knop_font = Font(family="Aniron", size=18, weight="bold")
    knop_achtergrond_kleur = "grey"

    knop_1 = Button(knop_omlijning, text="verhaal 1", font=knop_font, height=8, width=15,
                    command=lambda: verhaal1.laat_admin_verhaal_zien(root), bg=knop_achtergrond_kleur)
    knop_1.pack(side=LEFT, padx=10)

    knop_2 = Button(knop_omlijning, text="verhaal 2", font=knop_font, height=8, width=15,
                    command=lambda: verhaal2.laat_admin_verhaal_zien(root), bg=knop_achtergrond_kleur)
    knop_2.pack(side=LEFT, padx=10)

    knop_3 = Button(knop_omlijning, text="verhaal 3", font=knop_font, height=8, width=15,
                    command=lambda: verhaal3.laat_admin_verhaal_zien(root), bg=knop_achtergrond_kleur)
    knop_3.pack(side=LEFT, padx=10)

    terug_knop = Button(root, text="Terug", font=knop_font, width=10, height=2,
                        command=lambda: ga_naar_hoofdmenu(root), bg=knop_achtergrond_kleur)
    terug_knop.pack(pady=10, anchor="center")


def achtergrond_plaatje_laden(root):
    plaatje = Image.open("bestanden/pixelated_sauron.jpg")
    geherformateerde_plaatje = plaatje.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)

    foto = ImageTk.PhotoImage(geherformateerde_plaatje)

    achtergrond_label = Label(root, image=foto)
    achtergrond_label.image = foto
    achtergrond_label.place(x=0, y=0, relwidth=1, relheight=1)


def ga_naar_hoofdmenu(root):
    from hoofdmenu import maak_hoofdmenu_aan
    maak_hoofdmenu_aan(root)
