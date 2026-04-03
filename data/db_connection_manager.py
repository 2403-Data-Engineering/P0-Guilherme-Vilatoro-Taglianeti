import os 
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASS")
port = os.getenv("PORT")
db = os.getenv("DB")

def get_connection():
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        user = os.getenv("USER"),
        password = os.getenv("PASS"),
        port = os.getenv("PORT"),
        db = os.getenv("DB")
    )



def get_message() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        sql = "select * from demo"

        cursor.execute(sql)

        for row in cursor:
            print(row)


def create_message(message:str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("insert into demo (message) values (%(message)s);",{ "message":message})
        conn.commit()

def get_message_by_id(id:int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        

        cursor.execute("select * from demo where id = %s;", [id])
        
        for row in cursor:
            print(row)


def update_message(message:str,id:int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("insert into demo (message) values (%(message)s);",{ "message":message})
        conn.commit()


create_message("this is a test")
get_message()
        
get_message_by_id(7)

