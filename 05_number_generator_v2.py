"""Component 3 (random Maori numbers) v2
Generates random choice of Maori numbers in random order"""
import random

questions_wanted = int(input("How many questions do you want to answer? (between 10 and 50): "))

error = "Please enter a whole number between 10 and 50 questions to be answered\n"

# check if the amount is too high/low
if 10 <= questions_wanted <= 50:
    print(f"You will be asked {questions_wanted} questions. ")
    valid = True
else:
    print("Invalid input. Please enter a number between 10 and 50 to be asked. Thank you. ")

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

while quiz_number <= questions_wanted / 2:
    for num in number_list:
        answer = input(f"What is {num} in english?: ")
        if answer.lower() == maori_numbers[num]:
            print("Correct!")
            score += 1
            quiz_number += 1
        else:
            print(f"Incorrect, the correct translation for that word was {maori_numbers[num]}")
            quiz_number += 1

if score < 5:
    print(f"Really poor effort. You got {score} out of {questions_wanted} correct. ")
elif score < 10:
    print(f"You need some more revision. You got {score} out of {questions_wanted} correct.")
elif score < 20:
    print(f"Not bad! You got {score} out of {questions_wanted} correct.")
elif score < 30:
    print(f"Good! You got {score} out of {questions_wanted} correct.")
elif score == questions_wanted:
    print(f"Perfection! You got {score} out of {questions_wanted} correct.")
else:
    print(f"Horrible. Even my dog could do better. You got {score} out of {questions_wanted} correct. ")

