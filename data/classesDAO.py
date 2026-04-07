
from sqlalchemy.exc import IntegrityError

from data.db_connection_manager_alchemy import get_connection
from model.MClasses import ClassModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError



class ClassesDAO():


    def getClasses(self):
        with Session(get_connection()) as session:
            temp = session.query(ClassModel).all()
            return (0,temp)

    def addClasses(self, clas: ClassModel):
        try:
            with Session(get_connection()) as session:
                session.add(clas)
                session.commit()
                return(0,"ClasAdded")
        except IntegrityError:
            return(1, "The professor ID provided does not exist.")



    def getClass_by_id(self, id:int):
        with Session(get_connection()) as session:
            temp = session.query(ClassModel).filter_by(id=id).first()
            return (0,temp)

    def updateClass(self, clas: ClassModel):
        
        with Session(get_connection()) as session:
            try:
                temp = session.query(ClassModel).filter_by(id=clas.id).first()
                print(temp)
                print(clas)

                if temp == None:
                    return (2, "ErrorGettingClass")
                if not clas.name == "":
                    temp.name = clas.name
                if not clas.prof_id == "":
                    temp.prof_id = clas.prof_id
                print(temp)
                print(session.dirty)
                session.commit()
            except Exception as ex:
                print(ex)
            return(0, "ClasUpdated")
            
    #needs to change the active variable to False
    def DeleteClass(self, id:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(ClassModel).filter_by(id=id).first()

                if temp == None:
                    return (2, "ErrorGettingClass")

                temp.active = False
                session.commit()
                return (0, "ClassDeleted")
            except Exception as ex:
                print(ex)
                return (2, "ErrorDeletingClass")

    def ReactivateClass(self, id:int):
        with Session(get_connection()) as session:
            try:
                temp = session.query(ClassModel).filter_by(id=id).first()

                if temp == None:
                    return (2, "ErrorGettingClas")

                temp.active = True
                session.commit()
                return (0, "ClasDeleted")
            except Exception as ex:
                print(ex)
                return (2, "ErrorDeletingClas")


