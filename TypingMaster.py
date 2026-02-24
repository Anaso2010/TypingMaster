import random

WORDS = [
    "apple", "banana", "orange", "grape", "cherry",
    "peach", "melon", "kiwi", "mango", "pear",
    "plum", "lemon", "lime", "apricot", "papaya"
]

TOTAL_WORDS = 15
words_to_type = random.sample(WORDS, TOTAL_WORDS)

mistakes = 0

for i, word in enumerate(words_to_type, start=1):
    print(f"\nWord {i}/{TOTAL_WORDS}: {word}")
    user_input = input("Type: ")

    if user_input == word:
        print("Correct")
    else:
        print("Incorrect")
        mistakes += 1

correct = TOTAL_WORDS - mistakes
accuracy = (correct / TOTAL_WORDS) * 100

print("\nGame Over!")
print(f"Mistakes: {mistakes}")
print(f"Accuracy: {accuracy:.2f}%")


