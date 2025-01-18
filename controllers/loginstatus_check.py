from flask import session

#Check user login status 

def login_check()-> bool:
    response_data = session.get('global_data', None)
    if response_data == None:
        login_status = False
    else:
        login_status = response_data["login_status"]
    return login_status