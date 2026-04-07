from model.MClasses import ClassModel
from data.classesDAO import ClassesDAO


class ClassService:
    classDAO = ClassesDAO()
    # id represents the professor's ID
    def CreateClass(self, cl : ClassModel):
        
        return self.classDAO.addClasses(cl)
    
    
    def UpdateClass(self, cl: ClassModel):
        
        
        print("command to be implemented")
        print(cl.id)
        print(cl.name)
        self.classDAO.updateClass(cl)
        return (0, "Success")

    #cl cid is for class pid is for new professor
    def UpdateClassProfessor(self, cid: int, pid : int):
        print("command to be implemented")
        print(cid)
        print(pid)
        return (0, "Success")
    
    def ViewClass(self):
        
        print("command to be implemented")
        _,r = self.classDAO.getClasses()
        return (0,r)
        
    
    def FilterClass(self, cl: ClassModel):
        
        print("command to be implemented")
        _,r = self.classDAO.getClass_by_id(cl.id)
        return (0, r)
        
    
    def DeleteClass(self, cid : int):
        
        
        print("command to be implemented")
        self.classDAO.DeleteClass(cid)
        return (0, "Success")

    def ReactivateClass(self, cid : int):
        
        
        print("command to be implemented")
        self.classDAO.ReactivateClass(cid)
        return (0, "Success")