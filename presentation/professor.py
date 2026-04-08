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
            print("5) deactivate a professor")
            print("6) reactivate a professor")
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
                case "6":
                    self.ReactivateProfessor()
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
        
        
        
                

                
        

    #DONE
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
        department = getUserInpClassName(msg, error)
        msg = "Professor's email:"
        email = getUserInpEmail(msg, error)

        cl = ProfessorModel(  first_name=fname,last_name= lname,department= department,email= email)
        print("=====================================================")
        printServiceResult(self.ProfServ.CreateProfessor(cl))
        
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
        pm = ProfessorModel( id=id ,first_name=fname,last_name= lname,department= department,email= email)
        
        print("=====================================================")
        printServiceResult(self.ProfServ.UpdateProfessor(pm))
        
        return (0,"updateProfessor")
    

    
    def ViewProfessor(self):
        print("=====================================================")
        print("| ID | First Name | Last Name | Department | Email | Active |\n")
        printServiceResult(self.ProfServ.ViewProfessor())
        
    
    def FilterProfessor(self):
        
        
        print("=====================================================")
        print("Please tell me some information about the professor")
        print("***If you don't want to filter by that data leave it blank***")
        
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        print("=====================================================")
        

        msg = "Professor's first name:"
        fname = getUserInpName(msg, error,1)
        msg = "Professor's last name:"
        lname = getUserInpName(msg, error,1)
        msg = "Professor's department:"
        department = getUserInpClassName(msg, error,1)
        msg = "Professor's email:"
        email = getUserInpEmail(msg, error,1)

        pm = ProfessorModel( id=id ,first_name=fname,last_name= lname,department= department,email= email)
        printServiceResult(self.ProfServ.FilterProfessor(pm))
        
        
        return (0,"filterProfessor")
    
    def DeleteProfessor(self):
        
        print("=====================================================")
        print("To deativate a Professor I will need some extra information")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        print("=====================================================")
        msg = "Professor's id:"
        id = getUserInpInt(msg, error)
        
        
        printServiceResult(self.ProfServ.DeleteProfessor(id))
        
        return (0,"deleteProfessor")
    

    def ReactivateProfessor(self):
        
        print("=====================================================")
        print("To reactivate a Professor I will need some extra information")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        msg = "Professor's id:"
        id = getUserInpInt(msg, error)
        
        print("=====================================================")
        printServiceResult(self.ProfServ.ReactivateProfessor(id))
        
        return (0,"deleteProfessor")
    

