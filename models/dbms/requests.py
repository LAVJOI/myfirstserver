def select_allemail () -> str:
    return ("SELECT email FROM user_list")
def select_allaccoutingdata() -> str: 
    return ("SELECT email, password, id FROM user_list")
def select_userdata_byid() -> str:
    return ("SELECT surname, username, id FROM user_list WHERE id= %s")
def insert_data() -> str:
    return ("INSERT INTO user_list (surname, username, email, password) VALUES (%s, %s, %s, %s)")
def update_userdata_byid () -> str:
    return ("UPDATE user_list SET surname = %s, username = %s WHERE id = %s") 
def delete_byid() -> str:
    return ("DELETE FROM user_list WHERE id = %s")
def select_id_byemail () -> str:
    return ("SELECT id FROM user_list WHERE email = %s")