string = input("Give me a string: ")
print("The string you gave is \"", string, "\"")
length = len(string)
print("the string is ",length, " characters long")
punctlist = [","," ",".","!","'",":"]
print(punctlist)


def removespaces(stringToBeCleaned):
    position = 0
    clean = ""
    while position < length:
        cleanletter = stringToBeCleaned[position]
        # if cleanletter != " " and cleanletter != "." and cleanletter != ":" and cleanletter != "," and cleanletter != "'":
        if cleanletter not in punctlist:
            clean = clean + cleanletter
        position += 1
    return clean

cleanstring = removespaces(string)
print("If you clean it, that would be \"",cleanstring,"\"")

cleanlength = len(cleanstring)
print("the cleaned string is ",cleanlength, "characters long")

backwards = ""


p = cleanlength - 1
while p >= 0:
    letter = cleanstring[p]
    backwards = backwards + letter
    p -= 1
print("and if you make the cleanstring backwards you get \"",backwards,"\"")

if backwards == cleanstring:
    print ("You have a palindrome HURRAH")
else: 
    print("You do not have a palindrome. Try again.")

