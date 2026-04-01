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

    #cl id is for class id2 is for new professor
    def UpdateClassProfessor(self, cl: ClassModel, id2 : int):
        print("command to be implemented")
        print(cl.id)
        print(id2)
        return (0, "Success")
    
    def ViewClass(self):
        
        print("command to be implemented")
        
        return (0, "Success")
    
    def FilterClass(self):
        
        print("command to be implemented")
        return (0, "Success")
        
    
    def DeleteClass(self, cl : ClassModel):
        
        
        print("command to be implemented")
        print(cl.id)
        print(cl.name)
        return (0, "Success")