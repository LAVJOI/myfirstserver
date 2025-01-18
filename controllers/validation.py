from respect_validation import Validator as v

class Validator: 

    def __init__(self, data: dict):
        if "username" in data:
            global username
            self.username = data["username"] 

        if "surname" in data:
            global surname
            self.surname = data["surname"]

        if "email" in data:
            global email
            self.email = data["email"]

        if "password" in data:
            global password
            self.password = data["password"]

    
    def userdata_validator(self):

        validstatus_username = v.AllOf(
            v.NotEmpty(),
            v.stringType(), 
            v.length(min_value = 1, max_value = 49), 
            v.alnum()
            ).validate(self.username)
            
        validstatus_surname = v.AllOf(
            v.NotEmpty(),
            v.stringType(), 
            v.length(min_value = 1, max_value = 49), 
            v.alnum()
            ).validate(self.surname)
        
        return {
            "username": validstatus_username,
            "surname": validstatus_surname
            }



    
    def accoutingdata_validator(self):
        validstatus_password = v.AllOf(
            v.NotEmpty(),
            v.length(min_value = 6, max_value = 16)
        ).validate(self.password)

        validstatus_email = v.AllOf(
            v.NotEmpty(), 
            v.email()
            ).validate(self.email)
     
        return {
            "password": validstatus_password,
            "email": validstatus_email
            }
