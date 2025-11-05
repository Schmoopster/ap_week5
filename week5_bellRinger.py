# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = "abracadabra"
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))
# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
hij_index = alphabet.index('hij')
print(hij_index)
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0])
print(alphabet[2])
print(alphabet[4])
print(alphabet[6])
print(alphabet[8])
print(alphabet[10])
print(alphabet[12])
# c. Reverse the entire string using slicing.
revered_alphabet = alphabet[::-1]
print(revered_alphabet)
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote 
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find('John F. Kennedy'))
personality_name = quote[78:]
print(personality_name)
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(info.rfind('subjective'))
subjective_word = info[36:]
print(subjective_word)
# b. Extract every third word.
every_third_letter = info.split()[::3]
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_word_position = info.split()[::-1]
reversed_word_position = ''.join(reversed_word_position)
print(reversed_word_position)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
phrase = "MAY THE FORCE BE WITH YOU."
print(phrase.upper())
print(phrase.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
mottos = ["Make", "haste", "slowly."]
seperator = ""
result_string = seperator

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".

# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word_to_find = "moonlight"
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/
phrase1 = "Supercalifragilisticexpialidocious"
print(len(phrase1))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
letter_to_count = "i"