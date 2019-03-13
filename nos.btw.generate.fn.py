print("to generate nos. btw 100-200 which are divisible by 3 but not 4")
def generate():
    for i in range(101,201):
        if i%3==0 and i%4!=0:
            print (i)
generate()
