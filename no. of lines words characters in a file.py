fname= raw_input('enter file name to open-')
f= open(fname,'r')
text= f.read()
print'\t\tFILE CONTENTS'
print text
print'no. of characters-',len(text)
l=text.split(" ")
print'no. of words-',len(l)
l= text.split('\n')
print'no. of lines=',len(l)
