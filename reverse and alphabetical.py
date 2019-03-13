st= raw_input('enter string:-')
l= st.split(" ")
l= l[::-1]
rev= " ".join(l)
print'reverse is-'
print rev
l.sort()
alpha= " ".join(l)
print'alphabetical is-',alpha
