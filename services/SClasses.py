from model.MClasses import ClassModel

class ClassService:

    # id represents the professor's ID
    def CreateClass(self, cl : ClassModel):
        print("command to be implemented")
        print(cl.id)
        print(cl.name)
        return (0, "Success")
    
    
    def UpdateClass(self, cl: ClassModel):
        
        
        print("command to be implemented")
        print(cl.id)
        print(cl.name)
        return (0, "Success")

    #cl cid is for class pid is for new professor
    def UpdateClassProfessor(self, cid: int, pid : int):
        print("command to be implemented")
        print(cid)
        print(pid)
        return (0, "Success")
    
    def ViewClass(self):
        
        print("command to be implemented")
        
        return (0, "Success")
    
    def FilterClass(self):
        
        print("command to be implemented")
        return (0, "Success")
        
    
    def DeleteClass(self, cid : int):
        
        
        print("command to be implemented")
        print(cid)
        return (0, "Success")