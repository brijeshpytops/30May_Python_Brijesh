from .dbConnection import cursor, db

def delete_user(user_id):
    sql = "DELETE FROM users WHERE id = %s"
    values = (user_id,)
    
    cursor.execute(sql, values)
    db.commit()

    print(f"User with ID {user_id} deleted successfully.")