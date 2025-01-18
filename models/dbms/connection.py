import os
import psycopg2
from dotenv import load_dotenv, find_dotenv 


try:
    load_dotenv(find_dotenv())
    
    conn = psycopg2.connect(
        host=os.environ['HOST_DATACOLLECTOR'],
        database=os.environ['NAME_DATACOLLECTOR'],
        user=os.environ['USER_DATACOLLECTOR'],
        password=os.environ['PASSWORD_DATACOLLECTOR'],
        port=os.environ['PORT_DATACOLLECTOR'],
    )

    cursor = conn.cursor()


except Exception as e:
    print(f'Error while connecting to the database: {e}')