

class Menu:
    def __init__(self):
        pass
    def render(self):
        print("Sample Menu")

    


class MainMenu(Menu):
    
    def render(self):
        while (True):
            from presentation.classes import Classes
            from presentation.professor import Professor
            from presentation.student import Student
            print("=====================================================")
            print("Welcome to Revature University Administration Portal")
            print("What would you like to administer today?")
            print("1) Professors")
            print("2) Classes")
            print("3) Students")
            print("4) Reports")
            print("q) Quit")
            print("=====================================================")


            inp = input().lower()
            
            match inp:
                case "1":

                    return Professor().render()
                    
                case "2":
                    classes = Classes()
                    
                    return classes.render()
                    
                case "3":
                    return Student().render()
                    
                case "4":
                    return (0,reports)
                    
                    
                case "q":
                    print("=====================================================")
                    print("Thank you for utilizing our Admin Portal")
                    print("=====================================================")
                    return (1, "Quit")
                case _:
                    print("=====================================================")
                    print("Unregistered key \""+ inp +"\", please try again.")
                    print("=====================================================")
                


            
                







