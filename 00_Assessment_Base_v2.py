"""00_Assessment_Base_v2
Removes few unnecessary things from v1 and improves aesthetics"""
# Ask the user if they have played before
import random


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they are confident in their Maori numbers ability
        answer = input(question_text).lower()

        # If they say yes, output 'Program Revision List'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Revision List'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# function to display instructions
def revision():
    print("**** Maori Numbers 1-10 ****")
    print()
    print("The Maori numbers from 1-10 are: ")
    print("Tahi - 1 ")
    print("Rua - 2 ")
    print("Toru - 3 ")
    print("Wha - 4 ")
    print("Rima - 5 ")
    print("Ono - 6 ")
    print("Whitu - 7 ")
    print("Waru - 8 ")
    print("Iwa - 9 ")
    print("Tekau - 10 ")
    print()

    print("*" * 50)
    print()


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine go here...
print(formatter("*", "Welcome to the Maori Revision Game!"))
print()

confidence_ability = yes_no("Are you confident in your Maori number ability? ")
if confidence_ability == "No":
    revision()
else:
    print("Really??? Then Let's Go!")


def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (10-50) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check or number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
error_ = "Please enter a whole number between 10 and 50 questions to be answered"
# Ask the user how many questions they want to answer
questions_asked = int(input("How many questions do you want to answer? (between 10 and 50): "))

# check if the amount is too high/low
if 10 <= questions_asked <= 50:
    print(f"You will be asked {questions_asked} questions. ")
else:
    print(error_)
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
        print("*** Correct! ***")
        score += 1
        quiz_number += 1
    else:
        print(f"/// Incorrect, the correct translation for that word was {maori_numbers[question]} ///")
        quiz_number += 1

# function to analyze score and conclude results
if score == questions_asked:
    print(f"No revision needed! Flawless! You got {score} out of {questions_asked} correct.")
elif score == 0:
    print(f"Really! Zero?? Are you trolling?? You got {score} ??? Please do some MORE REVISION ASAP! ")
elif 10 <= questions_asked <= 20:
    print(f"Not bad! You got {score} out of {questions_asked} correct.")
elif 20 <= questions_asked <= 30:
    print(f"Well Done! You got {score} out of {questions_asked} correct.")
elif 30 <= questions_asked <= 40:
    print(f"Wow! You are getting good! You got {score} out of {questions_asked} correct.")
elif questions_asked >= 40:
    print(f"What a pro ! You got {score} out of {questions_asked} correct. Revision not needed anymore!")
else:
    print(f"Horrible. Even my dog could do better. You got {score} out of {questions_asked} correct. "
          f"Do more revision please!")
print()
print(formatter("#", "Thanks for doing your revision! Please come again anytime! Farewell! "))