print("to find whether agiven character is letter or digit")
def isdigit(ch):
    if ch>='0' and ch<='9':
        return True
    else:
        return False
def isletter(ch):
    if((ch>='a' and ch<='z') or(ch>='A'and ch<='Z')):
        return True
    else:
        return False
#main program
ch= input('enter a character:-')
if(isdigit(ch)):
    print("it is a digit")
elif(isletter(ch)):
    print("it is a letter")
else:
    print("it is other than letter or digit")
