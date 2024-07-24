from .dbConnection import cursor

def show_databases():
    sql = "show databases"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result