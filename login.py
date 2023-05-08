import mysql.connector

def handle_login(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        user="root",
        password=""
    )
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s", (username, password)
        )
        result = cursor.fetchone()
        if result is not None:
            return True
        else:
            return False
    except mysql.connector.Error as e:
        print("Erreur", e)
        raise ValueError("Impossible de se connecter")
