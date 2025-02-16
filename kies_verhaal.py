from tkinter import Label, Button
from tkinter.font import Font
from kies_karakter_menu import plaatjes_formateren


def ga_naar_spel(root, karakter, adventure_bestand_naam, muziek_bestand_naam):
    from verhaal_spel_spelen import spel_starten
    spel_starten(root, karakter, adventure_bestand_naam, muziek_bestand_naam)


def ga_naar_kies_naam(root, karakter):
    from kies_naam import kies_naam_scherm
    del karakter["naam"]
    kies_naam_scherm(root, karakter)


def kies_verhaal_scherm(venster, karakter):
    root_window = venster
    for widget in root_window.winfo_children():
        widget.destroy()
    label_font = Font(family="Aniron", size=36, weight="bold")
    label_plaatje = plaatjes_formateren(root_window, "bestanden/backgroundmenu3.jpg", 1700, 1000)
    gehaal_label = Label(root_window, text="Gehaald", font=label_font, background="grey")
    einde_1 = Label(root_window, text=karakter["einde1"], font=label_font,
                    background="grey")
    einde_2 = Label(root_window, text=karakter["einde2"], font=label_font,
                    background="grey")
    einde_3 = Label(root_window, text=karakter["einde3"], font=label_font,
                    background="grey")

    label = Label(root_window, text="Verhaal menu van de " + karakter["ras"] + " " + karakter["naam"], font=label_font,
                  background="grey")
    knop_verhaal_1 = Button(root_window, text="De mijnen van Moria", font=label_font, background="grey",
                            command=lambda: ga_naar_spel(root_window, karakter, "bestanden/scenario_een.json", "bestanden/01 The Prophecy.mp3"))
    knop_verhaal_2 = Button(root_window, text="Dol Amroth", font=label_font, background="grey",
                            command=lambda: ga_naar_spel(root_window, karakter, "bestanden/scenario_twee.json", "bestanden/11 The Ring Goes South.mp3"))
    knop_verhaal_3 = Button(root_window, text="De Gouw", font=label_font, background="grey",
                            command=lambda: ga_naar_spel(root_window, karakter, "bestanden/scenario_drie.json", "bestanden/02 Concerning Hobbits.mp3"))
    knop_terug = Button(root_window, text="Terug", font=label_font, background="grey",
                        command=lambda: ga_naar_kies_naam(root_window, karakter))

    label_plaatje.place(relx=0, rely=0, relwidth=1, relheight=1)
    label.place(relx=0.5, rely=0.1, anchor="center")
    knop_verhaal_1.place(relx=0.5, rely=0.3, anchor="center")
    knop_verhaal_2.place(relx=0.5, rely=0.5, anchor="center")
    knop_verhaal_3.place(relx=0.5, rely=0.7, anchor="center")
    gehaal_label.place(relx=0.9, rely=0.1, anchor="center")
    einde_1.place(relx=0.9, rely=0.3, anchor="center")
    einde_2.place(relx=0.9, rely=0.5, anchor="center")
    einde_3.place(relx=0.9, rely=0.7, anchor="center")

    knop_terug.place(relx=0, rely=1, anchor="sw")

    root_window.mainloop()
