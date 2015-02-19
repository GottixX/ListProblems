word = input("Enter word: ")
n = input("Enter n: ")
n = int(n)

words = []

counter = 0
word_count = 0
while counter < n:
    user_word = input("Word " + str(counter + 1) + ": ")
    words = words + [user_word]

    counter += 1
for word1 in words:
    if word in words:
        word_count += 1

print(word + " is found " + str(word_count) + " times")
    
