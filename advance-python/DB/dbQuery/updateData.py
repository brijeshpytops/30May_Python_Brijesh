from .dbConnection import cursor, db

def update_user(user_id, name=None, age=None, mobile=None):
    sql = "UPDATE users SET "
    updates = []
    values = []

    if name is not None:
        updates.append("name = %s")
        values.append(name)
    
    if age is not None:
        updates.append("age = %s")
        values.append(age)

    if mobile is not None:
        updates.append("mobile = %s")
        values.append(mobile)

    values.append(user_id)
    sql += ", ".join(updates) + " WHERE id = %s"

    cursor.execute(sql, values)
    db.commit()

    print(f"User with ID {user_id} updated successfully.")