
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