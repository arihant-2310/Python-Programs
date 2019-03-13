def add(title,copies):
    book[title]= book[title]+copies
def remove(title,copies):
    book[title]= book[title]-copies
def display():
    print'\t\tBOOK DETAILS'
    for i in sorted (book.keys()):
        print i,':',book[i]
        print
#main program
print'\t\tBOOK SHOP'
n= input('enter how many books-')
book={}
i=1
while i<=n:
    title= raw_input('enter book title-')
    copies= input('enter no.of copies -')
    book[title]= copies
    i=i+1
while True:
    display()
    choice= input('1.ADD BOOK\n 2. REMOVE BOOK \n3. DISPLAY BOOK \n4. EXIT')
    if choice==1:
        title= raw_input('enter title of the book-')
        copies= input('enter copies of the books to be added-')
        add(title,copies)
        display()
    elif choice==2:
        title= raw_input('enter title of the book sold-')
        copies= input('enter copies of the books sold-')
        remove(title,copies)
        display()
    else:
        break
        
