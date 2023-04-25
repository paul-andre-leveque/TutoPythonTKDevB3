from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(amount.get())
        if conversion_type.get() == "Euros en Dollars":
            conversion_rate = 1.1  # Remplacez cette valeur par le taux de change actuel.
            result.set(round(value * conversion_rate, 2))
        elif conversion_type.get() == "Dollars en Euros":
            conversion_rate = 1 / 1.1  # Remplacez cette valeur par le taux de change actuel.
            result.set(round(value * conversion_rate, 2))
    except ValueError:
        pass

root = Tk()
root.title("Convertisseur de devises")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

amount = StringVar()
amount_entry = ttk.Entry(mainframe, width=7, textvariable=amount)
amount_entry.grid(column=2, row=1, sticky=(W, E))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculaler", command=calculate).grid(column=3, row=3, sticky=W)

conversion_type = StringVar()
conversion_choice = ttk.Combobox(mainframe, width=15, textvariable=conversion_type)
conversion_choice['values'] = ('Euros en Dollars', 'Dollars en Euros')
conversion_choice.grid(column=1, row=1, sticky=(W, E))
conversion_choice.current(0)

ttk.Label(mainframe, text="Montant").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Résultat").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

amount_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
