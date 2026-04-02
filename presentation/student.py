from presentation.menu import Menu
from model.MStudents import StudentModel
from services.SStudent import StudentService
from presentation.helperFunctions import *

class Student(Menu):

    StudentServ = StudentService()


    def render(self):
        while (True):
            print("=====================================================")
            print("You are in the student screen")
            print("What would you like to administer today?")
            print("1) add a new student")
            print("2) update a student's data")
            print("3) view all students")
            print("4) filter students")
            print("5) delete a student")
            print("6) Enroll a student to a class")
            print("b) Back")
            print("q) Quit")
            print("=====================================================")

        
            inp = input().lower()
            
            match inp:
                case "1":
                    self.CreateStudent()
                    
                case "2":
                    self.UpdateStudent()
                

                case "3":
                    self.ViewStudent()
                    
                case "4":
                    self.FilterStudent()
                    
                case "5":
                    self.DeleteStudent()
                case "6":
                    self.EnrollStudent()
                case "b":
                    return (0,"MainMenu")
                    
                case "q":
                    print("=====================================================")
                    print("Thank you for utilizing our Admin Portal")
                    print("=====================================================")
                    return (1,"Quit")
                case _:
                    print("*****************************************************")
                    print("Unregistered key\""+ inp +"\", please try again.")
                    print("*****************************************************")
        
        
        
                

                
        


    def CreateStudent(self):
       
            
        print("=====================================================")
        print("To create a Student I will need some extra information")
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        

        msg = "Student's first name:"
        fname = getUserInpName(msg, error)
        msg = "Student's last name:"
        lname = getUserInpName(msg, error)
        msg = "Student's major:"
        major = getUserInpName(msg, error)
        msg = "Student's email:"
        email = getUserInpEmail(msg, error)
        msg = """Student's year:
(freshman,sophomore,junior,senior)"""
        year = getUserInpYear(msg, error)
        cl = StudentModel(None, fname, lname, major, email, year)
        print("=====================================================")
        self.StudentServ.CreateStudent(cl)
        print("=====================================================")
        return (0,"createStudent")
    
    def UpdateStudent(self):
        
        print("=====================================================")
        print("To update a student's information I will need some extra data")
        print("***If you don't want to change the data leave it blank***")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""

        msg = "Student's id:"
        id = getUserInpInt(msg, error)
        msg = "Student's first name:"
        fname = getUserInpName(msg, error,True)
        msg = "Student's last name:"
        lname = getUserInpName(msg, error,True)
        msg = "Student's major:"
        major = getUserInpName(msg, error,True)
        msg = "Student's email:"
        email = getUserInpEmail(msg, error,True)
        msg = """Student's year:
(freshman,sophomore,junior,senior)"""
        year = getUserInpYear(msg, error)
        #maybe use kwargs for input?
        cl = StudentModel(id, fname, lname, major, email, year)
        print("=====================================================")
        self.StudentServ.UpdateStudent(cl)
        print("=====================================================")
        return (0,"updateStudent")
    

    
    def ViewStudent(self):
        
        print("=====================================================")

        self.StudentServ.ViewStudent()

        print("=====================================================")
        return (0,"viewStudent")
    
    def FilterStudent(self):
        
        
        print("=====================================================")
        
        self.StudentServ.FilterStudent()
        print("=====================================================")
        return (0,"filterStudent")
    
    def DeleteStudent(self):
        
        print("=====================================================")
        print("To delete a Student I will need some extra information")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        msg = "Student's id:"
        id = getUserInpInt(msg, error)


        
        print("=====================================================")
        self.StudentServ.DeleteStudent(id)
        print("=====================================================")
        return (0,"deleteStudent")
    
    def EnrollStudent(self):
        print("=====================================================")
        print("To enroll a student I will need some extra information")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        msg = "Student's id:"
        sid = getUserInpInt(msg, error)
        msg = "Class id:"
        cid = getUserInpInt(msg, error)

        
        print("=====================================================")
        self.StudentServ.EnrollStudent(sid, cid)
        print("=====================================================")
        return (0,"EnrollStudent")


