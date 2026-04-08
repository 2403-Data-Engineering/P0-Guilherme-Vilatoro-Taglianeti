from presentation.menu import Menu
from services.SReport import ReportService
from presentation.helperFunctions import *

class Report(Menu):

    ReportServ = ReportService()


    def render(self):
        while (True):
            print("=====================================================")
            print("You are in the reports screen")
            print("What would you like to administer today?")
            print("1) student enrollment report")
            print("2) professor summary report")
            print("b) Back")
            print("q) Quit")
            print("=====================================================")

        
            inp = input().lower()
            
            match inp:
                case "1":
                    self.StudentReport()
                    
                case "2":
                    self.ProfessorReport()

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
        
        
        
                

                
        


    def StudentReport(self):
       
            
        print("=====================================================")
        print("To generate a student's report I will need some extra data")
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""
        

        msg = "Student's id:"
        id = getUserInpInt(msg, error)
        
        
        try:
            res,data  = self.ReportServ.StudentReport(id)

            if res == 1:
                print(f"""*****************************************************
Error: {data}
*****************************************************""")
                return(1,data)
        except:
            print("""*****************************************************
Error: when trying to generate a student's report
*****************************************************""")



        print("=====================================================")

        print("File saved as "+ data)

        return (0,"StudentReport")





    def ProfessorReport(self):
        
        print("=====================================================")
        print("To generate a professor's report I will need some extra data")
        
        error = """*****************************************************
Error: Data provided is incorrect or invalid.
*****************************************************"""

        msg = "Professor's id:"
        id = getUserInpInt(msg, error)
        
        
        print("=====================================================")
        try:
            res,data = self.ReportServ.ProfessorReport(id)
            if res == 1:
                print(f"""*****************************************************
Error: {data}
*****************************************************""")
                return(1,data)
        except:
            print("""*****************************************************
Error: when trying to generate a professor report
*****************************************************""")
        print("File saved as "+data)
       
        return (0,"ProfessorReport")
    
   