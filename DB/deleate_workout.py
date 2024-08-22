from database_connection import connect_database

def delete_workout_session(member_id):
    conn = connect_database()
    cursor = conn.cursor()
    try:
        check_query = "SELECT COUNT(*) FROM members WHERE member_id=%s"
        cursor.execute(check_query, (member_id,))
        result = cursor.fetchone()

        if result[0] == 0:
            print(f"Member with id {member_id} does not exist.")
            return

        delete_query = "UPDATE members SET duration_minutes=NULL, calories_burned=NULL WHERE member_id=%s"
        cursor.execute(delete_query, (member_id,))
        conn.commit()
        print(f"Workout session details for member with id {member_id} have been deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

delete_workout_session(1)
