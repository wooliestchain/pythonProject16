import uuid
import psycopg2
from datetime import datetime
import mysql.connector


now = datetime.now()
year = now.year
month = now.month
day = now.day

#Obtenir la quantité vendue pour un produit
def get_quantity_by_product(produit):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT SUM(quantity) FROM sales WHERE product_name=%s', (produit,)
        )
        rows = cursor.fetchone()[0]

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")


#Obtenir le total des recettes   pour un produit
def get_recete_by_product(produit):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT SUM(quantity*amount) FROM sales WHERE product_name=%s', (produit,)
        )
        rows = cursor.fetchone()[0]

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")




#Obtenir le total des recettes du jour
def get_recete_of_day(date):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT ROUND(SUM(quantity*amount),2) FROM sales WHERE date=%s', (date,)
        )
        rows = cursor.fetchone()[0]

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")


#Obtenir le total des recettes du jour pour un produit
def get_recete_of_day_by_product(produit, day= now.day):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT SUM(quantity*amount) FROM sales product_name =%s AND WHERE day=%s', (produit, day,)
        )
        rows = cursor.fetchone()[0]

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")



#Obtenir le total des recettes du mois pour un produit
def get_recete_of_month_by_product(produit, month= now.month):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT SUM(quantity*amount) FROM sales WHERE product_name =%s AND  month=%s", (produit, month,)
        )
        rows = cursor.fetchone()[0]

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")



#Obtenir la quantité vendue pour un produit sur un mois
def get_quantity_by_product_a_month(produit, mois):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT SUM(quantity) FROM sales WHERE product_name=%s and month =%s', (produit,mois,)
        )
        rows = cursor.fetchone()[0]

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")


#Obtenir les recettes  pour un produit sur un mois
def get_recete_by_product_a_month(produit, mois):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT SUM(quantity*amount) FROM sales WHERE product_name=%s and month =%s', (produit,mois,)
        )
        rows = cursor.fetchone()[0]

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")


def get_product_stuf(produit):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT product_name, ROUND(SUM(amount * quantity),2) AS total_sales, COUNT(*) AS sales_count, SUM(quantity) AS total_quantity FROM sales WHERE product_name = %s GROUP BY product_name', (produit,)
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour ce produit")



produit = "fruit"
month = now.month
result = get_recete_by_product_a_month(produit, month)
print(result)