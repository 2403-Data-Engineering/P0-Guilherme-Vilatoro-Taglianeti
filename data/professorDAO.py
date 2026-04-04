
from data.db_connection_manager_alchemy import get_connection
from model.MProfessor import ProfessorModel
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
            

    def getProfessors(self):
        pass

    def getProfessors(self):
        pass

    def getProfessors(self):
        pass

    def getProfessors(self):
        pass

    def getProfessors(self):
        pass

    def getProfessors(self):
        pass

