import tkinter as tk
from suds.client import Client
from datetime import datetime

def add_sale():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    client = Client('http://localhost:8000/?wsdl')
    result = client.service.add_sale(produit_entry.get(), montant_entry.get(), quantite_entry.get(), now, year, month, day)
    result_label.config(text=result)

# Créer la fenêtre tkinter
root = tk.Tk()
root.title("Ajouter une vente")

# Créer les widgets
produit_label = tk.Label(root, text="Produit : ")
produit_entry = tk.Entry(root)
montant_label = tk.Label(root, text="Montant : ")
montant_entry = tk.Entry(root)
quantite_label = tk.Label(root, text="Quantité : ")
quantite_entry = tk.Entry(root)
ajouter_button = tk.Button(root, text="Ajouter", command=add_sale)
result_label = tk.Label(root, text="")

# Placer les widgets dans la fenêtre
produit_label.grid(row=0, column=0)
produit_entry.grid(row=0, column=1)
montant_label.grid(row=1, column=0)
montant_entry.grid(row=1, column=1)
quantite_label.grid(row=2, column=0)
quantite_entry.grid(row=2, column=1)
ajouter_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

# Lancer la boucle principale tkinter
root.mainloop()
