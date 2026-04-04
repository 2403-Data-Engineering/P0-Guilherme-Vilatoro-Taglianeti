from model.MProfessor import ProfessorModel
from data.professorDAO import ProfessorDAO


class ProfService:

    profDAO = ProfessorDAO()

    def CreateProfessor(self, pm : ProfessorModel):
        try:    
            self.profDAO.addProfessors(pm)
            
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            return (0,"Error")

        return (0, "Success")
    
    
    def UpdateProfessor(self, pm: ProfessorModel):
        try:    
            self.profDAO.updateProfessor(pm)
            
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            return (0,"Error")

        return (0, "Success")
    
    
    def ViewProfessor(self):
        print("command to be implemented")
        
        return (0, "Success")
    
    def FilterProfessor(self, id):
        try:    
            _,a = self.profDAO.getProfessor_by_id(id)
            return (0,a)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            return (0,"Error")

        
        return (0, "Success")
        
    
    def DeleteProfessor(self, pid:int):
        
        
        print("command to be implemented")
        print(pid)
       
        return (0, "Success")