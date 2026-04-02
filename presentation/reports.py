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
        
        
        print("=====================================================")
        self.ReportServ.StudentReport(id)
        print("=====================================================")
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
        data = self.ReportServ.ProfessorReport(id)
        print("=====================================================")
        self.GenerateProfessorReport(data)
        return (0,"ProfessorReport")
    
    def GenerateProfessorReport(self, data):
        
        from yattag import Doc
        from datetime import datetime

        table_style = "border-collapse: collapse; width: 100%; margin: 20px 0; font-family: Arial, sans-serif; box-shadow: 0 2px 8px rgba(0,0,0,0.15);"
        th_style = "background-color: #4a90d9; color: white; padding: 12px 15px; text-align: left; font-size: 14px;"
        td_style = "padding: 10px 15px; border-bottom: 1px solid #ddd; font-size: 14px;"
        tr_even_style = "background-color: #f3f3f3;"

        doc, tag, text = Doc().tagtext()

        doc.asis('<!DOCTYPE html>')
        with tag('html'):
            with tag('head'):
                with tag('title'):
                    text('Professor Report')
            with tag('body'):
                with tag('h1'):
                    text('Professor Report')
                with tag('table', id='prof-table' , style=table_style):
                    with tag('thead'):
                        with tag('tr'):
                            with tag('th', style=th_style):
                                text("First Name")
                            with tag('th' , style=th_style):
                                text("Last Name")
                            with tag('th' , style=th_style):
                                text("Class Name")
                            with tag('th', style=th_style):
                                text("Class ID")
                    with tag('tbody'):
                        with tag('tr'):
                            with tag('td',  style=td_style):
                                text("John")
                            with tag('td'  , style=td_style):
                                text("Doe")
                            with tag('td',  style=td_style):
                                text("History")
                            with tag('td',  style=td_style):
                                text("1234")
                with tag('table', id='student-table', style=table_style + "margin-top: 40px;"):
                        with tag('thead'):
                            with tag('tr'):
                                with tag('th' , style=th_style):
                                    text("Student names")
                                with tag('th' , style=th_style):
                                    text(" ")
                                with tag('th' , style=th_style):
                                    text(" ")
                                with tag('th' , style=th_style):
                                    text(" ")
                        with tag('tbody'):
                            with tag('tr'):
                                with tag('td',  style=td_style):
                                    text("John Sam")
                                with tag('td',  style=td_style):
                                    text("Doe Doe")
                                with tag('td',  style=td_style):
                                    text("clara")
                                with tag('td',  style=td_style):
                                    text("Robin")
                            with tag('tr',  style=tr_even_style):
                                with tag('td',  style=td_style):
                                    text("John Sam")
                                with tag('td',  style=td_style):
                                    text("Doe Doe")
                                with tag('td',  style=td_style):
                                    text("clara")
                                
                            
                            
                   

        result = doc.getvalue()
        ts = datetime.now().timestamp()
        path = "ProfessorReport-" + str(int(ts)) + ".html"
        
        with open(path, "w") as f:
            f.write(result)


'''with tag('tbody'):
    for i, student in enumerate(students):
        if i % 4 == 0:              # start a new row every 4 students
            if i != 0:
                doc.asis('</tr>')   # close the previous row
            doc.asis('<tr>')        # open a new row
        with tag('td', style=td_style):
            text(student.name)
    doc.asis('</tr>')'''

