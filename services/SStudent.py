from model.MStudents import StudentModel
from data.studentDAO import StudentDAO


class StudentService:

    studentDAO = StudentDAO()

    def CreateStudent(self, sm : StudentModel):
       
        return self.studentDAO.addStudents(sm)
        
    
    
    def UpdateStudent(self, sm: StudentModel):
        
        
        return self.studentDAO.updateStudent(sm)

    
    def ViewStudent(self):
        return self.studentDAO.getStudents()
    
    def FilterStudent(self, sm: StudentModel):
        
        return self.studentDAO.filterStudents(sm)
        
    
    def DeleteStudent(self, sid:int):
        
        return self.studentDAO.DeleteStudent(sid)
    
    def ReactivateStudent(self, sid:int):

        return  self.studentDAO.ReactivateStudent(sid)
    
    def EnrollStudent(self,  cid:int, sid:int):

        return self.studentDAO.EnrollStudent(cid,sid)

    def UnenrollStudent(self,  cid:int, sid:int):
        
        return self.studentDAO.UnenrollStudent(cid,sid)