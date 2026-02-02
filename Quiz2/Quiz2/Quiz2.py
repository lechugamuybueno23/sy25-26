import random
attempt = 5
secret = random.randint(1,10)
solved = 0
#get the number
# ask the user what number they guessed
#if they got it right, tell them they got it right
#If not keep asking until they get it right

while attempt > 0 and solved == 0:
    guess = int(input("Guess a number between 1-10: "))
    if guess <= 0 or guess > 10:
        print("only a number between 1-10")
    elif guess != secret:
        attempt = attempt - 1
        print(f"wrong, you have {attempt} attempts left")
        if guess > secret:
            print("you guessed too high")
        elif guess < secret:
            print("you guessed too low")
    elif guess == secret:
        print(f"you got it, the number was {secret}")
        solved = solved + 1
    if attempt == 0:
        print("you lost")