from models.dbms.repositories.delete_repository import DeleteRepository
from models.dbms.repositories.login_repository import LoginRepository
from models.dbms.repositories.registration_repository import RegistrationRepository
from models.dbms.repositories.update_repository import UpdateRepository

from loguru import logger



def db_controller(data: dict, delete = False, login = False, registration = False, update = False) -> dict:

    logger.add('logs/db_logs/db_controller.log', rotation = '10 mb', level = 'INFO')

    surname = data.get("surname", None)
    username = data.get("username", None)
    email  = data.get("email", None)
    password = data.get("password", None)
    user_id = int(user_id) if (user_id:= data.get("user_id")) is not None else None

    try:

        if delete:
            logger.info("Deletion affected")
            DeleteRepository().delete_db(user_id)
            logger.opt(colors = True).info("<green>DELETE</green>")
        if login:
            logger.info("Login affected")
            response_data = LoginRepository().login_db(email, password) 
            logger.opt(colors = True).info(f"<green>LOGIN</green>. RESP_DATA: {response_data}")
            return response_data
        if registration:
            logger.info("Registration affected")
            response_data = RegistrationRepository().registration_db(username, surname, email, password)
            logger.opt(colors = True).info(f"<green>REGISTARTION</green>. RESP_DATA: {response_data}")
            return response_data
        if update:
            logger.info("Update affected")
            response_data = UpdateRepository().update_db(surname, username, user_id)
            logger.opt(colors = True).info(f"<green>UPDATE</green>. RESP_DATA: {response_data}")
            return response_data

    except Exception as e:
        print(f"Incorrect data distribution: {e}")
        