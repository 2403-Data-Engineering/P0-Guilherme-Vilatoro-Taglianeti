from model.MStudents import StudentModel
from data.studentDAO import StudentDAO


class StudentService:

    studentDAO = StudentDAO()

    def CreateStudent(self, sm : StudentModel):
        print(self.studentDAO.addStudents(sm))
        return (0, "Success")
    
    
    def UpdateStudent(self, sm: StudentModel):
        
        self.studentDAO.updateStudent(sm)
        print(sm)
        return (0, "Success")

    
    def ViewStudent(self):
        print("command to be implemented")
        print(self.studentDAO.getStudents())
        return (0, "Success")
    
    def FilterStudent(self, id):
        
        print("command to be implemented")
        print(self.studentDAO.getStudent_by_id(id))
        return (0, "Success")
        
    
    def DeleteStudent(self, sid:int):
        
        
        print("command to be implemented")
        print(sid)
        self.studentDAO.DeleteStudent(sid)
        return (0, "Success")
    
    def ReactivateStudent(self, sid:int):
        
        print("command to be implemented")
        print(sid)
        self.studentDAO.ReactivateStudent(sid)
        return (0, "Success")
    
    def EnrollStudent(self,  cid:int, sid:int):
        print("command to be implemented")
        print(sid)
        print(cid)
        self.studentDAO.EnrollStudent(cid,sid)
        return (0, "Success")

    def UnenrollStudent(self,  cid:int, sid:int):
        print("command to be implemented")
        print(sid)
        print(cid)
        self.studentDAO.UnenrollStudent(cid,sid)
        return (0, "Success")