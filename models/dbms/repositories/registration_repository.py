from models.dbms.repositories.repository import Repository
from models.dbms.requests import select_allemail, insert_data, select_id_byemail


class RegistrationRepository (Repository):
    def __init__(self):
        super().__init__()
    
    def registration_db(self, username: str, surname: str, email: str, password: str ) -> dict:

        query = select_allemail()

        received_data = self.exec(
            query, 
            fetch=True
        )

        for i in range( len(received_data)):
            if received_data[i]['email'] == email:
                return {
                    "login_status": False,
                    "user_data": None
                }
            
    

        param = (surname, username, email, password)

        query = insert_data()

        self.exec(
            query,
            param,
            commit = True
        )
    
        param = (email,)

        query = select_id_byemail()

        user_id = self.exec(
            query,
            param, 
            fetch= True
        )

        return {
            "login_status": True,
            "user_data": {
                        'surname': surname,
                        'username': username,
                        'id': user_id[0]["id"]                       

            }
        }

