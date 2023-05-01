"""Yes/No checking function
based on 01_yes_no_v3
"""


# Functions go here...
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


# Main routine go here...
revision_list = yes_no("Are you confident in your Maori numbers ability? ")
print(f"You entered '{revision_list}'")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")