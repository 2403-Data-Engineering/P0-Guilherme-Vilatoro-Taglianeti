from model.MProfessor import ProfessorModel
from data.professorDAO import ProfessorDAO


class ProfService:

    profDAO = ProfessorDAO()

    def CreateProfessor(self, pm : ProfessorModel):
            
        return self.profDAO.addProfessors(pm)
            
        

       
    
    
    def UpdateProfessor(self, pm: ProfessorModel):
          
        return self.profDAO.updateProfessor(pm)
            
        
    
    
    def ViewProfessor(self):
            
        return self.profDAO.getProfessors()
        
    
    def FilterProfessor(self, id):
        
        return  self.profDAO.getProfessor_by_id(id)

    
    def DeleteProfessor(self, pid:int):
        
         
        return self.profDAO.DeleteProfessor(pid)

       
    def ReactivateProfessor(self, pid:int):
        
        
        return self.profDAO.ReactivateProfessor(pid)
