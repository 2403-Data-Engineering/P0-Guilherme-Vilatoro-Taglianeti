
from data.db_connection_manager_alchemy import get_connection
from model.MStudents import StudentModel
from model.MStudentClass import StudentClass
from model.MClasses import ClassModel
from sqlalchemy.orm import Session



class StudentDAO():


    def getStudents(self):
        try:
            with Session(get_connection()) as session:
                temp = session.query(StudentModel).filter_by(active=True).all()
                return (0,temp)
        except:
            return (1, "Failed to retrieve students from the database.")

    def addStudents(self, student: StudentModel):
        try:
            with Session(get_connection()) as session:
                session.add(student)
                session.commit()
                return(0,f"Successfully added student {student.first_name} {student.last_name} to the database with ID {student.id}.")
        except:
            return (1, "Failed to add the student to the database.")


    def getStudent_by_id(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(StudentModel).filter_by(id=id).first()
                if temp == None:
                    return (1, f"No student with id {id} was found.")
                return (0,temp)
        except:
            return (1, f"Failed to retrieve student with id {id} from the database.")

    def updateStudent(self, student: StudentModel):
        try:
            with Session(get_connection()) as session:
                temp = session.query(StudentModel).filter_by(id=student.id).first()
                

                if temp == None:
                    return (1, f"No student with id {student.id} was found to update.")
                
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
                
                session.commit()
                return(0, f"Successfully updated student with id {student.id}.")
        except:
            return (1, f"Failed to update student with id {student.id} in the database.")
        
    def viewAllClassesAStudentIsIn(self, sid:int):
        try:
            with Session(get_connection()) as session:
                res, d = self.getStudent_by_id(sid)
                if res == 1:
                    return (1,d)
                
                temp = session.query(ClassModel)\
                .join(StudentClass, StudentClass.class_id == ClassModel.id)\
                .join(StudentModel, StudentClass.student_id == StudentModel.id).filter(StudentModel.id == sid, ClassModel.active == True, StudentClass.active == True).all()

                return (0,temp)
        except:
            return (1, f"Failed to view all of student's classes.")

    def filterStudents(self, filter:StudentModel):
        try:
            with Session(get_connection()) as session:

                temp = session.query(StudentModel)

                if not filter.major == "":
                    temp = temp.filter(StudentModel.major.like(f"%{filter.major}%"))
                if not filter.first_name == "":
                    temp = temp.filter(StudentModel.first_name.like(f"%{filter.first_name}%"))
                if not filter.last_name == "":
                    temp = temp.filter(StudentModel.last_name.like(f"%{filter.last_name}%"))
                if not filter.email == "":
                    temp = temp.filter(StudentModel.email.like(f"%{filter.email}%"))
                if not filter.year == "":
                    temp = temp.filter(StudentModel.year.like(f"%{filter.year}%"))

                result = temp.all() 
                return (0,result)
        except:
            return (1, f"Failed to retrieve filtered student from the database.")
            
    #needs to change the active variable to False
    def DeleteStudent(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(StudentModel).filter_by(id=id).first()

                if temp == None:
                    return (1, f"No student with id {id} was found to delete.")
                
                classes = session.query(StudentClass).filter_by(student_id=temp.id, active=True).first()

                if classes == None:
                    temp.active = False
                    session.commit()
                    return (0, f"Successfully deactivated student with id {id}.")
                else:
                    return(1, f"Student with id {id} is still enrolled in active classes and cannot be deleted.")
        except:
            return (1, f"Failed to delete student with id {id}.")

    def ReactivateStudent(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(StudentModel).filter_by(id=id).first()

                if temp == None:
                    return (1, f"No student with id {id} was found to reactivate.")

                temp.active = True
                session.commit()
                return (0, f"Successfully reactivated student with id {id}.")
        except:
            return (1, f"Failed to reactivate student with id {id}.")


    def EnrollStudent(self, cid:int,sid:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(StudentClass).filter_by(class_id = cid, student_id= sid).first()
                
                if temp == None:
                    res,temp = self.getStudent_by_id(sid)
                    if res == 1:
                        return (1,temp)
                    elif temp.active == False:
                        return (1, f"Student {sid} is inactive, and he must be active to enroll." )
                    session.add(StudentClass(class_id = cid, student_id= sid))
                    message = f"Successfully enrolled student {sid} in class {cid}."
                else:
                    temp.active = True
                    message = f"Student {sid} is already enrolled in class {cid}; enrollment was left active."
                session.commit()
                return (0, message)
        except:
            return (1, f"Failed to enroll student {sid} in class {cid}.")
            
    def UnenrollStudent(self, cid:int,sid:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(StudentClass).filter_by(class_id = cid, student_id= sid).first()
                
                if temp == None:
                    return (1, f"No enrollment was found for student {sid} in class {cid}.")
                
                else:
                    temp.active = False
                
                session.commit()
            
                
                return (0, f"Successfully unenrolled student {sid} from class {cid}.")
        except:
            return (1, f"Failed to unenroll student {sid} from class {cid}.")

