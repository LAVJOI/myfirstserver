from psycopg2.extras import RealDictCursor
from models.dbms.connection import conn
from loguru import logger

class Repository: 
    def __init__(self):
        self.conn = conn 
        logger.add("logs/db_logs/executor_db.log", rotation="10mb", level="INFO")
    
    def exec(self, query: str, param: tuple = None, fetch=False, commit=False): 

        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor: 

            cursor.execute(query) if (param is None) else cursor.execute(query, param)

            if fetch:
                a = cursor.fetchall()
                logger.info(f"Executor output: {a}")
                return a
            if commit: 
                return self.conn.commit()
            

