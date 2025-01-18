def create_user_list() -> str:
    return f"""
        CREATE TABLE IF NOT EXISTS user_list (
            id SERIAL PRIMARY KEY UNIQUE, 
            surname varchar(50), 
            username varchar(50), 
            email varchar(50) UNIQUE, 
            password varchar(50)
        );
    """