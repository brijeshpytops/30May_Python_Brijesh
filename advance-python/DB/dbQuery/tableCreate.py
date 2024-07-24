from .dbConnection import cursor

def create_table():
    sql = """CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    mobile VARCHAR(20)
    );"""

    cursor.execute(sql)