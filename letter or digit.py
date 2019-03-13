def isletter():
    if (ch>='a'and ch<='z')or (ch>='A' and ch<='Z'):
        return True
    else:
        return False
def isdigit():
    if(ch>='0'and ch<='9'):
        return True
    else:
        return False
#main Program
ch = raw_input('enter any character-')
if isletter():
    print'it is a letter'
elif isdigit():
    print'it is a digit'
else:
    print'it is other than letter or digit'
    
