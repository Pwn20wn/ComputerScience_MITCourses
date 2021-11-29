#lecture 3

#strings are immutable - meaning they cannot be modified
d = "hello"
print(d)
#d[0] = 'y' this would not work as str assignment is not supported
#binds new character at the beginning and prints yello
d = 'y'+d[1:len(d)]
print(d)

s = "abcdefghjkl"
len(s)
print(len(s))
#index the first object in the string
print(s[0])
#slice a through e
print(s[0:5])
#slide string "s" and print df
print(s[3:6:2])
#personal test
#added print with length of object
#len tells number of characters in strings
w = "hacker"
len(w)
print(len(w))

