import random


words = ["apple", "banana", "orange", "guava", "lemon", "pomegrante"]

word = random.choice(words)
guess = ""
flag = 0
chances = len(word) + 2

while not flag and chances != 0:
    chances -= 1
    ipt = input("\nEnter a character:")

    if ipt not in word:
        print("Not a character")
    elif ipt in guess:
        print("Character already guessed")
    else:
        guess += ipt
        count = 0

        for i in word:
            if i in guess:
                print(i, end=" ")
                count += 1
            else:
                print("_", end=" ")

            if count == len(word):
                print("\nCongratulations! You win!")
                flag = 1
                break


