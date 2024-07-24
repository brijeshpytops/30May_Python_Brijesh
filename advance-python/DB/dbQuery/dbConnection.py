import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="blog"
)

# ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
# FLUSH PRIVILEGES;
cursor = db.cursor()

# cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED BY ''")

