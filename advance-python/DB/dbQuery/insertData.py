from .dbConnection import cursor, db

def insert_data():
    sql = "INSERT INTO users (name, age, mobile) VALUES (%s, %s, %s)"
    vals = [
        ("John Doe", 28, "123-456-7890"),
        ("Jane Smith", 34, "234-567-8901"),
        ("Alice Johnson", 22, "345-678-9012"),
        ("Bob Brown", 45, "456-789-0123"),
        ("Charlie Davis", 31, "567-890-1234"),
        ("Dave Evans", 27, "678-901-2345"),
        ("Eve Foster", 29, "789-012-3456"),
        ("Frank Green", 36, "890-123-4567"),
        ("Grace Harris", 41, "901-234-5678"),
        ("Hank Irvine", 38, "012-345-6789")
    ]

    for val in vals:
        cursor.execute(sql, val)

    # Commit the transaction
    db.commit()
