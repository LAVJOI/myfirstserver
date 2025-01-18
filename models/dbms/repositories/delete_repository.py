from models.dbms.repositories.repository import Repository
from models.dbms.requests import delete_byid

class DeleteRepository (Repository):
    def __init__(self):
        super().__init__()

    def delete_db(self, user_id: int) -> None:

        query = delete_byid() 

        param = (user_id,)

        
        self.exec(
            query, 
            param,
            commit=True
        )

 
