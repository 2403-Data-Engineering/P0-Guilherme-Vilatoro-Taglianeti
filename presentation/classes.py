from presentation.menu import Menu
from model.MClasses import ClassModel
from services.SClasses import ClassService
from presentation.helperFunctions import *

class Classes(Menu):

    ClassServ = ClassService()


    def render(self):
        while (True):
            print("=====================================================")
            print("You are in the classes screen")
            print("What would you like to administer today?")
            print("1) create a class")
            print("2) update a class")
            print("3) view all classes")
            print("4) search for classes")
            print("5) delete a class")
            print("6) reactivate a class")
            print("b) Back")
            print("q) Quit")
            print("=====================================================")

        
            inp = input().lower()
            
            match inp:
                case "1":
                    self.CreateClass()
                    
                case "2":
                    self.UpdateClass()

                case "3":
                    self.ViewClass()
                    
                case "4":
                    self.FilterClass()
                    
                case "5":
                    self.DeleteClass()
                case "6":
                    self.ReactivateClass()
                case "b":
                    return (0,"MainMenu")
                    
                case "q":
                    print("=====================================================")
                    print("Thank you for utilizing our Admin Portal")
                    print("=====================================================")
                    return (1,"Quit")
                case _:
                    print("=====================================================")
                    print("Unregistered key\""+ inp +"\", please try again.")
                    print("=====================================================")
        
        
        
                

                
        


    def CreateClass(self):
       
            
        print("=====================================================")
        print("To create a class I will need some extra information")

        msg = """professor ID that will teach the class:"""
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        id = getUserInpInt(msg, error)


        msg = "class name:"
        name = getUserInpClassName(msg, error)

        cl = ClassModel(prof_id=id, name=name)
        print("=====================================================")
        e,m = self.ClassServ.CreateClass(cl)
        print("m")
        return (0,"createClass")
    
    def UpdateClass(self):
        
        print("=====================================================")
        print("To update a class name I will need some extra information")
        msg = """class ID:"""
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        id = getUserInpInt(msg, error)
        
        msg ="new class name:"
        name = getUserInpClassName(msg, error)
        msg ="new professor ID:"
        prof_id = getUserInpInt(msg, error, True)
        cl = ClassModel(id=id, name=name, prof_id=prof_id)
        print("=====================================================")
        self.ClassServ.UpdateClass(cl)
        print("=====================================================")
        return (0,"updateClass")
    
    
    def ViewClass(self):
        
        print("=====================================================")

        _,r =self.ClassServ.ViewClass()
        for c in r:
            print(c)
        
        
        return (0,"viewClass")
    
    def FilterClass(self):
        
        print("=====================================================")
        print("To filter a class I will need some extra information")

        msg = """professor ID that teaches the class:"""
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        prof_id = getUserInpInt(msg, error)
        msg = """class ID:"""
        id = getUserInpInt(msg, error)
        _, r = self.ClassServ.FilterClass(ClassModel(id= id, name="temp",prof_id = prof_id))
        print(r)
        return (0,"filterClass")
    
    def DeleteClass(self):
        
        
        print("=====================================================")
        print("To delete a class I will need some extra information")

        msg = """class ID:"""
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""

        id = getUserInpInt(msg, error)
        
        print("=====================================================")
        self.ClassServ.DeleteClass(id)
        print("=====================================================")
        return (0,"deleteClass")

    def ReactivateClass(self):
        
        
        print("=====================================================")
        print("To reactivate a class I will need some extra information")

        msg = """class ID:"""
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""

        id = getUserInpInt(msg, error)
        
        print("=====================================================")
        self.ClassServ.ReactivateClass(id)
        print("=====================================================")
        return (0,"ActivateClass")
    



