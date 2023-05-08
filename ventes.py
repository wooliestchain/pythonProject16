import uuid
import psycopg2
from datetime import datetime
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="wool",
    user="root",
    password=""
)
# Créer un curseur
cur = conn.cursor()

# Création de la table "sales"
cur.execute("""
    CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    amount FLOAT NOT NULL,
    quantity INTEGER NOT NULL,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
    );
""")

# Insertion d'un exemple de données
now = datetime.now()
year = now.year
month = now.month
day = now.day


def add_sale_to_database(produit, montant, quantite, now=datetime.now(), year=now.year, month=now.month, day=now.day):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sales (product_name, amount, quantity, year, month, day)
        VALUES (%s, %s, %s, %s, %s, %s);
        """, (produit, montant, quantite, year, month, day))
        conn.commit()
        print("Vente ajoutée avec succès!")
    except mysql.connector.Error as e:
        print("Une erreur s'est produite lors de l'ajout dans la base:", e)



def get_sales_by_product(produit):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT COUNT(*) FROM sales WHERE product_name=%s', (produit,)
        )
        rows = cursor.fetchone()[0]
        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")





#obtenir le nombre de ventes pour un mois
def get_total_sales_by_month_for_all_product(mois):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT ROUND(SUM(amount*quantity),2) as recettes FROM sales WHERE month= %s ', (mois,)
        )
        rows = cursor.fetchone()[0]
        return rows

    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce mois:")


#obtenir le nombre de ventes pour un mois pour un produit
def get_total_sales_by_month_for_a_product(produit,mois):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM sales WHERE month= %s and product_name = %s ", (mois, produit,)
        )
        rows = cursor.fetchone()[0]
        return rows

    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce mois:")


cur.close()
conn.close()