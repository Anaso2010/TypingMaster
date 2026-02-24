import random

WORDS = [
    "apple", "banana", "orange", "grape", "cherry",
    "peach", "melon", "kiwi", "mango", "pear",
    "plum", "lemon", "lime", "apricot", "papaya"
]

TOTAL_WORDS = 15
words_to_type = random.sample(WORDS, TOTAL_WORDS)

print(words_to_type)

mistakes = 0
for word in words_to_type:
    user_input = input(f"Type: {word}")

    if user_input == word:
        print("Correct")
    else:
        print("Incorrect")
        mistakes += 1

for i, word in enumerate(words_to_type, start=1):
    print(f"\nWord {i}/{TOTAL_WORDS}: {word}")
    user_input = input("Type: ")

for i, word in enumerate(words_to_type, start=1):
    print(f"\nWord {i}/{TOTAL_WORDS}: {word}")
    user_input = input("Type: ")