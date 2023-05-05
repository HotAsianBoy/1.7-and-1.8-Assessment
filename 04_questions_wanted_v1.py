"""Component 2 (Questions wanted) v1
Ask user how many question they want to answer (between 10 and 50)"""


questions_wanted = int(input("How many questions do you want to answer? (between 10 and 50): "))

# Keep asking until a valid amount (10-50) is entered
while not 10 <= questions_wanted <= 50:
    print("Try again. Please enter a whole number between 10 and 50 questions to be answered. ")
    # ask for the input
    questions_wanted = int(input("How many questions do you want to answer? (between 10 and 50): "))

print(f"You are will be asked {questions_wanted} questions. ")
