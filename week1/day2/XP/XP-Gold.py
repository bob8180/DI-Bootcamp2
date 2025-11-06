import random

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# #Concatenate without using +
# for item in list2:
#     list1.append(item)
# print(list1)

# for num in range(1500, 2501):
#     if num % 5 == 0 or num % 7 == 0:
#         print(num)

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_name = input("Enter your name: ")
# if user_name in names:
#     print(names.index(user_name))

# numbers = []    
# for i in range(3):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# print("The greatest number is:", max(numbers))

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# vowels = 'aeiou'

# for letter in alphabet:
#     if letter in vowels:
#         print(f"{letter} is a vowel")
#     else:
#         print(f"{letter} is a consonant")

# words = []
# for i in range(7):
#     word = input(f"Enter word {i+1}: ")
#     words.append(word)

# letter = input("Enter a single character: ")

# for word in words:
#     if letter in word:
#         print(f"In word '{word}', '{letter}' first appears at index {word.index(letter)}.")
#     else:
#         print(f"The letter '{letter}' does not exist in the word '{word}'.")

# input_str = input("Enter comma-separated numbers: ")
# numbers_list = input_str.split(",")
# numbers_tuple = tuple(numbers_list)
# print("List:", numbers_list)
# print("Tuple:", numbers_tuple)

wins = 0
losses = 0

while True:
    user_input = input("Guess a number from 1 to 9 (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    if not user_input.isdigit() or not (1 <= int(user_input) <= 9):
        print("Please enter a valid number between 1 and 9.")
        continue
    user_guess = int(user_input)
    random_num = random.randint(1, 9)
    if user_guess == random_num:
        print("Winner")
        wins += 1
    else:
        print(f"Better luck next time. The number was {random_num}.")
        losses += 1

print(f"Total games won: {wins}")
print(f"Total games lost: {losses}")