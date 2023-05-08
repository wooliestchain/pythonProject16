import mysql.connector
from tkinter import messagebox


def add_commerce(code,nom,year, sector, descr):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        username="root",
        password=""
    )

    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO commerce (code, commerce_name,year_fond, sector, descr)
        VALUES (%s, %s, %s, %s, %s);
        """, (code,nom,year, sector, descr))
        conn.commit()
        print("Commerce ajouté avec succés")
    except mysql.connector.Error as e:
        print("Une erreur s'est produite!!",e)

    finally:
        cursor.close()
        conn.close()

res = add_commerce(12, "ffe", 2002, "dsd", "dfddf")
print(res)
def modify_commerce(code, new_name, new_sector, new_descr):
    import mysql.connector

    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="wool",
            username="root",
            password=""
        )

        cursor = conn.cursor()
        sql_query = "UPDATE commerce SET commerce_name=%s, sector=%s, descr=%s WHERE code=%s"
        data = (new_name, new_sector, new_descr, code)
        cursor.execute(sql_query, data)
        conn.commit()
        print("Le commerce a été modifié avec succès !")

    except mysql.connector.Error as e:
        print("Une erreur s'est produite :", e)

    finally:
        cursor.close()
        conn.close()
