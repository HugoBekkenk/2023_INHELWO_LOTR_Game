from PIL import ImageTk, Image
from tkinter import Label, Button
from tkinter.font import Font
from kies_karakter_menu import plaatjes_formateren, kies_karakter_menu_scherm
import wachtwoord
import pygame


def ga_naar_kies_karakter(root):
    kies_karakter_menu_scherm(root)


def ga_naar_admin(root):
    wachtwoord.laat_pagina_zien(root)


def ga_naar_kies_adventure(root, karakter):
    from kies_verhaal import kies_verhaal_scherm
    kies_verhaal_scherm(root, karakter)


def controleer_karakters():
    with open("bestanden/karakter_info.txt") as bestand:
        karakter = bestand.read()
        karakter = karakter.replace("\n", "")
        karakter_info = karakter.split(";")
        if len(karakter_info) == 11:
            karakter_dictionary = {
                "kracht": int(karakter_info[2]),
                "verdediging": int(karakter_info[3]),
                "levens": int(karakter_info[5]),
                "max_levens": int(karakter_info[6]),
                "eigenschap": karakter_info[7],
                "sluip": int(karakter_info[4]),
                "ras": karakter_info[1],
                "naam": karakter_info[0],
                "einde1": karakter_info[8],
                "einde2": karakter_info[9],
                "einde3": karakter_info[10]
            }
            return karakter_dictionary
        else:
            return False


def maak_hoofdmenu_aan(root):
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("bestanden/13 The Bridge Of Khazad Dum.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    for widget in root.winfo_children():
        widget.destroy()
    label_font = Font(family="Aniron", size=36, weight="bold")
    label_achtergrond = plaatjes_formateren(root, "bestanden/backgroundmenu2_edit.png", 1700, 1000)
    label = Label(root, text="Hoofdmenu", font=label_font, background="grey", border=5)
    knop_kies_karakter = Button(root, text="Maak je karakter", borderwidth=5, font=label_font, background="grey",
                                command=lambda: ga_naar_kies_karakter(root))
    knop_programma_afsluiten = Button(root, text="exit", borderwidth=5, font=label_font, background="grey",
                                      command=exit)
    karakter = controleer_karakters()
    if karakter:
        if karakter["levens"] > 0:
            button_karakter = Button(root, text="Kies " + karakter["naam"], borderwidth=5, font=label_font,
                                 background="grey", command=lambda: ga_naar_kies_adventure(root, karakter))
            button_karakter.place(relx=0.5, rely=0.5, anchor="center")

    foto_admin_menu = Image.open("bestanden/hsleiden_pixelated.png")
    foto_admin_menu = foto_admin_menu.resize((100, 100), Image.LANCZOS)
    foto_admin_menu = ImageTk.PhotoImage(foto_admin_menu)

    knop_admin_menu = Button(root, image=foto_admin_menu, command=lambda: ga_naar_admin(root))
    knop_admin_menu.image = foto_admin_menu

    label_achtergrond.place(x=0, y=0, relwidth=1, relheight=1)
    label.place(relx=0.5, rely=0.1, anchor="center")
    knop_kies_karakter.place(relx=0.5, rely=0.3, anchor="center")
    knop_programma_afsluiten.place(relx=0.5, rely=0.7, anchor="center")
    knop_admin_menu.place(relx=0.9, rely=0.9, anchor="center")

    root.mainloop()
