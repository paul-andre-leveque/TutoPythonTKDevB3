from tkinter import *
from tkinter import ttk


class CurrencyConverter:

    def __init__(self, root):

        root.title("Convertisseur de devises")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.amount = StringVar()
        amount_entry = ttk.Entry(mainframe, width=7, textvariable=self.amount)
        amount_entry.grid(column=2, row=1, sticky=(W, E))
        self.result = StringVar()

        ttk.Label(mainframe, textvariable=self.result).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculer", command=self.calculate).grid(column=3, row=3, sticky=W)

        self.conversion_type = StringVar()
        conversion_choice = ttk.Combobox(mainframe, width=15, textvariable=self.conversion_type)
        conversion_choice['values'] = ('Euros en Dollars', 'Dollars en Euros')
        conversion_choice.grid(column=1, row=1, sticky=(W, E))
        conversion_choice.current(0)

        ttk.Label(mainframe, text="Montant").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="Résultat").grid(column=1, row=2, sticky=E)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        amount_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.amount.get())
            if self.conversion_type.get() == "Euros en Dollars":
                conversion_rate = 1.1  # Remplacez cette valeur par le taux de change actuel.
                self.result.set(round(value * conversion_rate, 2))
            elif self.conversion_type.get() == "Dollars en Euros":
                conversion_rate = 1 / 0.9  # Remplacez cette valeur par le taux de change actuel.
                self.result.set(round(value * conversion_rate, 2))
        except ValueError:
            pass


root = Tk()
CurrencyConverter(root)
root.mainloop()
