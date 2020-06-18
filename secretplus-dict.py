import random
import datetime

secret = random.randint(1, 30)
attempts = 0
current_time = datetime.datetime.now()


with open("score.txt", "r") as score_file:
    lowest_score = int(score_file.read())
    print("The current low score is " + str(lowest_score))

for score_dict in lowest_score:
    print(str(score_dict["attempts"] + "attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1 # syntactic sugar für [ attempts = attempts + 1 ]
    # sog. Zählvariable - bei jeder Schleife, steigt der Wert der VAR um 1)

    if guess == secret:
        lowest_score.append({"attempts": attempts, "date": str(datetime.datetime.now)})

        with open("score.txt", "w") as score_file:
            score_file.write(str(attempts))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
