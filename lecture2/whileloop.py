print ("""
    ***********************
    ***********************
       :)
    ***********************
    ***********************

    Go left or right
""")

n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
else:
    print("You got out of the Lost Forest! \o/")

# to-do create a counter if user inputs right more than two times return sad face
# if user puts right more than 4 times return funny flip over table
