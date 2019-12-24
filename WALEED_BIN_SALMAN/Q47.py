
number = int(input("Enter an integer...\n"))

L = len(str(number))

text=""
counter = number
for z in range(number):
    temp_text = str("".join([str(i).rjust(L," ") for i in range(1,number+1)] + [str(i).rjust(L," ") for i in range(number-1,0,-1)]))
    
    for j in range(number, counter, -1):
        temp_text = temp_text.replace(str(j), " "*len(str(j)), 2)
    counter -= 1  

    text += temp_text
    text += "\n"
print(text)