from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import Label, Button


def ga_naar_main_menu(root):
    from hoofdmenu import maak_hoofdmenu_aan
    maak_hoofdmenu_aan(root)


def ga_naar_kies_naam(root, stats):
    from kies_naam import kies_naam_scherm
    kies_naam_scherm(root, stats)


def plaatjes_formateren(root, bestanden_naam, x, y):
    plaatje = Image.open(bestanden_naam)
    aangepast_plaatje = plaatje.resize((x, y), Image.LANCZOS)
    voorbeeld_plaatje = ImageTk.PhotoImage(aangepast_plaatje)
    label_plaatje = Label(root, image=voorbeeld_plaatje)
    label_plaatje.image = voorbeeld_plaatje
    return label_plaatje


def ras_knop_functie(root, stats, bestand_naam, label_font):
    statistieken_label = Label(root, text="Statistieken\n\n" + "Kracht: " + str(stats["kracht"]) + "\n\n" +
                                          "Verdediging: " + str(stats["verdediging"]) +"\n\n" +
                                          "Sluip kracht: " + str(stats["sluip"]) + "\n\n" + "Levens: " +
                                          str(stats["max_levens"]) + "\n\n\n" + "Speciale eigenschap:\n\n" +
                                          stats["eigenschap"], width=25, height=17, font=label_font, wraplength=500, background="grey")

    volgende_knop = Button(root, text="Volgende", font=label_font, width=10, height=2, background="grey",
                           command=lambda: ga_naar_kies_naam(root, stats))
    ras_plaatje = plaatjes_formateren(root, bestand_naam, 750, 850)

    statistieken_label.place(relx=0.22, rely=0.8, anchor="sw")
    volgende_knop.place(relx=0.30, rely=1, anchor="sw")
    ras_plaatje.place(relx=0.56, rely=1, anchor="sw")


def kies_karakter_menu_scherm(venster):
    root = venster
    for widget in root.winfo_children():
        widget.destroy()
    elf_statistieken = {"kracht": 15,
                        "verdediging": 10,
                        "levens": 15,
                        "max_levens": 15,
                        "eigenschap": "Elven hebben geweldig zicht, beter dan elk ander ras!",
                        "sluip": 7,
                        "ras": "elf",
                        "einde1": "niet",
                        "einde2": "niet",
                        "einde3": "niet"
                        }
    dwerg_statistieken = {"kracht": 15,
                          "verdediging": 14,
                          "levens": 7,
                          "max_levens": 7,
                          "eigenschap":
                          "Dwergen zijn gewend in de mijnen te leven, dus ondergronds hebben ze het voordeel!",
                          "sluip": 0,
                          "ras": "dwerg",
                          "einde1": "niet",
                          "einde2": "niet",
                          "einde3": "niet"
                          }
    hobbit_statistieken = {"kracht": 10,
                           "verdediging": 8,
                           "levens": 13,
                           "max_levens": 13,
                           "eigenschap":
                           "Hobbits zijn klein, dus ze kunnen door doorgangen die voor andere onbeschikbaar zijn!",
                           "sluip": 10,
                           "ras": "hobbit",
                           "einde1": "niet",
                           "einde2": "niet",
                           "einde3": "niet"
                           }
    mens_statistieken = {"kracht": 13,
                         "verdediging": 12,
                         "levens": 13,
                         "max_levens": 13,
                         "eigenschap": "Mensen zijn heel nobel, dus ze geven niet snel op in een gevecht!",
                         "sluip": 4,
                         "ras": "mens",
                         "einde1": "niet",
                         "einde2": "niet",
                         "einde3": "niet"
                         }
    dwerg_bestand = "bestanden/dwerg_no_background_border.png"
    elf_bestand = "bestanden/elf_no_background_border.png"
    hobbit_bestand = "bestanden/hobbit_no_background_border.png"
    mens_bestand = "bestanden/mens_no_background_border.png"
    achtergrond_bestand = "bestanden/backgroundmenu1.jpg"

    label_font = Font(family="Aniron", size=25, weight="bold")

    achtergrond = plaatjes_formateren(root, achtergrond_bestand, 1920, 1080)
    achtergrond.place(x=0, y=0, relwidth=1, relheight=1)

    elf_knop = Button(root, text="Elf", width=10, height=2, font=label_font, background="grey",
                      command=lambda: ras_knop_functie(root, elf_statistieken, elf_bestand, label_font))
    dwerg_knop = Button(root, text="Dwerg", width=10, height=2, font=label_font, background="grey",
                        command=lambda: ras_knop_functie(root, dwerg_statistieken, dwerg_bestand, label_font))
    hobbit_knop = Button(root, text="Hobbit", width=10, height=2, font=label_font, background="grey",
                         command=lambda: ras_knop_functie(root, hobbit_statistieken, hobbit_bestand, label_font))
    mens_knop = Button(root, text="Mens", width=10, height=2, font=label_font, background="grey",
                       command=lambda: ras_knop_functie(root, mens_statistieken, mens_bestand, label_font))
    terug_knop = Button(root, text="Terug", width=10, height=2, font=label_font, background="grey",
                        command=lambda: ga_naar_main_menu(root))

    elf_knop.place(relx=0, rely=0.2, anchor="sw")
    dwerg_knop.place(relx=0, rely=0.4, anchor="sw")
    hobbit_knop.place(relx=0, rely=0.6, anchor="sw")
    mens_knop.place(relx=0, rely=0.8, anchor="sw")
    terug_knop.place(relx=0, rely=1, anchor="sw")
    root.mainloop()
