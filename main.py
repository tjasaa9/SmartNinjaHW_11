#HW 11
import datetime
import json
import random

secret = random.randint(1, 10)
attempts = 0

name = input("Please enter your name here: ")

with open("score_list.json", "r") as score_file:
    top_score =json.loads(score_file.read())
    #top_score.sort()
    #print(top_score[:3])

new_top_score = sorted(top_score, key=lambda k: k['attempts'])[:3]

for score_dict in new_top_score:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + " - " +  score_dict.get("name"))



while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    attempts += 1

    if guess == secret:
        top_score.append({"attempts": attempts, "date": str(datetime.datetime.now()),"name": name, "secret": secret})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(top_score))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")