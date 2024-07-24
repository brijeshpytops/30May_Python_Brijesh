from .dbConnection import cursor, db

def show_data():
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Mobile: {row[3]}")
