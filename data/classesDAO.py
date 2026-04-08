
from sqlalchemy.exc import IntegrityError

from data.db_connection_manager_alchemy import get_connection
from model.MClasses import ClassModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError



class ClassesDAO():


    def getClasses(self):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ClassModel).all()
                return (0,temp)
        except:
            return (1, "Failed to retrieve classes from the database.")

    def addClasses(self, clas: ClassModel):
        try:
            with Session(get_connection()) as session:
                session.add(clas)
                session.commit()
                return (0, f"Successfully added class {clas.name} to the database with ID {clas.id}.")
        except:
            return (1, "Failed to add the class to the database.")



    def getClass_by_id(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ClassModel).filter_by(id=id).first()
                if temp == None:
                    return (1, f"No class with id {id} was found.")
                return (0,temp)
        except:
            return (1, f"Failed to retrieve class with id {id} from the database.")

    def updateClass(self, clas: ClassModel):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ClassModel).filter_by(id=clas.id).first()
                

                if temp == None:
                    return (1, f"No class with id {clas.id} was found to update.")
                if not clas.name == "":
                    temp.name = clas.name
                if not clas.prof_id == "":
                    temp.prof_id = clas.prof_id
                
                session.commit()
                return (0, f"Successfully updated class with id {clas.id}.")
        except:
            return (1, f"Failed to update class with id {clas.id} in the database.")
    
    def filterClass(self, clas: ClassModel):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ClassModel)
                
                if temp == None:
                    return (1, f"No class with id {clas.id} was found to update.")
                if not clas.name == "":
                    temp = temp.filter(ClassModel.name.like(f"%{clas.name}%"))
                if not clas.prof_id == "":
                    temp = temp.filter(ClassModel.prof_id.like(f"%{clas.prof_id}%"))
                    
                
                resp = temp.all()
                return (0, resp)
        except:
            return (1, f"Failed to update class with id {clas.id} in the database.")
            
    #needs to change the active variable to False
    def DeleteClass(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ClassModel).filter_by(id=id).first()

                if temp == None:
                    return (1, f"No class with id {id} was found to deactivate.")

                temp.active = False
                session.commit()
                return (0, f"Successfully deactivated class with id {id}.")
        except:
            return (1, f"Failed to deactivate class with id {id}.")

    def ReactivateClass(self, id:int):
        try:
            with Session(get_connection()) as session:
                temp = session.query(ClassModel).filter_by(id=id).first()

                if temp == None:
                    return (1, f"No class with id {id} was found to reactivate.")

                temp.active = True
                session.commit()
                return (0, f"Successfully reactivated class with id {id}.")
        except:
            return (1, f"Failed to reactivate class with id {id}.")


