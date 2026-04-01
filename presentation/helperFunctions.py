
def getUserInpInt(message="" , error = "") -> int:
    while(True):
        try:
            print(message)
            val = int(input())
            
            return val
        except KeyboardInterrupt:
            quit()
        except:
            print(error)


def getUserInpName(message="" , error = "", skipable = False) -> int:
    while(True):
        try:
            print(message)
            val = input().strip()
            if (val.isalpha() or (skipable == True and len(val) == 0)):
                return val
            raise
        except KeyboardInterrupt:
            quit()
        except:
            print(error)

def getUserInpClassName(message="" , error = "", skipable = False) -> int:
    while(True):
        try:
            print(message)
            val = input().strip()
            if (len(val)>0 or (skipable == True and len(val) == 0)):
                return val
            raise
        except KeyboardInterrupt:
            quit()
        except:
            print(error)

def getUserInpEmail(message="" , error = "", skipable = False) -> int:
    import re
    while(True):
        try:
            print(message)
            val = input().strip()
            if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", val) or (skipable == True and len(val) == 0):
                return val
            raise
        except KeyboardInterrupt:
            quit()
        except:
            print(error)

def getUserInpYear(message="" , error = "", skipable = False) -> int:
    import re
    while(True):
        try:
            print(message)
            val = input().strip().lower()
            if (re.match(r"^freshman|sophomore|junior|senior$", val) or (skipable == True and len(val) == 0)):
                return val
            raise
        except KeyboardInterrupt:
            quit()
        except:
            print(error)

            