# Ask the user how confident they are in Maori numbers
show_instructions = input("Are you confident in your Maori numbers ability? : ")

# If they say yes, output 'Program Revision List'
if show_instructions == "yes":
    print("program continues")

# If they say no, output 'Display Revision List'
elif show_instructions == "no":
    print("Display revision list")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no'")