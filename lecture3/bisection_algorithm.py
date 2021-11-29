# Helps when the search space is large
# The example in the lecture was to guess a number between 0 & 100 in under 10 guesses
# student picks a number
# Start with guessing if the number was 50, if not then asked if it was larger or smaller
# since the number was larger, then 0-50 was eliminated from the search and so on until the number was found

# half interval each iteration
# new guess is halfway in between


# bisection search convergence
# search space first guess n/2
# 2nd guess n/4
# kth guess n/2^k

# guess converges on the order of log^2N steps
# bisection search works when value of function varies monotonically with input
# code as show only works for positive cubes >1 - why?
# challenges
## 1) modify to work with negative cubes!
## 2) modify to work with x <1

#current program goes into infinite loop
#working on finding if statement
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
        guess = (high + low)/2.0
        num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
