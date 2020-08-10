import re

# first char "P" or "p" followed by "ython"
print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[Pp]ython", "python"))

# any lower case alpha char followed by "way"
print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"[a-z]way", "What a way to go"))

# search contains "cloud" followed by any lower/upper/numberic char
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# string begins with lower/upper char
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

# string begins with lower/upper char or space
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

#string contains cat or dog - first occurrence
print(re.search(r"cat|dog", "I like cats."))

print(re.search(r"cat|dog", "I like dogs."))

print(re.search(r"cat|dog", "I like both dogs and cats."))

#string contains cat or dog - all occurrences
print(re.findall(r"cat|dog", "I like both dogs and cats."))





