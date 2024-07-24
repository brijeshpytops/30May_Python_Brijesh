from .dbConnection import cursor

def create_database():
    database_name = input("Enter a database name: ")
    sql = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    cursor.execute(sql)