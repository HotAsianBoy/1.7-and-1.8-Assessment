"""Component 2 (Questions wanted) v3
More efficient method - include valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable"""

# Main routine
error = "That was not a valid input\n"
questions_wanted = 0

# Keep asking until a valid amount (10-50) is entered
while not 10 <= questions_wanted <= 50:
    try:
        # ask for amount
        questions_wanted = int(input("Please enter a whole number between 10 and 50"
                                 "\nHow many questions would you like to answer? "))
        print()

    except ValueError:
        print(error)

print(f"You will be asked {questions_wanted} questions. ")
