from tkinter import Label, Button, Entry
from tkinter.font import Font


from kies_karakter_menu import plaatjes_formateren


def ga_naar_kies_verhaal(root, karakter):
    from kies_verhaal import kies_verhaal_scherm
    kies_verhaal_scherm(root, karakter)


def ga_naar_kies_karakter(root):
    from kies_karakter_menu import kies_karakter_menu_scherm
    kies_karakter_menu_scherm(root)


def krijg_waarde_en_ga_door(root, statestieken, naam):
    if naam != "":
        statestieken.update({"naam": naam[:10]})
        schrijf_karakter_weg(statestieken)
        ga_naar_kies_verhaal(root, statestieken)


def schrijf_karakter_weg(karakter):
    with open("bestanden/karakter_info.txt", "w") as bestand:
        bestand.write(karakter["naam"] + ";" + karakter["ras"] + ";" + str(karakter["kracht"]) + ";" +
                      str(karakter["verdediging"]) + ";" + str(karakter["sluip"]) + ";" + str(karakter["levens"])+ ";" + str(karakter["max_levens"]) + ";" + karakter["eigenschap"] +
                      ";" + karakter["einde1"] + ";" + karakter["einde2"] + ";" + karakter["einde3"])


def kies_naam_scherm(venster, stats):
    root = venster
    for widget in root.winfo_children():
        widget.destroy()
    label_font = Font(family="Aniron", size=36, weight="bold")
    label_plaatje = plaatjes_formateren(root, "bestanden/backgroundmenu5.jpg", 1700, 1000)
    label_naam_kiezen_titel = Label(root, text="Kies je naam", font=label_font, background="grey")
    label_naam_vraag = Label(root, text="Wat is de naam van jouw " + stats["ras"] + "?", font=label_font,
                             background="grey")

    naam_invul_veld = Entry(root, bd=1, width=30, font=label_font, background="grey")
    knop_terug = Button(root, text="Terug", font=label_font, background="grey",
                        command=lambda: ga_naar_kies_karakter(root))
    knop_volgende = Button(root, text="Volgende", font=label_font, background="grey",
                           command=lambda: krijg_waarde_en_ga_door(root, stats, naam_invul_veld.get()))

    label_plaatje.place(relx=0, rely=0, relwidth=1, relheight=1)
    label_naam_kiezen_titel.place(relx=0.5, rely=0.1, anchor="center")
    label_naam_vraag.place(relx=0.5, rely=0.3, anchor="center")
    naam_invul_veld.place(relx=0.5, rely=0.5, anchor="center")
    knop_terug.place(relx=0, rely=1, anchor="sw")
    knop_volgende.place(relx=1, rely=1, anchor="se")

    root.mainloop()
