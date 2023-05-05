"""Component 2 (Questions wanted) v2
Use try/accept and pull error message out of the loop """

error = "Please enter a whole number between 10 and 50 questions to be answered\n"
valid = False

# Keep asking until a valid amount (10-50) is entered
while not valid:
    try:
        # ask for questions wanted
        questions_wanted = int(input("How many questions do you want to answer? (between 10 and 50): "))

        # check if the amount is too high/low
        if 10 <= questions_wanted <= 50:
            print(f"You will be asked {questions_wanted} questions. ")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
