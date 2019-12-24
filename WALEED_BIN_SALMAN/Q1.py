
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
