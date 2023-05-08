import tkinter as tk
from suds.client import Client
from datetime import datetime

class VentesApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Ajouter une vente")
        self.master.geometry("400x300")
        self.master.configure(background='#F5F5F5')
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Produit : ", font=("Helvetica", 14), pady=10, padx=10, bg='#F5F5F5').grid(row=0, column=0)
        self.produit_entry = tk.Entry(self.master, width=30, font=("Helvetica", 14))
        self.produit_entry.grid(row=0, column=1, pady=10, padx=10)

        tk.Label(self.master, text="Montant : ", font=("Helvetica", 14), pady=10, padx=10, bg='#F5F5F5').grid(row=1, column=0)
        self.montant_entry = tk.Entry(self.master, width=30, font=("Helvetica", 14))
        self.montant_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(self.master, text="Quantité : ", font=("Helvetica", 14), pady=10, padx=10, bg='#F5F5F5').grid(row=2, column=0)
        self.quantite_entry = tk.Entry(self.master, width=30, font=("Helvetica", 14))
        self.quantite_entry.grid(row=2, column=1, pady=10, padx=10)

        tk.Button(self.master, text="Ajouter la vente", command=self.add_sale, font=("Helvetica", 14), bg='#4285F4', fg='#FFFFFF').grid(row=3, column=1, pady=10, padx=10)

    def add_sale(self):
        produit = self.produit_entry.get()
        montant = self.montant_entry.get()
        quantite = self.quantite_entry.get()

        client = Client('http://localhost:8000/?wsdl')
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        result = client.service.add_sale(produit, montant, quantite, now, year, month, day)
        print(result)

root = tk.Tk()
app = VentesApp(root)
app.mainloop()
