import mysql.connector


def no_entry_get_quantity_by_product():
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT product_name, SUM(quantity) as total_quantity FROM sales GROUP BY product_name'
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour les produits")


def no_entry_max_day_of_sales():
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT date, ROUND(SUM(quantity * amount),2) AS total_sales FROM sales GROUP BY date ORDER BY total_sales DESC LIMIT 1'
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour les produits")


def no_entry_max_month_of_sales():
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT month, MAX(quantity * amount) as max_sales FROM sales GROUP BY date ORDER BY max_sales DESC LIMIT 1'
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour les produits")



def no_entry_max_month():
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT month FROM sales GROUP BY month ORDER BY SUM(quantity * amount) DESC LIMIT 1'
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour les produits")



def no_entry_max_sales():
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT month, ROUND(SUM(quantity * amount),2) AS total_sales FROM sales GROUP BY month ORDER BY total_sales DESC LIMIT 1'
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour les produits")







def total_recette():
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT ROUND(SUM(quantity * amount),2) as total_sales FROM sales'
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour les produits")


def mvp_recette():
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT product_name, quantity, MAX(ROUND(quantity*amount,2)) AS max_sales FROM sales GROUP BY product_name ORDER BY max_sales DESC LIMIT 1'
        )
        rows = cursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible d'obtenir les ventes pour les produits")


res = mvp_recette()
print(res)