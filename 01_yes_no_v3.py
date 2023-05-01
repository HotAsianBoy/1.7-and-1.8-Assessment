"""1.7 and 1.8 assessment Yes / NO
Simplifies the input by converting it to lower case. Also accepts y or n as
abbreviations. Prints result of user choice as well as input - for testing
"""

revision_list = ""
while revision_list != "x":

    # Ask the user if they are confident in their ability
    revision_list = input("Are you confident in you Maori numbers ability? : ").lower()

    # If they say yes, output 'Program Instructions'
    if revision_list == "yes" or revision_list == "y":
        print("program continues")

    # If they say no, output 'Display Revision List'
    elif revision_list == "no" or revision_list == "n":
        print("Display revision list")

    # Otherwise - show error
    else:
        print("Please answer 'yes' or 'no'")

    print(f"You entered '{revision_list}'")