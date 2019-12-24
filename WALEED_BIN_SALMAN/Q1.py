''' Example of the output

enter an integer...
15
 1  0  0  0  0  0  0  0  0  0  0  0  0  0  0 
 0  2  0  0  0  0  0  0  0  0  0  0  0  0  0
 0  0  3  0  0  0  0  0  0  0  0  0  0  0  0
 0  0  0  4  0  0  0  0  0  0  0  0  0  0  0
 0  0  0  0  5  0  0  0  0  0  0  0  0  0  0
 0  0  0  0  0  6  0  0  0  0  0  0  0  0  0
 0  0  0  0  0  0  7  0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  8  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0  9  0  0  0  0  0  0
 0  0  0  0  0  0  0  0  0 10  0  0  0  0  0
 0  0  0  0  0  0  0  0  0  0 11  0  0  0  0
 0  0  0  0  0  0  0  0  0  0  0 12  0  0  0
 0  0  0  0  0  0  0  0  0  0  0  0 13  0  0
 0  0  0  0  0  0  0  0  0  0  0  0  0 14  0
 0  0  0  0  0  0  0  0  0  0  0  0  0  0 15

'''


number = int(input("enter an integer...\n"))

text = ""

for c in range(1, number+1):
    for r in range(1,number+2):
        if c == r:
            text += "{:2d} ".format(r)
        elif r == number+1:
            text += "\n"
        else:
            text += "{:2d} ".format(0)

print(text)
