st= raw_input('enter string-')
l= st.split(" ")
(mx,word)=(0," ")
for i in l:
    if len(i)>mx:
        (mx,word)=(len(i),i)
print'longest word-',word
print'maximun length-',mx
