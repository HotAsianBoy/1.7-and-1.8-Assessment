"""Component 3 (random Maori numbers) v1
Generates random choice of Maori numbers in random order"""

import random

numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]

# Testing loop to generate 20 random Maori numbers
for item in range(20):
    number = random.choice(numbers)
    print(number, end='\t')  # can wrap output making it easier to screenshot
