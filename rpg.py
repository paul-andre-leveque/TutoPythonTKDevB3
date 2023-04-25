import random
from tkinter import *
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

characters = {
    'Chevalier': {'Force': 15, 'Agilité': 10, 'Intelligence': 7, 'Endurance': 14, 'Histoire': ''},
    'Magicien': {'Force': 5, 'Agilité': 8, 'Intelligence': 17, 'Endurance': 9, 'Histoire': ''},
    'Voleur': {'Force': 10, 'Agilité': 15, 'Intelligence': 9, 'Endurance': 11, 'Histoire': ''},
    'Archer': {'Force': 12, 'Agilité': 14, 'Intelligence': 8, 'Endurance': 12, 'Histoire': ''},
    'Druide': {'Force': 8, 'Agilité': 10, 'Intelligence': 15, 'Endurance': 10, 'Histoire': ''},
    'Paladin': {'Force': 13, 'Agilité': 9, 'Intelligence': 12, 'Endurance': 14, 'Histoire': ''}
}

class CharacterSelector:
    def __init__(self, root):
        root.title("Sélection de personnage")

        # ajout de style avec la commande pip install ttkthemes
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="#f0f0f0", foreground="#3a3a3a")
        style.configure("TButton", font=("Arial", 12), relief=SUNKEN, padding=(5, 5))
        style.configure("TLabelFrame", font=("Arial", 14, "bold"), background="#f0f0f0", foreground="#3a3a3a",padding=(10, 10), relief=SUNKEN)
        style.configure("TFrame", background="#f0f0f0")

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Selection Personage
        character_frame = ttk.LabelFrame(mainframe, text="Personnage", padding="10 10 10 10")
        character_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.selected_character = StringVar()
        character_choice = ttk.Combobox(character_frame, width=15, textvariable=self.selected_character)
        character_choice['values'] = tuple(characters.keys())
        character_choice.grid(column=0, row=0, padx=5, pady=5)
        character_choice.current(0)
        character_choice.bind("<<ComboboxSelected>>", self.update_stat_spinboxes)


        stats_frame = ttk.LabelFrame(mainframe, text="Statistiques", padding="10 10 10 10")
        stats_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.stats_vars = {stat: IntVar() for stat in characters['Chevalier'].keys() if stat != 'Histoire'}

        #Barre de progression
        self.progress = ttk.Progressbar(mainframe, orient=HORIZONTAL, length=200, mode='determinate', maximum=100,value=0)
        self.progress.grid(column=1, row=5, columnspan=4, pady=10)


        self.stat_spinboxes = {}
        for idx, stat in enumerate(characters['Chevalier'].keys()):
            if stat != 'Histoire':
                ttk.Label(stats_frame, text=stat).grid(column=0, row=idx, sticky=W, padx=5, pady=5)
                spinbox = Spinbox(stats_frame, from_=0, to=30, textvariable=self.stats_vars[stat], width=3, command=self.validate_stats)
                spinbox.grid(column=1, row=idx, sticky=(W, E), padx=5, pady=5)
                self.stat_spinboxes[stat] = spinbox

        self.points_left = IntVar()
        self.points_left.set(44)
        ttk.Label(stats_frame, text="Points restants : ").grid(column=0, row=5, sticky=W, padx=5, pady=5)
        ttk.Label(stats_frame, textvariable=self.points_left).grid(column=1, row=5, sticky=W, padx=5, pady=5)
        ttk.Button(stats_frame, text="Random stat", command=self.randomize_stats).grid(column=0, row=6,columnspan=2, sticky=(W, E),padx=5, pady=5)

        # Editeur D'histoire
        story_frame = ttk.LabelFrame(mainframe, text="Histoire", padding="10 10 10 10")
        story_frame.grid(column=0, row=1, columnspan=2, sticky=(N, W, E, S))

        self.story_text = Text(story_frame, wrap=WORD, width=40, height=10)
        self.story_text.grid(column=0, row=0, padx=5, pady=5)

        ttk.Button(story_frame, text="Sauvegarder l'histoire", command=self.save_story).grid(column=0, row=1,sticky=(W, E), padx=5,pady=5)
        ttk.Button(story_frame, text="Combattre un monstre", command=self.start_battle).grid(column=0, row=2, sticky=(W, E), padx=5, pady=5)
        self.update_stat_spinboxes()

    def update_stat_spinboxes(self, event=None):
        character_name = self.selected_character.get()
        stats = characters[character_name]
        for stat in stats:
            if stat != 'Histoire':
                self.stats_vars[stat].set(stats[stat])
        self.story_text.delete(1.0, END)
        self.story_text.insert(INSERT, characters[character_name]['Histoire'])

    def validate_stats(self):
        total_points = sum(self.stats_vars[stat].get() for stat in self.stats_vars)
        if total_points > 44:
            for stat in self.stats_vars:
                self.stats_vars[stat].set(characters[self.selected_character.get()][stat])
        else:
            character_name = self.selected_character.get()
            for stat in self.stats_vars:
                characters[character_name][stat] = self.stats_vars[stat].get()
            self.points_left.set(44 - total_points)

    def randomize_stats(self):
        remaining_points = 44
        character_name = self.selected_character.get()
        for stat in self.stats_vars:
            random_value = random.randint(0, remaining_points)
            self.stats_vars[stat].set(random_value)
            characters[character_name][stat] = random_value
            remaining_points -= random_value
        self.points_left.set(remaining_points)

    def save_story(self):
        character_name = self.selected_character.get()
        characters[character_name]['Histoire'] = self.story_text.get(1.0, END).strip()

    def start_battle(self):
        character_name = self.selected_character.get()
        character_stats = characters[character_name]

        monster = self.generate_monster()

        battle_result = self.battle(character_name,character_stats, monster)

        messagebox.showinfo("Résultat du combat", battle_result)

        current_value = self.progress["value"]
        if character_name in battle_result:
            new_value = min(current_value + 10, 100)  # augmenter la barre de progression de 10, jusqu'à un maximum de 100
            self.progress["value"] = new_value
            if new_value == 100:
                messagebox.showinfo("Gagné", "Félicitations ! Vous avez gagné !")
        else:
            new_value = max(current_value - 10, 0)  # diminuer la barre de progression de 10, jusqu'à un minimum de 0
            self.progress["value"] = new_value
            if new_value == 0:
                messagebox.showinfo("Perdu", "Vous avez perdu. Essayez à nouveau !")


    def generate_monster(self):
            monster_stats = {
                "Force": random.randint(1, 30),
                "Agilité": random.randint(1, 30),
                "Intelligence": random.randint(1, 30),
                "Endurance": random.randint(1, 30)
            }
            return monster_stats

    def battle(self, character_name, character_stats, monster_stats):
        # implemente la logique du combat
        # Compare la des stats du personnage et du monstre
        character_power = sum(character_stats[stat] for stat in character_stats if stat != 'Histoire')
        monster_power = sum(monster_stats.values())

        if character_power > monster_power:
            return f"{character_name} a gagné le combat contre le monstre!"
        elif character_power < monster_power:
            return f"{character_name} a perdu le combat contre le monstre."
        else:
            return f"{character_name} et le monstre ont fait match nul."


root = ThemedTk(theme="arc")
root.configure(background="#f0f0f0")
CharacterSelector(root)
root.mainloop()