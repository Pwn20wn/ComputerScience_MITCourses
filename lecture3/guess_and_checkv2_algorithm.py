# cube = 8

# for guess in range(cube+1):
#    if guess**3 == cube:
#        print("Cube root of", cube, "is", guess)

# two extra features
# Deal with negative cubes & tell user it's not a perfect cube
# Solves the issue of the program silently failing
cube = 8

# For loop that goes through 0-8
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        #after break, it determines whether guess is 2 or 3
        break
        #if guess is not equal to 2 or 3 then it prints out that it's not a perfect cube
    if guess**3 != abs(cube):
        print(cube, 'is not a perfect cube')
# else statement determines whether it should be a positive or negative cube
    # checks to see if the cube of the number is less than 0, if it is then it's a negative number == negative cube
    else:
        if cube < 0:
            guess = -guess
            print('Cube root of '+str(cube)+' is '+str(guess))

# limitation of the program is that it only checks perfect cubes
# sometimes we need the closest number and that's where appromixations come in