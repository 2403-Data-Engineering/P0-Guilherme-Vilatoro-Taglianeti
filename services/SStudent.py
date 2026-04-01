from model.MStudents import StudentModel


class StudentService:
    def CreateStudent(self, sm : StudentModel):
        print("command to be implemented")
        print(sm.id)
        print(sm.first_name)
        print(sm.last_name)
        print(sm.department)
        print(sm.email)
        return (0, "Success")
    
    
    def UpdateStudent(self, sm: StudentModel):
        
        print("command to be implemented")
        print(sm.id)
        print(sm.first_name)
        print(sm.last_name)
        print(sm.department)
        print(sm.email)
        return (0, "Success")

    #sm id is for Student id2 is for new Student
    
    def ViewStudent(self):
        print("command to be implemented")
        
        return (0, "Success")
    
    def FilterStudent(self):
        
        print("command to be implemented")
        return (0, "Success")
        
    
    def DeleteStudent(self, sm : StudentModel):
        
        
        print("command to be implemented")
        print(sm.id)
        #print(sm.first_name)
        #print(sm.last_name)
        #print(sm.department)
        #print(sm.email)
        return (0, "Success")