"""Component 2 (How much) v4
Changing v3 into a function
Also needed to change questions_wanted to the more generic variable name 'response',
changing the condition and position of the number comparison into the loop
to make the function recyclable"""


def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "PLease enter a number between {} and {}\n".format(low, high)

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
questions_wanted = num_check("How many questions do you want to answer? (between 10 and 50): ", 10, 50)
print(f"You will be asked {questions_wanted} questions. ")
