from .dbConnection import cursor, db

def filter_users(column, pattern):
    # Ensure that the column is valid to prevent SQL injection
    valid_columns = ['name', 'age', 'mobile']
    if column not in valid_columns:
        raise ValueError("Invalid column specified. Must be one of: 'name', 'age', 'mobile'.")

    sql = f"SELECT * FROM users WHERE {column} LIKE %s"
    value = (f"%{pattern}%",)  # Use % as wildcards for the LIKE clause

    cursor.execute(sql, value)
    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Mobile: {row[3]}")
    else:
        print("No records found.")


