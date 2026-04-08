
from data.db_connection_manager_alchemy import get_connection
from model.MProfessor import ProfessorModel
from model.MClasses import ClassModel
from sqlalchemy.orm import Session



class ProfessorDAO():


    def getProfessors(self):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ProfessorModel).filter_by(active=True).all()
                return (0,temp)
        except :
            return (1, "Failed to retrieve professors from the database.")

    def addProfessors(self, prof: ProfessorModel):
        try:
            with Session(get_connection()) as session:
                session.add(prof)
                session.commit()
                return (0, f"Successfully added professor {prof.first_name} {prof.last_name} to the database.")
        except:
            return (1, "Failed to add the professor to the database.")


    def getProfessor_by_id(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ProfessorModel).filter_by(id=id, active=True).first()
                if temp == None:
                    return (1, f"No professor with id {id} was found.")
                return (0,temp)
        except:
            return (1, f"Failed to retrieve professor with id {id} from the database.")

    def updateProfessor(self, prof: ProfessorModel):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ProfessorModel).filter_by(id=prof.id).first()

                if temp == None:
                    return (1, f"No professor with id {prof.id} was found to update.")
                if not prof.department == "":
                    temp.department = prof.department
                if not prof.first_name == "":
                    temp.first_name = prof.first_name
                if not prof.last_name == "":
                    temp.last_name = prof.last_name
                if not prof.email == "":
                    temp.email = prof.email
                session.commit()
                return (0, f"Successfully updated professor with id {prof.id}.")
        except:
            return (1, f"Failed to update professor with id {prof.id} in the database.")
            
    #needs to change the active variable to False
    def DeleteProfessor(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ProfessorModel).filter_by(id=id).first()

                if temp == None:
                    return (1, f"No professor with id {id} was found to deactivate.")
                classes = session.query(ClassModel).filter_by(prof_id=temp.id, active=True).first()
                if classes == None:
                    temp.active = False
                    session.commit()
                    return (0, f"Successfully deactivated professor with id {id}.")
                else:
                    return (1, f"Professor with id {id} is still assigned to active classes and cannot be deactivated.")
        except:
            return (1, f"Failed to deactivate professor with id {id}.")

    def ReactivateProfessor(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ProfessorModel).filter_by(id=id).first()

                if temp == None:
                    return (1, f"No professor with id {id} was found to reactivate.")

                temp.active = True
                session.commit()
                return (0, f"Successfully reactivated professor with id {id}.")
        except:
            return (1, f"Failed to reactivate professor with id {id}.")


