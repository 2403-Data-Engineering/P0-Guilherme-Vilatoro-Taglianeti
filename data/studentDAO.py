
from data.db_connection_manager_alchemy import get_connection
from model.MStudents import StudentModel
from sqlalchemy.orm import Session



class StudentDAO():


    def getStudents(self):
        with Session(get_connection()) as session:
            temp = session.query(StudentModel).all()
            return (0,temp)

    def addStudents(self, student: StudentModel):
        
        with Session(get_connection()) as session:
            session.add(student)
            session.commit()
            return(0,"StudentAdded")


    def getStudent_by_id(self, id:int):
        with Session(get_connection()) as session:
            temp = session.query(StudentModel).filter_by(id=id).first()
            return (0,temp)

    def updateStudent(self, student: StudentModel):
        
        with Session(get_connection()) as session:
            try:
                temp = session.query(StudentModel).filter_by(id=student.id).first()
                print(temp)
                print(student)

                if temp == None:
                    return (2, "ErrorGettingStudent")
                
                if not student.major == "":
                    temp.major = student.major
                if not student.first_name == "":
                    temp.first_name = student.first_name
                if not student.last_name == "":
                    temp.last_name = student.last_name
                if not student.email == "":
                    temp.email = student.email
                if not student.year == "":
                    temp.year = student.year
                print(temp)
                print(session.dirty)
                session.commit()
            except Exception as ex:
                print(ex)
            return(0, "StudentUpdated")
            
    #needs to change the active variable to False
    def DeleteStudent(self, id:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(StudentModel).filter_by(id=id).first()

                if temp == None:
                    return (2, "ErrorGettingStudent")

                temp.active = False
                session.commit()
                return (0, "StudentDeleted")
            except Exception as ex:
                print(ex)
                return (2, "ErrorDeletingStudent")

    def ReactivateStudent(self, id:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(StudentModel).filter_by(id=id).first()

                if temp == None:
                    return (2, "ErrorGettingStudent")

                temp.active = True
                session.commit()
                return (0, "StudentDeleted")
            except Exception as ex:
                print(ex)
                return (2, "ErrorDeletingStudent")


