# good enough solution
# start with a guess and increment by some small value
# keep guessing if | guess**3 - cube | >+ epsilon for some small epsilon aka as long as we're not close enough
# the epsilon is too small at first for numbers like 27
# to find the square root of 10000, if the epsilon increment becomes too large
# It skips over the perfect epsilon and makes this program an infinite loop based on the code on line 16
# the and clause on line 16 helps it make sure it's less than cube
#cube = 27
#cube = 8120601
cube = 10000
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
