"""Component 4 (user score) v1
After test is finished, user will be graded a score for perfection and
non-perfection"""
import random
error = "Please enter a whole number between 10 and 50 questions to be answered\n"

# Ask the user how many questions they want to answer
questions_asked = int(input("How many questions do you want to answer? (between 10 and 50): "))

# check if the amount is too high/low
if 10 <= questions_asked <= 50:
    print(f"You will be asked {questions_asked} questions. ")
else:
    print(error)
    quit()


maori_numbers = {"tahi": "1",
                 "rua": "2",
                 "toru": "3",
                 "wha": "4",
                 "rima": "5",
                 "ono": "6",
                 "whitu": "7",
                 "waru": "8",
                 "iwa": "9",
                 "tekau": "10"
                 }

score = 0
number_list = list(maori_numbers.keys())
random.shuffle(number_list)
quiz_number = 0

# function to start test
while quiz_number < questions_asked:
    question = random.choice(number_list)
    answer = input(f"What is {question} in english?: ")
    if answer.lower() == maori_numbers[question]:
        print("Correct!")
        score += 1
        quiz_number += 1
    else:
        print(f"Incorrect, the correct translation for that word was {maori_numbers[question]}")
        quiz_number += 1

# function to analyze score and conclude results
if score == questions_asked:
    print(f"No revision needed! Flawless!You got {score} out of {questions_asked} correct.")
else:
    print(f"Horrible. Even my dog could do better. You got {score} out of {questions_asked} correct. "
          f"Do more revision please!")
