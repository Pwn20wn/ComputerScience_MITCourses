#checks string to determine if the letter i or u exists across the index
s = "christian"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u in your name")

#checks to see if the characters i or u exist in the street name
#more pythonic
street_name = "birdhouse road"
for char in street_name:
    if char == 'i' or char == 'u':
        print("There is an i or u in the street name")