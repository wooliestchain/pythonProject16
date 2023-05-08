import mysql.connector



def add_product(code,produit, categorie, prix):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        username="root",
        password=""
    )

    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO product (code, product_name, product_categorie, prix)
        VALUES (%s, %s, %s, %s);
        """, (code,produit, categorie, prix))
        conn.commit()
        print("Produit ajouté avec succès")
    except mysql.connector.Error as e:
        print("Une erreur s'est produite!!",e)

    finally:
        cursor.close()
        conn.close()




def modify_product(product_id, new_product_name, new_category, new_price):
    import mysql.connector

    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="wool",
            username="root",
            password=""
        )

        cursor = conn.cursor()
        sql_query = "UPDATE product SET product_name=%s, product_categorie=%s, prix=%s WHERE code=%s"
        data = (new_product_name, new_category, new_price, product_id)
        cursor.execute(sql_query, data)
        conn.commit()
        print("Le produit a été modifié avec succès !")

    except mysql.connector.Error as e:
        print("Une erreur s'est produite :", e)

    finally:
        cursor.close()
        conn.close()


modify_product(10,"raisin","pépin",40)