from data.reportDAO import ReportDAO
from itertools import groupby


class ReportService:
    repDao= ReportDAO()
    def StudentReport(self, id: int):
        
        try:    
            res,d = self.repDao.getStudentReportData(id)
        except:
            return(res,d)
        try:
            res,d = self.GenerateStudentReport(d)
        except:
            return(1,"Failed to generate professor report")
        return (res,d)
    
    
    def ProfessorReport(self, id : int):
        
        try:
            res,d = self.repDao.getProfessorReportData(id)

        except:
            return(res, d)
        try:
            res,d= self.GenerateProfessorReport(d)
        except:
            return(1,"Failed to generate professor report")
        return (res, d)
    

    def GenerateStudentReport(self, data):

        from yattag import Doc
        from datetime import datetime

        table_style = "border-collapse: collapse; width: 100%; margin: 20px 0; font-family: Arial, sans-serif; box-shadow: 0 2px 8px rgba(0,0,0,0.15);"
        th_style = "background-color: #4a90d9; color: white; padding: 12px 15px; text-align: left; font-size: 14px;"
        td_style = "padding: 10px 15px; border-bottom: 1px solid #ddd; font-size: 14px;"
        tr_even_style = "background-color: #f3f3f3;"
        curr_style = tr_even_style
        doc, tag, text = Doc().tagtext()

        doc.asis('<!DOCTYPE html>')
        with tag('html'):
            with tag('head'):
                with tag('title'):
                    text('Student Report')
            with tag('body'):
                with tag('h1'):
                    text('Student Report')
                with tag('table', id='prof-table' , style=table_style):
                    with tag('thead'):
                        with tag('tr'):
                            with tag('th', style=th_style):
                                text("First Name")
                            with tag('th' , style=th_style):
                                text("Last Name")
                            with tag('th' , style=th_style):
                                text("Email")
                            with tag('th', style=th_style):
                                text("Major")
                    with tag('tbody'):
                        with tag('tr'):
                            with tag('td',  style=td_style):
                                text(data[0].student_first_name)
                            with tag('td'  , style=td_style):
                                text(data[0].student_last_name)
                            with tag('td',  style=td_style):
                                text(data[0].student_email)
                            with tag('td',  style=td_style):
                                text(data[0].student_major)
                with tag('table', id='class-table', style=table_style + "margin-top: 40px;"):
                        with tag('thead'):
                            with tag('tr'):
                                with tag('th' , style=th_style):
                                    text("class id")
                                with tag('th' , style=th_style):
                                    text("class name")
                                with tag('th' , style=th_style):
                                    text("professor name")
                        with tag('tbody'):
                            for row in data:
                                if curr_style == "":
                                    curr_style = tr_even_style
                                else:
                                    curr_style = ""
                                with tag('tr', style = curr_style):
                                    with tag('td',  style=td_style):
                                        text(row.class_id)
                                    with tag('td',  style=td_style):
                                        text(row.class_name)
                                    with tag('td',  style=td_style):
                                        text(row.professor_first_name+ " " + row.professor_last_name)
                                    
                                   
                                
                            
                            
                   

        result = doc.getvalue()
        ts = datetime.now().timestamp()
        path = "StudentReport-"+ data[0].student_first_name+ data[0].student_last_name+ "-"+str(int(ts)) + ".html"
        
        with open(path, "w") as f:
            f.write(result)
        return(0,path)



    



    #need implementation
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
                                text("Department")
                            with tag('th', style=th_style):
                                text("Email")
                    with tag('tbody'):
                        with tag('tr'):
                            with tag('td',  style=td_style):
                                text(data[0].professor_first_name)
                            with tag('td'  , style=td_style):
                                text(data[0].professor_last_name)
                            with tag('td',  style=td_style):
                                text(data[0].professor_department)
                            with tag('td',  style=td_style):
                                text(data[0].professor_email)
            grouped_data = groupby(data, key=lambda r: r.class_id)
            for class_id, students in grouped_data:
                students = list(students)  
                first = students[0]       

                with tag('table', id=f'class-table-{class_id}', style=table_style + "margin-top: 40px;"):
                    with tag('thead'):
                        with tag('tr'):
                            with tag('th', style=th_style):
                                text(f"Class ID: {str(first.class_id)}")
                            with tag('th', style=th_style):
                                text(first.class_name)
                            with tag('th', style=th_style):
                                text("")

                    with tag('tbody'):
                        for row in students:
                            with tag('tr'):
                                with tag('td', style=td_style):
                                    text(row.student_first_name)
                                with tag('td', style=td_style):
                                    text(row.student_last_name)
                                with tag('td', style=td_style):
                                    text(row.student_email)
                                   
                                
                            
                            
                   

        result = doc.getvalue()
        ts = datetime.now().timestamp()
        path = "ProfessorReport-"+data[0].professor_first_name + data[0].professor_last_name + "-" + str(int(ts)) + ".html"
        
        with open(path, "w") as f:
            f.write(result)
        
        return(0,path)
