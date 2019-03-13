print("program to read number of lines, words and characters from a file")
fname= input("enter file name to be read")
lines=0
words=0
characters=0
f= open(fname,'r')
for line in f:
    wordlist= line.split(" ")
    lines= lines+1
    words= words+len(wordlist)
    characters= characters+ len(line)
print("lines=",lines)
print("words=",words)
print("characters=",characters)
