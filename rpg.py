import random
from tkinter import *
from tkinter import ttk

characters = {
    'Chevalier': {'Force': 15, 'Agilité': 10, 'Intelligence': 7, 'Endurance': 14},
    'Magicien': {'Force': 5, 'Agilité': 8, 'Intelligence': 17, 'Endurance': 9},
    'Voleur': {'Force': 10, 'Agilité': 15, 'Intelligence': 9, 'Endurance': 11},
    'Archer': {'Force': 12, 'Agilité': 14, 'Intelligence': 8, 'Endurance': 12},
    'Druide': {'Force': 8, 'Agilité': 10, 'Intelligence': 15, 'Endurance': 10},
    'Paladin': {'Force': 13, 'Agilité': 9, 'Intelligence': 12, 'Endurance': 14}
}

class CharacterSelector:
    def __init__(self, root):
        root.title("Sélection de personnage")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.selected_character = StringVar()
        self.character_stats = StringVar()

        character_choice = ttk.Combobox(mainframe, width=15, textvariable=self.selected_character)
        character_choice['values'] = tuple(characters.keys())
        character_choice.grid(column=1, row=1, sticky=(W, E))
        character_choice.current(0)

        ttk.Label(mainframe, text="Personnage").grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text="Statistiques").grid(column=2, row=2, sticky=W)

        stats_label = ttk.Label(mainframe, textvariable=self.character_stats)
        stats_label.grid(column=2, row=1, sticky=(W, E))

        ttk.Button(mainframe, text="Afficher les statistiques", command=self.display_stats).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text="Randomiser les statistiques", command=self.randomize_stats).grid(column=4, row=3, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def display_stats(self):
        character_name = self.selected_character.get()
        stats = characters[character_name]
        stats_text = "\n".join(f"{stat}: {value}" for stat, value in stats.items())
        self.character_stats.set(stats_text)

    def randomize_stats(self):
        for character in characters:
            for stat in characters[character]:
                characters[character][stat] = random.randint(1, 20)
        self.display_stats()


root = Tk()
CharacterSelector(root)
root.mainloop()
