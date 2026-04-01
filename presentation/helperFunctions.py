
def getUserInpInt(message="" , error = "") -> int:
    while(True):
        try:
            print(message)
            val = int(input())
            return val
        except:
            print(error)


def getUserInpName(message="" , error = "") -> int:
    while(True):
        try:
            print(message)
            val = input().strip()
            if (val.isalpha()):
                return val
            raise
        except:
            print(error)

def getUserInpClassName(message="" , error = "") -> int:
    while(True):
        try:
            print(message)
            val = input().strip()
            if (len(val)>0):
                return val
            raise
        except:
            print(error)

def getUserInpEmail(message="" , error = "") -> int:
    import re
    while(True):
        try:
            print(message)
            val = input().strip()
            if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", val):
                return val
            raise
        except:
            print(error)