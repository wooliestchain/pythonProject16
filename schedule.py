import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calendrier")

# Création du widget Frame pour le tableau
table_frame = ttk.Frame(root, borderwidth=2, relief="groove")
table_frame.pack(padx=10, pady=10)

# Définition des titres des colonnes
titles = ["Faculté", "Cours", "Sujet", "Salle", "Jour", "Heure de début", "Heure de fin", "Utilisateur"]

# Création des titres des colonnes
for i, title in enumerate(titles):
    col_title = ttk.Label(table_frame, text=title, font=("Helvetica", 12, "bold"), background="#f0f0f0", width=15, anchor="center")
    col_title.grid(row=0, column=i+1, padx=2, pady=2, sticky="nsew")
    table_frame.columnconfigure(i+1, weight=1)

# Définition des données de la table
data = [
    ["Faculté A", "Cours A", "Sujet A", "Salle A", "Lundi", "08:00", "10:00", "Utilisateur A"],
    ["Faculté B", "Cours B", "Sujet B", "Salle B", "Mardi", "11:00", "13:00", "Utilisateur B"],
    ["Faculté C", "Cours C", "Sujet C", "Salle C", "Mercredi", "14:00", "16:00", "Utilisateur C"],
    ["Faculté D", "Cours D", "Sujet D", "Salle D", "Jeudi", "17:00", "19:00", "Utilisateur D"]
]

# Création des données de la table
for i, row in enumerate(data):
    # Numéro de la ligne
    row_number = i + 1

    # Création de l'étiquette pour le numéro de la ligne
    row_label = ttk.Label(table_frame, text=row_number, font=("Helvetica", 12), background="#f0f0f0", width=5, anchor="center")
    row_label.grid(row=row_number, column=0, padx=2, pady=2, sticky="nsew")

    # Création des cellules de la ligne
    for j, cell_value in enumerate(row):
        cell = ttk.Label(table_frame, text=cell_value, font=("Helvetica", 12), background="white", width=15, anchor="center")
        cell.grid(row=row_number, column=j+1, padx=2, pady=2, sticky="nsew")

# Redimensionnement des colonnes
for i in range(len(titles)+1):
    table_frame.columnconfigure(i, weight=1)

root.mainloop()
