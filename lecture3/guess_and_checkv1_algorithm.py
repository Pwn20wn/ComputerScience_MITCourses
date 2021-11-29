#Exhuastive enumeration
#find cube root of a number
#works if you're able to check if your solution is correct

#code below finds cube root of a number

cube = 8

for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)