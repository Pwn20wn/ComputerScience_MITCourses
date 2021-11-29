##Original Author: Ana Bell MIT Professor
#Using code to follow along Lecture 3 for String Manipulation, Guess and Check, Approximation, and Bisection

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiam level (1-10): "))

i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "!" + " " + char)
    else:
        print("Give me a " + char + "!" + " " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")
