import random

s1 ='''
    +---+
    |   |
        |
        |
        |
        |
  =========
'''

s2 ='''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
'''

s3 ='''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
'''

s4 ='''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
'''

s5 ='''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
'''


s6 ='''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
'''


stages = [s1, s2, s3, s4, s5, s6]

words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "pear"]

d = 6
a = random.choice(words)
colour = ['_' for _ in range(len(a))]
print(colour)

c = False
while not c:
    b = input("Guess a letter: ").lower()
    for j in range(len(a)):
        if a[j] == b:
            colour[j] = b
    print(colour)

    if b not in a:
        d -= 1
        if d == 0:
            c = True
            print("You lose")

    if '_' not in colour:
        c = True
        print("You Win!!")

    print(stages[6 - d])

