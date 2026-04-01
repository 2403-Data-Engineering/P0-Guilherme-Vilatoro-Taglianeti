from model.MStudents import StudentModel


class StudentService:
    def CreateStudent(self, sm : StudentModel):
        print("command to be implemented")
        print(sm.id)
        print(sm.first_name)
        print(sm.last_name)
        print(sm.major)
        print(sm.email)
        print(sm.year)
        return (0, "Success")
    
    
    def UpdateStudent(self, sm: StudentModel):
        
        print("command to be implemented")
        print(sm.id)
        print(sm.first_name)
        print(sm.last_name)
        print(sm.major)
        print(sm.email)
        print(sm.year)
        return (0, "Success")

    
    def ViewStudent(self):
        print("command to be implemented")
        
        return (0, "Success")
    
    def FilterStudent(self):
        
        print("command to be implemented")
        return (0, "Success")
        
    
    def DeleteStudent(self, sid:int):
        
        
        print("command to be implemented")
        print(sid)
        
        return (0, "Success")
    
    def EnrollStudent(self, sid:int, cid:int):
        print("command to be implemented")
        print(sid)
        print(cid)
        
        return (0, "Success")