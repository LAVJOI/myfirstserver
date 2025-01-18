from models.dbms.repositories.repository import Repository
from models.dbms.requests import update_userdata_byid, select_userdata_byid

class UpdateRepository(Repository):

    def __init__(self):
        super().__init__()
    
    def update_db(self, surname: str, username: str, user_id: int) -> dict:


        param = (surname, username, user_id,)

        query = update_userdata_byid()

        self.exec(
            query,
            param,
            commit=True
        )

        param = (user_id,)
        query = select_userdata_byid()
                
        user_data = self.exec(
            query,
            param,
            fetch=True

        )

        login_status = True

        return {
            "login_status": login_status, 
            "user_data": user_data[0]
        }


