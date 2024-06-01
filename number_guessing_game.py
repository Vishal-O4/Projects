import random

x, y = map(int, input("Enter the range of integers separated by space:").split())
print("The range is from", x, "to", y)
num = random.randint(x, y)
f = 0
count = 0
print(num)
while not f:
    user = int(input("Guess the number:"))
    print(user)
    near = [x for x in range(num-(y//10), num+(y//10))]
    print(near)
    count += 1
    if user == num:
        f = 1
    elif user in near:
        if user > num:
            print("Your guess is near but high")
        elif user < num:
            print("Your guess is near but low")
    elif user > num:
        print("You guessed too high!")
    else:
        print("You guessed too low")
print("Game over! You guessed in ", count, " tries")
