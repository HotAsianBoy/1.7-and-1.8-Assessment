"""Component 3 (random Maori numbers) v2
Generates random choice of Maori numbers in random order"""

import random
Tahi = 1
Rua = 2
Toru = 3
Wha = 4
Rima = 5
Ono = 6
Whitu = 7
Waru = 8
Iwa = 9
Tekau = 10

numbers = input(f"{Tahi, Rua, Toru, Wha, Rima, Ono, Whitu, Waru, Iwa, Tekau, }, ")
number = random.choice(numbers)
random.shuffle(numbers)

question = input(f"What number is {number} ?: ")
user_answer = input(question).lower()

if user_answer == number:
    print(f"Correct! What number is {number} ?: ")
