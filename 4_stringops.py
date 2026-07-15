sentence = "I like to eat KFC"

# orginal strings are immutable - unchange
# upper() -> converts a string into capital letters and returns a new string

upperStr = sentence.upper() # captial

print(upperStr)

# lower -> converts a string into small letters and returns a new string
lowerStr = sentence.lower()
print(lowerStr)

# len(strring) - counts characters in the string => returns the count
print(len(sentence))

# strings are indexed - every character of a string is represented by a positional number
# index numbers starts from 0 not 1
# access a character using variable[index]
print(sentence[0]) # I
print(sentence[2])
print(sentence[15])
print(sentence[16])

# formulate to get the last char
print(sentence[len(sentence) - 1]) # print(sentence[17 - 1]) => print(sentence[16])

# replace(existing, new)
newSent = sentence.replace("KFC", "McDonalds")

print(sentence)
print(newSent)