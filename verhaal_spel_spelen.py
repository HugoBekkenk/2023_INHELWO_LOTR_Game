import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import json
import pygame
from kies_karakter_menu import plaatjes_formateren
from kies_naam import schrijf_karakter_weg
from random import randint


def spel_starten(root_scherm, karakter, json_bestand_naam, muziek_bestand_naam):
    karakter_plaatje_naam = None
    monster_stats = None
    speciale_aanval_bruikbaar = 1
    speciale_aanval_bruikbaar_text = "(" + str(speciale_aanval_bruikbaar) + "x bruikbaar)"
    if karakter["ras"] == "elf":
        speciale_aanval = ["Elf: Schiet je boog op het monster", "Je pakt je grote oorlogs boog en trekt hem zo ver mogelijk naar achteren en raakt het monster in zijn hoofd, je doet grote schade"]
        if karakter["naam"] == "Legolas":
            karakter_plaatje_naam = "bestanden/Legolaspixel_grey_background.png"
        else:
            karakter_plaatje_naam = "bestanden/pixelelf_grey_background.png"
    elif karakter["ras"] == "dwerg":
        speciale_aanval = ["Dwerg: Sla het monster met je hamer", "Je springt in de lucht een met een harde slag val je het monster aan met je grote hamer, je doet grote schade"]
        karakter_plaatje_naam = "bestanden/pixeldwarf_grey_background.png"
    elif karakter["ras"] == "hobbit":
        speciale_aanval = ["Hobbit: Sluip en val het monster aan van achteren", "Je kruipt in de schaduw achter het monster en steekt hem in de rug, je doet grote schade"]
        karakter_plaatje_naam = "bestanden/pixelhobbit_grey_background.png"
    elif karakter["ras"] == "mens":
        speciale_aanval = ["Mens: Ren dapper op de vijand af", "Je rent op het monster af en drijft je zwaard diep in het monster, je doet grote schade"]
        karakter_plaatje_naam = "bestanden/mens_grey_background.png"

    knoppen = []
    for widget in root_scherm.winfo_children():
        widget.destroy()

    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(muziek_bestand_naam)
    pygame.mixer.music.play(-1)

    def ga_naar_hoofdmenu(root):
        from hoofdmenu import maak_hoofdmenu_aan
        maak_hoofdmenu_aan(root)

    game_status = {
        "current_scene": "start",
        "points": 0,
        "ras": karakter["ras"],
    }
    with open(json_bestand_naam, "r") as json_file:
        scenes = json.load(json_file)

    achtergrond_fotos = {
        scene_naam: ImageTk.PhotoImage(
            Image.open(scene_data["background_image"])
        )
        for scene_naam, scene_data in scenes.items()
        if "background_image" in scene_data
    }


    def maak_leven_labels(monster_stats, karakter):
        monster_levens_label = tk.Label(text="Levens " + monster_stats["naam"] + ": " + str(monster_stats["levens"]),
                                        font=("Arial", 22), fg="red", bg="grey", anchor="w")
        monster_levens_label.place(relx=0.8, rely=0.1, anchor="w")
        karakter_levens_label = tk.Label(text="Levens " + karakter["naam"] + ": " + str(karakter["levens"]),
                                         font=("Arial", 22), fg="red", bg="grey", anchor="w")
        karakter_levens_label.place(relx=0.8, rely=0.2, anchor="w")


    def verwijder_leven_labels():
        monster_levens_label = tk.Label(bg="grey", width=50, height=22)
        monster_levens_label.place(relx=0.8, rely=0, anchor="nw")
        # karakter_levens_label = tk.Label(bg="grey", width=50, height=2)
        # karakter_levens_label.place(relx=0.8, rely=0.2, anchor="w")


    def maak_random_getal():
        random_getal = randint(1, 20)
        if random_getal < 10:
            random_getal_vermenigvuldiger = 0.5 + (random_getal / 20)
        else:
            random_getal_vermenigvuldiger = random_getal / 10
        return random_getal_vermenigvuldiger, random_getal

    def maak_dobbelsteen_label(random_getal):
        dobesteen_label = tk.Label(text="Rolt D20: \n" + str(random_getal),
                                        font=("Arial", 22), fg="red", bg="grey", anchor="center")
        dobesteen_label.place(relx=0.9, rely=0.3, anchor="center")



    def verander_scene(volgende_scene, punten, muziek_bestand_naam, monster_stats, speciale_aanval_bruikbaar):
        game_status["points"] += punten
        # if game_status["current_scene"] == "begin_mijnen" and game_status["ras"] == "dwerg":
        #     volgende_scene = "dwerg_is_gaaf"
        if game_status["current_scene"] == "nieuw_persoon" and game_status["ras"] == "elf":
            volgende_scene = "elf_is_gaaf"
        elif game_status["current_scene"] == "slecht_einde_deel_een" and game_status["ras"] == "mens":
            volgende_scene = "slecht_einde_deel_een_mens"
        elif game_status["current_scene"] == "rusten_deel_een" and game_status["ras"] == "hobbit":
            volgende_scene = "hobbit_is_gaaf"
        elif game_status["current_scene"] == "rusten" and game_status["ras"] == "hobbit":
            volgende_scene = "rusten_hobbit"

        elif game_status["current_scene"] == "quit1":
            karakter["einde1"] = "wel"
            schrijf_karakter_weg(karakter)
            ga_naar_hoofdmenu(root_scherm)
            pygame.mixer.music.stop()

        elif game_status["current_scene"] == "quit2":
            karakter["einde2"] = "wel"
            schrijf_karakter_weg(karakter)
            ga_naar_hoofdmenu(root_scherm)
            pygame.mixer.music.stop()

        elif game_status["current_scene"] == "quit3":
            karakter["einde3"] = "wel"
            schrijf_karakter_weg(karakter)
            ga_naar_hoofdmenu(root_scherm)
            pygame.mixer.music.stop()
        scene = scenes[game_status["current_scene"]]
        music_path = scene.get("music")
        if music_path != muziek_bestand_naam:
             muziek_bestand_naam = music_path
             pygame.mixer.music.load(music_path)
             pygame.mixer.music.play(-1)
        if volgende_scene == "gevecht":
            if not monster_stats:
                monster_stats_text = scene.get("monster_stats")
                monster_stats_list = monster_stats_text.split(";")
                monster_stats = {"naam": monster_stats_list[0], "kracht": int(monster_stats_list[1]), "verdediging": int(monster_stats_list[2]), "levens": int(monster_stats_list[3]), "ontdekking": int(monster_stats_list[4])}
            verwijder_leven_labels()
            maak_leven_labels(monster_stats, karakter)
        if game_status["current_scene"] == "gevecht":
            verwijder_leven_labels()
            maak_leven_labels(monster_stats, karakter)
            if karakter["levens"] <= 0:
                verwijder_leven_labels()
                volgende_scene = "gevecht_aanvallen_mislukt"
        if game_status["current_scene"] == "gevecht_aanvallen":
            if karakter["kracht"] > monster_stats["verdediging"]:
                verwijder_leven_labels()
                maak_leven_labels(monster_stats, karakter)
                random_getal = maak_random_getal()
                maak_dobbelsteen_label(random_getal[1])
                schade = int((karakter["kracht"] - monster_stats["verdediging"]) * random_getal[0])
                monster_stats["levens"] -= schade
                schade_monster_label = tk.Label(text="- " + str(schade) + "  ",
                                        font=("Arial", 25), fg="red", bg="grey", anchor="w")
                schade_monster_label.place(relx=1, rely=0.1, anchor="e")
                if monster_stats["levens"] <= 0:
                    verwijder_leven_labels()
                    volgende_scene = "gevecht_monster_verslagen"
            else:
                verwijder_leven_labels()
                volgende_scene = "gevecht_aanvallen_mislukt"
        if game_status["current_scene"] == "gevecht_speciale_aanvallen":
            if speciale_aanval_bruikbaar >= 1:
                verwijder_leven_labels()
                maak_leven_labels(monster_stats, karakter)
                schade = int(karakter["kracht"] / 2)
                monster_stats["levens"] -= schade
                schade_monster_label = tk.Label(text="- " + str(schade) + "  ",
                                                font=("Arial", 22), fg="red", bg="grey", anchor="w")
                schade_monster_label.place(relx=1, rely=0.1, anchor="e")
                if monster_stats["levens"] <= 0:
                    verwijder_leven_labels()
                    volgende_scene = "gevecht_monster_verslagen"
                speciale_aanval_bruikbaar -= 1
                volgende_scene = "gevecht_speciale_aanvallen_gelukt"
            else:
                verwijder_leven_labels()
                maak_leven_labels(monster_stats, karakter)
                volgende_scene = "gevecht_speciale_aanvallen_mislukt"
        if volgende_scene == "gevecht_aangevallen":
            verwijder_leven_labels()
            maak_leven_labels(monster_stats, karakter)
        if game_status["current_scene"] == "gevecht_aangevallen":
            if monster_stats["kracht"] > karakter["verdediging"]:
                random_getal = maak_random_getal()
                maak_dobbelsteen_label(random_getal[1])
                schade_karakter = int((monster_stats["kracht"] - karakter["verdediging"]) * random_getal[0])
                karakter["levens"] -= schade_karakter
                schade_karakter_label = tk.Label(text="- " + str(schade_karakter) + "  ",
                                                font=("Arial", 22), fg="red", bg="grey", anchor="w")
                schade_karakter_label.place(relx=1, rely=0.2, anchor="e")
            else:
                volgende_scene = "gevecht_aangevallen_mislukt"
            if karakter["levens"] <= 0:
                verwijder_leven_labels()
                volgende_scene = "gevecht_aanvallen_mislukt"
        if game_status["current_scene"] == "ontsnappen":
            random_getal = maak_random_getal()
            maak_dobbelsteen_label(random_getal[1])
            sluip_score_karakter = karakter["sluip"] * random_getal[0]
            ontdekking_score_monster = monster_stats["ontdekking"] * maak_random_getal()[0]
            if sluip_score_karakter > ontdekking_score_monster:
                volgende_scene = "ontsnapt"
            else:
                volgende_scene = "gevonden"
        if game_status["current_scene"] == "ontsnapt":
            verwijder_leven_labels()
        if volgende_scene == "level_up":
            karakter["kracht"] += 1
            karakter["verdediging"] += 1
            karakter["sluip"] += 1
            karakter["max_levens"] += 1
            karakter["levens"] = karakter["max_levens"]



        game_status["current_scene"] = volgende_scene
        update_gui(muziek_bestand_naam, monster_stats, speciale_aanval_bruikbaar)

    def update_gui(muziek_bestand_naam, monster_stats, speciale_aanval_bruikbaar):
        speciale_aanval_bruikbaar_text = "(" + str(speciale_aanval_bruikbaar) + "x bruikbaar)"
        label_font = Font(family="Aniron", size=15, weight="bold")
        scene = scenes[game_status["current_scene"]]
        verhaal_tekst.config(text=scene["text"].replace("{naam}", karakter["naam"]).replace("{ras}", karakter["ras"]).replace("{speciale_aanval_text}", speciale_aanval[1]))
        locatie_persoon.config(text="locatie:\n" + scene["plaats"])

        achtergrond_label.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
        achtergrond_label.config(image=achtergrond_fotos[game_status["current_scene"]])

        for knop in knoppen:
            knop.place_forget()

        knoppen.clear()

        for index, optie in enumerate(scene["options"]):
            volgende_scene = optie["next_scene"]
            punten = optie.get("points", 0)

            knop = tk.Button(root_scherm, text=optie["text"].replace("{naam}", karakter["naam"]).replace("{ras}",
                             karakter["ras"]).replace("{speciale_aanval}", speciale_aanval[0]).replace("{bruikbaar}", speciale_aanval_bruikbaar_text), borderwidth=5,
                             font=label_font, background="grey",
                             command=lambda volgende_scene_nieuw=volgende_scene,
                             punten_nieuw=punten: verander_scene(volgende_scene_nieuw, punten_nieuw, muziek_bestand_naam, monster_stats, speciale_aanval_bruikbaar))

            knop.place(relx=0.5, rely=1 - (index * 0.06), anchor="s")

            knoppen.append(knop)
    achtergrond_label = tk.Label()
    achtergrond_label.place(relx=0, rely=0, anchor="nw")

    grijze_rand = tk.Frame(root_scherm, bg="grey")
    grijze_rand.place(relx=1, rely=0, relwidth=0.2, relheight=1, anchor="ne")

    grijze_rand_2 = tk.Frame(root_scherm, bg="grey")
    grijze_rand_2.place(relx=0, rely=0, relwidth=0.2, relheight=1, anchor="nw")

    karakter_plaatje_label = plaatjes_formateren(root_scherm, karakter_plaatje_naam, 400, 400)
    karakter_plaatje_label.place(relx=0, rely=0, relwidth=0.2, anchor="nw")

    statistieken_label = tk.Label(root_scherm, text="Naam: " + karakter["naam"] + "\n\n" + "Ras: " +
                                  karakter["ras"].capitalize() + "\n\n" + "Kracht: " + str(
        karakter["kracht"]) + "\n\n" + "Verdediging: " + str(karakter["verdediging"]) + "\n\n" + "Sluip kracht: " + str(karakter["sluip"])
        + "\n\n" + "Levens: " + str(karakter["levens"]) + "\n\n\n" + "Speciale eigenschap:\n\n" + karakter["eigenschap"], font=("Arial", 15),
                                  wraplength=260, background="grey")
    statistieken_label.place(relx=0, rely=0.4, relwidth=0.2, anchor="nw")

    verhaal_tekst = tk.Label(justify="left", anchor="e", wraplength=260, font=("Arial", 17), bg="grey")
    verhaal_tekst.place(relx=0.9, rely=0.5, anchor="center")

    locatie_persoon = tk.Label(justify="center", anchor="w", font=("Arial", 15), bg="grey", wraplength=260)
    locatie_persoon.place(relx=0.1, rely=1, anchor="s")

    afsluit_knop = tk.Button(root_scherm, text="Hoofdmenu", font=("Arial", 15), bg="grey",
                             command=lambda: ga_naar_hoofdmenu(root_scherm))
    afsluit_knop.place(relx=0, rely=0, relwidth=0.2, anchor="nw")

    update_gui(muziek_bestand_naam, monster_stats, speciale_aanval_bruikbaar)

    root_scherm.mainloop()
