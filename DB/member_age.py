from database_connection import connect_database

def update_member_age(member_id, new_age):
    conn = connect_database()
    cursor = conn.cursor()
    try:

        check_query = "SELECT COUNT(*) FROM members WHERE member_id=%s"
        cursor.execute(check_query, (member_id,))
        result = cursor.fetchone()

        if result[0] == 0:
            print(f"Member with id {member_id} does not exist.")
            return

        update_query = "UPDATE members SET age=%s WHERE member_id=%s"
        cursor.execute(update_query, (new_age, member_id))
        conn.commit()
        print(f"Member with id {member_id} has been updated successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

update_member_age(1, 35)