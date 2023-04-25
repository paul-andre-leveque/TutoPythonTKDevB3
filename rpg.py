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
        self.stats_vars = {stat: IntVar() for stat in characters['Chevalier'].keys()}

        character_choice = ttk.Combobox(mainframe, width=15, textvariable=self.selected_character)
        character_choice['values'] = tuple(characters.keys())
        character_choice.grid(column=1, row=1, sticky=(W, E))
        character_choice.current(0)
        character_choice.bind("<<ComboboxSelected>>", self.update_stat_spinboxes)

        ttk.Label(mainframe, text="Personnage").grid(column=1, row=2, sticky=W)

        self.stat_spinboxes = {}
        for idx, stat in enumerate(characters['Chevalier'].keys()):
            ttk.Label(mainframe, text=stat).grid(column=4, row=idx+1, sticky=W)
            spinbox = Spinbox(mainframe, from_=0, to=30, textvariable=self.stats_vars[stat], width=3, command=self.validate_stats)
            spinbox.grid(column=5, row=idx+1, sticky=(W, E))
            self.stat_spinboxes[stat] = spinbox

        self.points_left = IntVar()
        self.points_left.set(45)
        ttk.Label(mainframe, text="Points restants : ").grid(column=6, row=1, sticky=W)
        ttk.Label(mainframe, textvariable=self.points_left).grid(column=7, row=1, sticky=W)

        ttk.Button(mainframe, text="Random stat", command=self.randomize_stats).grid(column=7, row=4, sticky=W)

        self.update_stat_spinboxes()

    def update_stat_spinboxes(self, event=None):
        character_name = self.selected_character.get()
        stats = characters[character_name]
        for stat in stats:
            self.stats_vars[stat].set(stats[stat])

    def validate_stats(self):
        total_points = sum(self.stats_vars[stat].get() for stat in self.stats_vars)
        if total_points > 45:
            for stat in self.stats_vars:
                self.stats_vars[stat].set(characters[self.selected_character.get()][stat])
        else:
            characters_name = self.selected_character.get()
            for stat in self.stats_vars:
                characters[characters_name][stat] = self.stats_vars[stat].get()
            self.points_left.set(45 - total_points)


    def randomize_stats(self):
        remaining_points = 45
        character_name = self.selected_character.get()
        for stat in self.stats_vars:
            random_value = random.randint(0, remaining_points)
            self.stats_vars[stat].set(random_value)
            characters[character_name][stat] = random_value
            remaining_points -= random_value
        self.points_left.set(remaining_points)

root = Tk()
CharacterSelector(root)
root.mainloop()
