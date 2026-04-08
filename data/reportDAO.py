
from data.db_connection_manager_alchemy import get_connection
from model.MStudents import StudentModel
from model.MStudentClass import StudentClass
from model.MProfessor import ProfessorModel
from model.MClasses import ClassModel
from sqlalchemy.orm import Session



class ReportDAO():

    def getStudentReportData(self, sid:int):
        try:
            with Session(get_connection()) as session:
                data = session.query(
                StudentModel.first_name.label('student_first_name'),
                StudentModel.last_name.label('student_last_name'),
                StudentModel.major.label('student_major'),
                StudentModel.email.label('student_email'),
                ClassModel.name.label('class_name'),
                ClassModel.id.label('class_id'),
                ProfessorModel.first_name.label('professor_first_name'),
                ProfessorModel.last_name.label('professor_last_name')
                ).filter(StudentModel.id == sid)\
                .join(StudentClass, StudentModel.id == StudentClass.student_id)\
                .join(ClassModel, ClassModel.id == StudentClass.class_id)\
                .join(ProfessorModel, ProfessorModel.id == ClassModel.prof_id)\
                .all()

                return(0,data)
        except:
            return(1,'Failed to fetch the student\'s data')

    def getProfessorReportData(self, pid:int):
        try:
            with Session(get_connection()) as session:
                data = session.query(
                StudentModel.first_name.label('student_first_name'),
                StudentModel.last_name.label('student_last_name'),
                StudentModel.email.label('student_email'),
                ClassModel.name.label('class_name'),
                ClassModel.id.label('class_id'),
                ProfessorModel.first_name.label('professor_first_name'),
                ProfessorModel.last_name.label('professor_last_name'),
                ProfessorModel.email.label('professor_email'),
                ProfessorModel.department.label('professor_department')
                ).filter(ProfessorModel.id == pid)\
                .join(ClassModel, ClassModel.prof_id == ProfessorModel.id)\
                .join(StudentClass, ClassModel.id == StudentClass.class_id)\
                .join(StudentModel, StudentModel.id == StudentClass.student_id)\
                .order_by('class_id').all()

                return(0,data)
        except:
            return(1,'Failed to fetch the professor\'s data')