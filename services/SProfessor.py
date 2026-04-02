from model.MProfessor import ProfessorModel


class ProfService:
    def CreateProfessor(self, pm : ProfessorModel):
        print("command to be implemented")
        print(pm.id)
        print(pm.first_name)
        print(pm.last_name)
        print(pm.department)
        print(pm.email)
        return (0, "Success")
    
    
    def UpdateProfessor(self, pm: ProfessorModel):
        
        print("command to be implemented")
        print(pm.id)
        print(pm.first_name)
        print(pm.last_name)
        print(pm.department)
        print(pm.email)
        return (0, "Success")

    #pm id is for Professor id2 is for new professor
    
    def ViewProfessor(self):
        print("command to be implemented")
        
        return (0, "Success")
    
    def FilterProfessor(self):
        
        print("command to be implemented")
        return (0, "Success")
        
    
    def DeleteProfessor(self, pid:int):
        
        
        print("command to be implemented")
        print(pid)
       
        return (0, "Success")