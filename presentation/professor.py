from presentation.menu import Menu
from model.MProfessor import ProfessorModel
from services.SProfessor import ProfService
from presentation.helperFunctions import *

class Professor(Menu):

    ProfServ = ProfService()


    def render(self):
        while (True):
            print("=====================================================")
            print("You are in the professor screen")
            print("What would you like to administer today?")
            print("1) add a new professor")
            print("2) update a professor's data")
            print("3) view all professors")
            print("4) filter professors")
            print("5) delete a professor")
            print("b) Back")
            print("q) Quit")
            print("=====================================================")

        
            inp = input().lower()
            
            match inp:
                case "1":
                    self.CreateProfessor()
                    
                case "2":
                    self.UpdateProfessor()
                

                case "3":
                    self.ViewProfessor()
                    
                case "4":
                    self.FilterProfessor()
                    
                case "5":
                    self.DeleteProfessor()
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
        
        
        
                

                
        


    def CreateProfessor(self):
       
            
        print("=====================================================")
        print("To create a Professor I will need some extra information")
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        


        msg = "Professor's first name:"
        fname = getUserInpName(msg, error)
        msg = "Professor's last name:"
        lname = getUserInpName(msg, error)
        msg = "Professor's department:"
        department = getUserInpName(msg, error)
        msg = "Professor's email:"
        email = getUserInpEmail(msg, error)

        cl = ProfessorModel(None, fname, lname, department, email)
        print("=====================================================")
        self.ProfServ.CreateProfessor(cl)
        print("=====================================================")
        return (0,"createProfessor")
    
    def UpdateProfessor(self):
        
        print("=====================================================")
        print("To update a professor's information I will need some extra data")
        print("***If you don't want to change the data leave it blank***")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""

        msg = "Professor's id:"
        id = getUserInpInt(msg, error)
        msg = "Professor's first name:"
        fname = getUserInpName(msg, error,1)
        msg = "Professor's last name:"
        lname = getUserInpName(msg, error,1)
        msg = "Professor's department:"
        department = getUserInpName(msg, error,1)
        msg = "Professor's email:"
        email = getUserInpEmail(msg, error,1)
        #maybe use kwargs for input?
        cl = ProfessorModel(id, fname, lname, department, email)
        print("=====================================================")
        self.ProfServ.UpdateProfessor(cl)
        print("=====================================================")
        return (0,"updateProfessor")
    

    
    def ViewProfessor(self):
        
        print("=====================================================")

        self.ProfServ.ViewProfessor()

        print("=====================================================")
        return (0,"viewProfessor")
    
    def FilterProfessor(self):
        
        
        print("=====================================================")
        
        self.ProfServ.FilterProfessor()
        print("=====================================================")
        return (0,"filterProfessor")
    
    def DeleteProfessor(self):
        
        print("=====================================================")
        print("To delete a Professor I will need some extra information")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        msg = "Professor's id:"
        id = getUserInpInt(msg, error)
        
        print("=====================================================")
        self.ProfServ.DeleteProfessor(id)
        print("=====================================================")
        return (0,"deleteProfessor")
    



