from tkinter import *
from tkinter import ttk

def calculer(*args):
    try:
        valeur = float(montant.get())
        if conversion.get() == "Euros en Dollars":
            taux_conversion = 1.1  # Remplacez cette valeur par le taux de change actuel.
            resultat.set(round(valeur * taux_conversion, 2))
        elif conversion.get() == "Dollars en Euros":
            taux_conversion = 1 / 0.9  # Remplacez cette valeur par le taux de change actuel.
            resultat.set(round(valeur * taux_conversion, 2))
    except ValueError:
        pass

racine = Tk()
racine.title("Convertisseur de devises")

cadre_principal = ttk.Frame(racine, padding="3 3 12 12")
cadre_principal.grid(column=0, row=0, sticky=(N, W, E, S))
racine.columnconfigure(0, weight=1)
racine.rowconfigure(0, weight=1)

montant = StringVar()
saisie_montant = ttk.Entry(cadre_principal, width=7, textvariable=montant)
saisie_montant.grid(column=2, row=1, sticky=(W, E))

resultat = StringVar()
ttk.Label(cadre_principal, textvariable=resultat).grid(column=2, row=2, sticky=(W, E))

ttk.Button(cadre_principal, text="Calculer", command=calculer).grid(column=3, row=3, sticky=W)

conversion = StringVar()
choix_conversion = ttk.Combobox(cadre_principal, width=15, textvariable=conversion)
choix_conversion['values'] = ('Euros en Dollars', 'Dollars en Euros')
choix_conversion.grid(column=1, row=1, sticky=(W, E))
choix_conversion.current(0)

ttk.Label(cadre_principal, text="Montant").grid(column=1, row=1, sticky=W)
ttk.Label(cadre_principal, text="Résultat").grid(column=1, row=2, sticky=E)

for enfant in cadre_principal.winfo_children():
    enfant.grid_configure(padx=5, pady=5)

saisie_montant.focus()
racine.bind("<Return>", calculer)

racine.mainloop()