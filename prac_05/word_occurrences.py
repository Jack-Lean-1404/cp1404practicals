# Guess = 15mins and 30sec
# Actual = 13mins and 6sec

word_to_occurrence = {}

string = input("Enter a string: ")

for word in string.split():
    frequency = word_to_occurrence.get(word, 0)
    word_to_occurrence[word] = frequency + 1

words = list(word_to_occurrence.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_occurrence[word]}")



