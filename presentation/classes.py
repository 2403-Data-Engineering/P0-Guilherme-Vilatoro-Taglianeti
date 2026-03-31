from presentation.menu import Menu
from model.classes import ClassModel
from services.classes import ClassService

class Classes(Menu):

    ClassServ = ClassService()


    def render(self):
        while (True):
            print("=====================================================")
            print("You are in the classes screen")
            print("What would you like to administer today?")
            print("1) create a class")
            print("2) update a class name")
            print("3) update the professor teaching a class")
            print("4) view all classes")
            print("5) search for classes")
            print("6) delete a class")
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
                    self.UpdateClassProfessor()

                case "4":
                    self.ViewClass()
                    
                case "5":
                    self.FilterClass()
                    
                case "6":
                    self.DeleteClass()
                case "b":
                    return (0,"MainMenu")
                    
                case "q":
                    print("=====================================================")
                    print("Thank you for utilizing our Admin Portal")
                    print("=====================================================")
                    return (1,"Quit")
                

                
        


    def CreateClass(self):
        
        
        print("=====================================================")
        print("To create a class I will need some extra information")
        print("professor ID that will teach the class:")
        id  = int(input())
        print("class name:")
        name = input()
        cl = ClassModel(id, name)
        print("=====================================================")
        self.ClassServ.CreateClass(cl)
        print("=====================================================")
        return (0,"createClass")
    
    def UpdateClass(self):
        
        
        print("=====================================================")
        print("To update a class I will need some extra information")
        print("class ID:")
        id  = int(input())
        print("new class name:")
        name = input()
        cl = ClassModel(id, name)
        print("=====================================================")
        self.ClassServ.UpdateClass(cl)
        print("=====================================================")
        return (0,"updateClass")
    
    def UpdateClassProfessor(self):
        
        
        print("=====================================================")
        print("To update a class professor I will need some extra information")
        print("class ID:")
        id  = int(input())
        print("new professor ID:")
        id2 = input()
        cl = ClassModel(id, "")
        print("=====================================================")
        self.ClassServ.UpdateClassProfessor(cl, id2)
        print("=====================================================")
        return (0,"updateClassProfessor")
    
    def ViewClass(self):
        
        print("=====================================================")

        self.ClassServ.ViewClass()

        print("=====================================================")
        return (0,"viewClass")
    
    def FilterClass(self):
        
        
        print("=====================================================")
        
        self.ClassServ.FilterClass()
        print("=====================================================")
        return (0,"filterClass")
    
    def DeleteClass(self):
        
        
        print("=====================================================")
        print("To delete a class I will need some extra information")
        print("class ID")
        id  = int(input())
        
        cl = ClassModel(id, "")
        print("=====================================================")
        self.ClassServ.DeleteClass(cl)
        print("=====================================================")
        return (0,"deleteClass")
    



