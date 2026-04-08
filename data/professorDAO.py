
from data.db_connection_manager_alchemy import get_connection
from model.MProfessor import ProfessorModel
from model.MClasses import ClassModel
from sqlalchemy.orm import Session



class ProfessorDAO():


    def getProfessors(self):
        with Session(get_connection()) as session:
            temp = session.query(ProfessorModel).all()
            return (0,temp)

    def addProfessors(self, prof: ProfessorModel):
        
        with Session(get_connection()) as session:
            session.add(prof)
            session.commit()
            return(0,"ProfAdded")


    def getProfessor_by_id(self, id:int):
        with Session(get_connection()) as session:
            temp = session.query(ProfessorModel).filter_by(id=id).first()
            return (0,temp)

    def updateProfessor(self, prof: ProfessorModel):
        
        with Session(get_connection()) as session:
            try:
                temp = session.query(ProfessorModel).filter_by(id=prof.id).first()
                print(temp)
                print(prof)

                if temp == None:
                    return (2, "ErrorGettingProf")
                if not prof.department == "":
                    temp.department = prof.department
                if not prof.first_name == "":
                    temp.first_name = prof.first_name
                if not prof.last_name == "":
                    temp.last_name = prof.last_name
                if not prof.email == "":
                    temp.email = prof.email
                print(temp)
                print(session.dirty)
                session.commit()
            except Exception as ex:
                print(ex)
            return(0, "ProfUpdated")
            
    #needs to change the active variable to False
    def DeleteProfessor(self, id:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(ProfessorModel).filter_by(id=id).first()

                if temp == None:
                    return (2, "ErrorGettingProf")
                classes = session.query(ClassModel).filter_by(prof_id=temp.id, active=True).first()
                if classes == None:
                    temp.active = False
                    session.commit()
                    return (0, "Professor deleted")
                else:
                    return (1, "Professor is still teaching")
            except Exception as ex:
                print(ex)
                return (1, "ErrorDeletingProf")

    def ReactivateProfessor(self, id:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(ProfessorModel).filter_by(id=id).first()

                if temp == None:
                    return (2, "ErrorGettingProf")

                temp.active = True
                session.commit()
                return (0, "professor reactivated")
            except Exception as ex:
                print(ex)
                return (2, "ErrorDeletingProf")


