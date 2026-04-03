import sys
sys.path.append(r"D:\Revature\P0-Guilherme-Vilatoro-Taglianeti")


from sqlalchemy import create_engine, text
from model.Base import Base
from model.MStudentClass import StudentClass
from model.MProfessor import ProfessorModel
from model.MClasses import ClassModel
from model.MStudents import StudentModel

import os 
from dotenv import load_dotenv




def get_connection():
    load_dotenv()
    engine = create_engine(f"mysql+mysqlconnector://{os.getenv("USER")}:{os.getenv("PASS")}@{os.getenv("HOST")}:{os.getenv("PORT")}/{os.getenv("DB")}",echo=True)
    Base.metadata.create_all(engine)
    return engine

def noUse():
    try:
        with get_connection().connect() as con:
            result = con.execute(text("select * from demo"))
            print(result.all())
            print(f"Connection to the for user created successfully.")
        print(result.all())

    except Exception as ex:
        print("Connection could not be made due to the following error:\n", ex)

noUse()


