import bcrypt
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from admin import admin_laat_pagina_zien
import os


def hash_wachtwoord(wachtwoord):
    salt = bcrypt.gensalt()
    gehasht_wachtwoord = bcrypt.hashpw(wachtwoord.encode('utf-8'), salt)
    return gehasht_wachtwoord, salt


def opvragen_opgeslagen_hashed_wachtwoord():
    bestand_naam = os.path.join('bestanden', 'kaas.txt')

    try:
        with open(bestand_naam, 'r') as bestand:
            opgeslagen_gehashte_wachtwoord = bestand.read().strip()
            return opgeslagen_gehashte_wachtwoord.encode('utf-8')
    except FileNotFoundError:
        print(f"Bestand {bestand_naam} niet gevonden.")
        return None


def laat_pagina_zien(root):
    for widget in root.winfo_children():
        widget.destroy()

    achtergrond = Image.open("bestanden/pixelated_sauron.jpg")
    geherformateerde_achtergrond = achtergrond.resize((root.winfo_screenwidth(), root.winfo_screenheight()),
                                                      Image.LANCZOS)
    foto = ImageTk.PhotoImage(geherformateerde_achtergrond)

    achtergrond_label = Label(root, image=foto)
    achtergrond_label.image = foto
    achtergrond_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas = Canvas(root, width=foto.width(), height=foto.height())
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=foto)

    label_font = Font(family="Aniron", size=16, weight="bold")
    label = Label(canvas, text="Admin pagina", font=label_font, bg="grey")
    label.pack(pady=20)

    label_font = Font(family="Aniron", size=12)
    label = Label(canvas, text="Voer het admin wachtwoord in:", font=label_font, bg="grey")
    label.pack(pady=10)

    wachtwoord_entry = Entry(canvas, show="*", fg="black", font=("Aniron", 20, "bold"))
    wachtwoord_entry.pack(pady=10, anchor="center")

    knop_font = Font(family="Aniron", size=20, weight="bold")
    knop_bg_kleur = "grey"

    knop = Button(canvas, text="Login", command=lambda: check_wachtwoord(wachtwoord_entry, root),
                  font=knop_font, bg=knop_bg_kleur)
    knop.pack(pady=10)

    knop_terug = Button(root, text="Terug", font=knop_font, width=10, height=2,
                        command=lambda: ga_naar_main_menu(root), bg=knop_bg_kleur)
    knop_terug.pack(pady=10, anchor="center")


def ga_naar_main_menu(root):
    from hoofdmenu import maak_hoofdmenu_aan
    maak_hoofdmenu_aan(root)


def check_wachtwoord(wachtwoord_entry, root):
    for widget in root.winfo_children():
        if isinstance(widget, Label) and widget["text"] == "Incorrect wachtwoord":
            widget.destroy()

    opgslagen_hashed_wachtwoord = opvragen_opgeslagen_hashed_wachtwoord()
    gebruiker_invoeg_wachtwoord = wachtwoord_entry.get()

    try:
        if bcrypt.checkpw(gebruiker_invoeg_wachtwoord.encode('utf-8'), opgslagen_hashed_wachtwoord):
            admin_laat_pagina_zien(root)
        else:
            fout_melding_label = Label(root, text="Incorrect wachtwoord", fg="red")
            fout_melding_label.pack(pady=10)
    except Exception:
        fout_melding_label = Label(root, text="Er is een fout opgetreden bij het controleren van het wachtwoord",
                                   fg="red")
        fout_melding_label.pack(pady=10)
