from database_connection import connect_database

def list_distinct_trainers():
    conn = connect_database()
    cursor = conn.cursor()
    try:
        query = "SELECT DISTINCT trainer_id FROM members"
        cursor.execute(query)
        results = cursor.fetchall()
        trainer_ids = []
        for row in results:
            trainer_ids.append(row[0])
        return trainer_ids
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


trainers = list_distinct_trainers()
print("Distinct trainer IDs:", trainers)


def count_members_per_trainer():
    conn = connect_database()
    cursor = conn.cursor()
    try:
        query = "SELECT trainer_id, COUNT(*) AS member_count FROM members GROUP BY trainer_id"
        cursor.execute(query)
        results = cursor.fetchall()
        trainer_member_counts = {}
        for row in results:
            trainer_id = row[0]
            member_count = row[1]
            trainer_member_counts[trainer_id] = member_count
        return trainer_member_counts
    except Exception as e:
        print(f"Error: {e}")
        return {}
    finally:
        cursor.close()
        conn.close()

member_counts = count_members_per_trainer()
print("Members per trainer:", member_counts)


def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    cursor = conn.cursor()
    try:
        query = """
        SELECT member_id, name, age, trainer_id 
        FROM members 
        WHERE age BETWEEN %s AND %s
        """
        cursor.execute(query, (start_age, end_age))
        results = cursor.fetchall()
        members = []
        for row in results:
            member = {
                'member_id': row[0],
                'name': row[1],
                'age': row[2],
                'trainer_id': row[3]
            }
            members.append(member)
        return members
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
members_in_range = get_members_in_age_range(25, 30)
print("Members between ages 25 and 30:", members_in_range)

