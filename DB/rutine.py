from database_connection import connect_database

conn = connect_database()
cursor = conn.cursor()
try:
    routine_duration_in_minutes = 30
    calories_burned = 1300
    member_id = 1
    query = "UPDATE members SET duration_minutes=%s, calories_burned=%s WHERE member_id=%s"
    cursor.execute(query, (routine_duration_in_minutes, calories_burned, member_id))
    conn.commit()
    print("Routine added successfully")
except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
