import json
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image


def achtergrond_plaatje_laden(root):
    plaatje = Image.open("bestanden/pixelated_sauron.jpg")
    geherformateerde_plaatje = plaatje.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)

    foto = ImageTk.PhotoImage(geherformateerde_plaatje)

    achtergrond_label = Label(root, image=foto)
    achtergrond_label.image = foto
    achtergrond_label.place(x=0, y=0, relwidth=1, relheight=1)
    achtergrond_label.lower()


knop_achtergrond_kleur = "grey"


class Verhaal1:
    def __init__(self):
        self.eindes = {}

    def laat_admin_verhaal_zien(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        achtergrond_plaatje_laden(root)

        bestand = open('bestanden/scenario_een.json', 'r')
        bestand_informatie = json.load(bestand)
        bestand.close()

        self.eindes = {
            "goed": bestand_informatie['goed_einde']['text'],
            "slecht": bestand_informatie['slecht_einde_deel_een']['text'],
        }

        titel_font = Font(family="Aniron", size=24, weight="bold")
        titel_label = Label(text="Admin menu", bg="grey", font=titel_font)
        titel_label.place(relx=0.5, rely=0.05, anchor="center")

        knop_font = Font(family="Aniron", size=16)

        goed_knop = Button(root, bg=knop_achtergrond_kleur, text="Goed", font=knop_font, width=10, height=2,
                           command=lambda: self.laat_goed_zien(root))
        goed_knop.place(relx=0.45, rely=0.4, anchor="s")

        slecht_knop = Button(root, bg=knop_achtergrond_kleur, text="Slecht", font=knop_font, width=10, height=2,
                             command=lambda: self.laat_slecht_zien(root))
        slecht_knop.place(relx=0.55, rely=0.4, anchor="s")

        terug_knop = Button(root, bg=knop_achtergrond_kleur, text="Terug", font=knop_font, width=10, height=2,
                            command=lambda: self.naar_admin_menu(root))
        terug_knop.place(relx=1, rely=1, anchor="se")

    def naar_admin_menu(self, root):
        from admin import admin_laat_pagina_zien
        admin_laat_pagina_zien(root)

    def laat_goed_zien(self, root):
        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] == self.eindes['goed']:
                widget.destroy()

        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] in self.eindes["slecht"]:
                widget.destroy()
        label_font = Font(family="Aniron", size=16)
        achtergrond_plaatje_laden(root)
        goed_label_origineel = Label(root, text=self.eindes["goed"], wraplength=500, font=label_font, bg="grey")
        goed_label_origineel.place(relx=0.5, rely=0.6, anchor="s")

        goed_label_directie = Label(root, text="Oost leidt je naar het goede pad!", wraplength=500, font=label_font, bg="grey")
        goed_label_directie.place(relx=0.5, rely=0.65, anchor="s")

    def laat_slecht_zien(self, root):
        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] == self.eindes['slecht']:
                widget.destroy()

        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] in self.eindes["goed"]:
                widget.destroy()
        label_font = Font(family="Aniron", size=16)
        achtergrond_plaatje_laden(root)
        slecht_label_origineel = Label(root, text=self.eindes["slecht"], wraplength=500, font=label_font, bg="grey")
        slecht_label_origineel.place(relx=0.5, rely=0.6, anchor="s")

        slecht_label_directie = Label(root, text="West leidt je naar het slechte pad!", wraplength=500, font=label_font, bg="grey")
        slecht_label_directie.place(relx=0.5, rely=0.65, anchor="s")


