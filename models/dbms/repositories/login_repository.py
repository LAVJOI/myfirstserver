from models.dbms.repositories.repository import Repository
from models.dbms.requests import select_allaccoutingdata, select_userdata_byid

class LoginRepository(Repository):

    def __init__(self):
        super().__init__()

    def login_db(self, email: str, password: str ) -> dict:
        
        login_status = False

        query = select_allaccoutingdata()

        received_data = self.exec(
            query,
            fetch=True
            
        )
        
        for i in range(len(received_data)):
            if received_data[i]['email'] == email and received_data[i]['password'] == password:
                user_id = received_data[i]["id"]
                login_status = True

                query = select_userdata_byid()
                
                param= (user_id,)

                user_data = self.exec(
                    query,
                    param,
                    fetch=True
                )
                
                

                return {
                    'login_status': login_status, 
                    'user_data': user_data[0]
                }
        else:    
            return {
                'login_status': login_status,
                'user_data': None
            }
            
