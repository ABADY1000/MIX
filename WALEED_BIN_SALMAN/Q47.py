''' Example of the output

Enter an integer...
19
 1 2 3 4 5 6 7 8 910111213141516171819181716151413121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 9101112131415161718  181716151413121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 91011121314151617      1716151413121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 910111213141516          16151413121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 9101112131415              151413121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 91011121314                  1413121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 910111213                      13121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 9101112                          121110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 91011                              1110 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 910                                  10 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 9                                       9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8                                           8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7                                               7 6 5 4 3 2 1
 1 2 3 4 5 6                                                   6 5 4 3 2 1
 1 2 3 4 5                                                       5 4 3 2 1
 1 2 3 4                                                           4 3 2 1
 1 2 3                                                               3 2 1
 1 2                                                                   2 1
 1                                                                       1

'''
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