class Verhaal2:
    def __init__(self):
        self.eindes = {}

    def laat_admin_verhaal_zien(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        achtergrond_plaatje_laden(root)

        bestand = open('bestanden/scenario_twee.json', 'r')
        bestand_informatie = json.load(bestand)
        bestand.close()

        self.eindes = {
            "goed": bestand_informatie['goed_einde']['text'],
            "slecht1": bestand_informatie['eerste_slechte_eind']['text'],
            "slecht2": bestand_informatie['tweede_slechte_einde']['text'],
        }

        titel_font = Font(family="Aniron", size=24, weight="bold")
        titel_label = Label(text="Admin menu", bg="grey", font=titel_font)
        titel_label.place(relx=0.5, rely=0.05, anchor="center")

        knop_font = Font(family="Aniron", size=16)

        goed_knop = Button(root, bg=knop_achtergrond_kleur, text="Goed", font=knop_font, width=10, height=2,
                           command=lambda: self.laat_goed_zien(root))
        goed_knop.place(relx=0.4, rely=0.4, anchor="s")

        slecht1_knop = Button(root, bg=knop_achtergrond_kleur, text="Slecht1", font=knop_font, width=10, height=2,
                              command=lambda: self.laat_slecht1_zien(root))
        slecht1_knop.place(relx=0.5, rely=0.4, anchor="s")
        slecht2_knop = Button(root, bg=knop_achtergrond_kleur, text="Slecht2", font=knop_font, width=10, height=2,
                              command=lambda: self.laat_slecht2_zien(root))
        slecht2_knop.place(relx=0.6, rely=0.4, anchor="s")

        terug_knop = Button(root, bg=knop_achtergrond_kleur, text="Terug", font=knop_font, width=10, height=2,
                            command=lambda: self.naar_admin_menu(root))
        terug_knop.place(relx=1, rely=1, anchor="se")

    def naar_admin_menu(self, root):
        from admin import admin_laat_pagina_zien
        admin_laat_pagina_zien(root)

    def laat_goed_zien(self, root):
        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] == self.eindes['goed']:
                widget.destroy()

        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] in [self.eindes["slecht1"], self.eindes["slecht2"]]:
                widget.destroy()
        label_font = Font(family="Aniron", size=16)
        achtergrond_plaatje_laden(root)
        goed_label_origineel = Label(root, text=self.eindes["goed"], wraplength=500, bg="grey", font=label_font)
        goed_label_origineel.place(relx=0.5, rely=0.65, anchor="s")

        goed_label_directie = Label(root, text="De weg vragen laat je uiteindelijk eindigen bij het goede einde!",
                                    wraplength=500, bg="grey", font=label_font)
        goed_label_directie.place(relx=0.5, rely=0.75, anchor="s")
        self.goed_label_directie = goed_label_directie

        if hasattr(self, 'slecht_label_directie1'):
            self.slecht_label_directie1.destroy()
            del self.slecht_label_directie1
        else:
            pass

        if hasattr(self, 'slecht_label_directie2'):
            self.slecht_label_directie2.destroy()
            del self.slecht_label_directie2
        else:
            pass

    def laat_slecht1_zien(self, root):
        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] == self.eindes['slecht1']:
                widget.destroy()

        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] in [self.eindes["goed"], self.eindes["slecht2"]]:
                widget.destroy()
        label_font = Font(family="Aniron", size=16)
        achtergrond_plaatje_laden(root)
        slecht_label_origineel1 = Label(root, text=self.eindes["slecht1"], wraplength=500, bg="grey", font=label_font)
        slecht_label_origineel1.place(relx=0.5, rely=0.6, anchor="s")

        slecht_label_directie1 = Label(root,
                                       text="Je verstopt je of vlucht leiden beide naar het eerste slechte einde.",
                                       wraplength=500, bg="grey", font=label_font)
        slecht_label_directie1.place(relx=0.5, rely=0.7, anchor="s")
        self.slecht_label_directie1 = slecht_label_directie1

        if hasattr(self, 'goed_label_directie'):
            self.goed_label_directie.destroy()
            del self.goed_label_directie
        else:
            pass

        if hasattr(self, 'slecht_label_directie2'):
            self.slecht_label_directie2.destroy()
            del self.slecht_label_directie2
        else:
            pass

    def laat_slecht2_zien(self, root):
        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] == self.eindes['slecht2']:
                widget.destroy()

        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] in [self.eindes["goed"], self.eindes["slecht1"]]:
                widget.destroy()
        label_font = Font(family="Aniron", size=16)
        achtergrond_plaatje_laden(root)
        slecht_label_origineel2 = Label(root, text=self.eindes["slecht2"], wraplength=500, bg="grey", font=label_font)
        slecht_label_origineel2.place(relx=0.5, rely=0.6, anchor="s")

        slecht_label_directie2 = Label(root, text="West leidt je naar het slechte pad!", wraplength=500, bg="grey", font=label_font)
        slecht_label_directie2.place(relx=0.5, rely=0.65, anchor="s")
        self.slecht_label_directie2 = slecht_label_directie2

        if hasattr(self, 'goed_label_directie'):
            self.goed_label_directie.destroy()
            del self.goed_label_directie
        else:
            pass

        if hasattr(self, 'slecht_label_directie1'):
            self.slecht_label_directie1.destroy()
            del self.slecht_label_directie1
        else:
            pass


