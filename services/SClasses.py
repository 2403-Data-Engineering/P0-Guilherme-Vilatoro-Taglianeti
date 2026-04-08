from model.MClasses import ClassModel
from data.classesDAO import ClassesDAO


class ClassService:
    classDAO = ClassesDAO()
    # id represents the professor's ID
    def CreateClass(self, cl : ClassModel):
        
        return self.classDAO.addClasses(cl)
    
    
    def UpdateClass(self, cl: ClassModel):
        
        
        return self.classDAO.updateClass(cl)


    def ViewClass(self):
        
        
        return self.classDAO.getClasses()
        
    
    def FilterClass(self, cl: ClassModel):
        
        return self.classDAO.getClass_by_id(cl.id)
        
    
    def DeleteClass(self, cid : int):
        
        
        return self.classDAO.DeleteClass(cid)

    def ReactivateClass(self, cid : int):
        
        return self.classDAO.ReactivateClass(cid)