from models.dbms.connection import conn, cursor


def load_models(func):
    try: 
        cursor.execute(
            func
        )
        conn.commit()
    except Exception as e:
        print(f"Error while creating tables: {e}")