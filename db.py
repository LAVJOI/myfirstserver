import psycopg2
import config



class Database:
    def connect_db (self):
        conn = psycopg2.connect (
        host = config.host,
        database = config.db_name,
        user = config.us_name,
        password = config.password,
        )
        return conn

    def registration_db (self, data):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM user_list")
        received_data = cursor.fetchall()

        for i in range( len(received_data)):
            print("база",received_data[i][0])
            print(data['email'])
            if received_data[i][0] == data['email']:
                template = 'bad_data_registration.html'
                cursor.close()
                conn.close()
                return template
            
        surname = data["surname"]
        username = data["username"]
        email  = data["email"]
        password = data["password"]

        cursor.execute(f"INSERT INTO user_list (surname, username, email, password) VALUES ('{surname}', '{username}', '{email}', '{password}');")
        conn.commit()
        cursor.close()
        conn.close()
        template = 'successful.html'
        return template


    def login(self, data):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT email, password, id FROM user_list")
        received_data = cursor.fetchall()
        login_status = False
        for i in range(len(received_data)):
            if received_data[i][0] == data["email"] and received_data[i][1] == data["password"]:
               user_id = received_data[i][2]
               login_status = True
            
               cursor.execute (f'SELECT surname, username, id FROM user_list WHERE id={user_id};')
               user_data = cursor.fetchall()
               cursor.close()
               conn.close()
               return [login_status, user_data]
        else:    
            cursor.close()
            conn.close()
            return login_status

    def delete(self, user_id):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM user_list WHERE id = {user_id}")
        conn.commit()
        cursor.close()
        conn.close()


    def change(self, data):
        conn = self.connect_db()
        cursor = conn.cursor()
        user_id = data[1]
        user_data = data[0]
        username = user_data["username"] 
        surname = user_data["surname"]
        cursor.execute(f"UPDATE user_list SET surname = '{surname}', username = '{username}' WHERE id = {user_id}")
        conn.commit()
        cursor.execute(f"SELECT surname, username, id FROM user_list WHERE id = {user_id}")
        user_data = cursor.fetchall()
        login_status = True 
        return [login_status, user_data]

    def create(self): 
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS user_list  (id SERIAL PRIMARY KEY UNIQUE, surname varchar(50), username varchar(50), email varchar(50) UNIQUE, password varchar(50))")
        conn.commit()
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='user_list'")
        if cursor.fetchone() is None:
            print("Table did't create")