class Verhaal3:
    def __init__(self):
        self.eindes = {}

    def laat_admin_verhaal_zien(self, root):

        for widget in root.winfo_children():
            widget.destroy()

        achtergrond_plaatje_laden(root)

        bestand = open('bestanden/scenario_drie.json', 'r')
        bestand_informatie = json.load(bestand)
        bestand.close()

        self.eindes = {
            "goed": bestand_informatie['goed_einde']['text'],
            "slecht": bestand_informatie['slecht_eind_deel_een']['text'],
        }

        titel_font = Font(family="Aniron", size=24, weight="bold")
        titel_label = Label(text="Admin menu", bg="grey", font=titel_font)

        titel_label.place(relx=0.5, rely=0.05, anchor="center")

        knop_font = Font(family="Aniron", size=16)

        goed_knop = Button(root, bg=knop_achtergrond_kleur, text="Goed", font=knop_font, width=10, height=2,
                           command=lambda: self.laat_goed_zien(root))
        goed_knop.place(relx=0.45, rely=0.5, anchor="s")

        slecht_knop = Button(root, bg=knop_achtergrond_kleur, text="Slecht", font=knop_font, width=10, height=2,
                             command=lambda: self.laat_slecht_zien(root))
        slecht_knop.place(relx=0.55, rely=0.5, anchor="s")

        terug_knop = Button(root, bg=knop_achtergrond_kleur, text="Terug", font=knop_font, width=10, height=2,
                            command=lambda: self.naar_admin_menu(root))
        terug_knop.place(relx=1, rely=1, anchor="se")

    def naar_admin_menu(self, root):
        from admin import admin_laat_pagina_zien
        admin_laat_pagina_zien(root)

    def laat_goed_zien(self, root):
        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] == self.eindes['goed']:
                widget.destroy()

        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] in self.eindes["slecht"]:
                widget.destroy()
        label_font = Font(family="Aniron", size=16)
        achtergrond_plaatje_laden(root)
        goed_label_origineel = Label(root, text=self.eindes["goed"], wraplength=500, bg="grey", font=label_font)
        goed_label_origineel.place(relx=0.5, rely=0.6, anchor="s")

        goed_label_directie = Label(root, text="Door weg te lopen met Sam kom je bij het goede einde!", wraplength=500, bg="grey", font=label_font)
        goed_label_directie.place(relx=0.5, rely=0.7, anchor="s")
        self.goed_label_directie = goed_label_directie

        if hasattr(self, 'slecht_label_directie'):
            self.slecht_label_directie.destroy()
            self.slecht_label2_directie.destroy()
            del self.slecht_label_directie
            del self.slecht_label2_directie
        else:
            pass

    def laat_slecht_zien(self, root):
        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] == self.eindes['slecht']:
                widget.place_forget()

        for widget in root.winfo_children():
            if isinstance(widget, Label) and widget["text"] in self.eindes["goed"]:
                widget.place_forget()
        label_font = Font(family="Aniron", size=16)
        achtergrond_plaatje_laden(root)
        slecht_label_origineel = Label(root, text=self.eindes["slecht"], wraplength=500, bg="grey", font=label_font)
        slecht_label_origineel.place(relx=0.5, rely=0.75, anchor="s")

        slecht_label_directie = Label(root, text="Door de oude vrouw aan te spreken kom je bij het slechte einde!",
                                      wraplength=500, bg="grey", font=label_font)
        slecht_label_directie.place(relx=0.5, rely=0.85, anchor="s")
        slecht_label2_directie = Label(root, text="Je negeert haar", wraplength=500, bg="grey", font=label_font)
        slecht_label2_directie.place(relx=0.5, rely=0.9, anchor="s")
        self.slecht_label_directie = slecht_label_directie
        self.slecht_label2_directie = slecht_label2_directie

        if hasattr(self, 'goed_label_directie'):
            self.goed_label_directie.destroy()
            del self.goed_label_directie
        else:
            pass
