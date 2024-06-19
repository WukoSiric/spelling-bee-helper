
words = [] 

file = open('wordlist.txt', 'r')

for line in file: 
  words.append(line.strip().upper())


center_letter = input("Enter the center letter: ").upper()
other_letters = ["", "", "", "", "", ""]
for i in range(6):
  other_letters[i] = input("Enter other letter (" + str(i + 1) + "/6): ").upper()

print(center_letter)
print(other_letters)

required_letters = set(other_letters)
required_letters.add(center_letter)
potential_words = [] 
for word in words: 
  if len(word) <= 3: 
    continue

  if center_letter not in word: 
    continue 

  word_letters = set(word)
  if required_letters.issuperset(word_letters):
    potential_words.append(word)


print(potential_words)