"""Took functions from component 03_v1 as the basis for this function which
incorporates both yes/no and show instructions"""


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
    print("The Maori numbers from 1-10 will go here")
    print()
    print("Program continues")
    print()


# Main routine go here...
confidence_ability = yes_no("Are you confident in your Maori numbers ability? ")

if confidence_ability == "No":
    revision()
else:
    print("Program continues")