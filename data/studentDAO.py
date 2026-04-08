
from data.db_connection_manager_alchemy import get_connection
from model.MStudents import StudentModel
from model.MStudentClass import StudentClass
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
                
                classes = session.query(StudentClass).filter_by(student_id=temp.id, active=True).first()

                if classes == None:
                    temp.active = False
                    session.commit()
                    return (0, "StudentDeleted")
                else:
                    return(1,"Student is still enrolled into class(es)")
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


    def EnrollStudent(self, cid:int,sid:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(StudentClass).filter_by(class_id = cid, student_id= sid).first()
                
                if temp == None:
                    session.add(StudentClass(class_id = cid, student_id= sid))
                    message = "Student enrolled"
                else:
                    temp.active = True
                    message = "Student is already enrolled"
                session.commit()
                return (0, message)
            except Exception as ex:
                print(ex)
                return (2, "ErrorEnrollingStudent")
            
    def UnenrollStudent(self, cid:int,sid:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(StudentClass).filter_by(class_id = cid, student_id= sid).first()
                
                if temp == None:
                    return (0, "Student enrollment not found")
                
                else:
                    temp.active = False
                
                session.commit()
            
                
                return (0, "Student unenrolled")
            except Exception as ex:
                print(ex)
                return (2, "ErrorEnrollingStudent")

