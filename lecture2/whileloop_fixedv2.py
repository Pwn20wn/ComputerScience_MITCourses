print("""
    ***********************
    ***********************
       :)
    ***********************
    ***********************
    
    Go left or right
""")

#n = input("You're in the Lost Forest. Go left or right? ")
#while n == "right":
#    n = input("You're in the Lost Forest. Go left or right? ")
#print("You got out of the Lost Forest! \o/")

#to-do create a counter if user inputs right more than two times return sad face
#if user puts right more than 4 times return funny flip over table

def forest_question(path_check):
    if path_check == "right":
        print("Interesting choice")
        return True
    if path_check == "left":
        print("On the right path")
    return False
counter = 0
direction = forest_question(str)
direction_question: str = str(input("You're in the Lost Forest. Go left or right? "))
while direction_question == "right":
    direction_question = str(input("You're in the Lost Forest. Go left or right? "))
    counter = counter+1
    if counter > 2:
        print("Interesting choice.")
        #print(direction_question)
    if counter > 3:
        print("Interesting choice..")
        #print(direction_question)
    if counter > 4:
        print("Interesting choice...")
        #print(direction_question)
    if counter > 5:
        print ("""***********************
                  ***********************
                       :(
                  ***********************
                  ***********************

                 Go left or right""")
        if counter == 6:
            print ("""***********************
                      ********   ***********
                        ARGGHH! *FLIPS TABLE OVER*
                      ***********************
                      ***********************

                     Go left or right""")
        #print(direction_question)
    c = 0
    while direction_question == "left":
        direction_question = str(input ("You're in the Lost Forest. Go left or right? "))
        c = c+1
        if counter <= 1:
            print ("""***********************
                              ***********************
                                   :( dude get me out
                              ***********************
                              ***********************

                             Go left or right""")
        if c == 2:
            print("Wooo you've left the forest \o/")
            raise SystemExit








#forest_question = input("You're in the Lost Forest. Go left or right? ")
#while forest_question == "right":
    #counter = counter+1
    #if counter == 1:
        #return forest_question
    #print("Keep going")
   # if counter == 2:
        #print("""
                #***********************
               # ***********************
               #    :(
               # ***********************
               # ***********************

               # Go left or right
        # """)
    #if counter == 3:
#return forest_question
   # else:
        #print ("You got out of the Lost Forest! \o/")
       # raise SystemExit
