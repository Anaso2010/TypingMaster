import random

WORDS = [
    "apple", "banana", "orange", "grape", "cherry",
    "peach", "melon", "kiwi", "mango", "pear",
    "plum", "lemon", "lime", "apricot", "papaya"
]

TOTAL_WORDS = 15
words_to_type = random.sample(WORDS, TOTAL_WORDS)

print(words_to_type)