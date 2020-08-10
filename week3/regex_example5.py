import re

# match Py, any number of chars, followed by "n"

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))

# match "Py", any number of lower case alpha chars, followed by "n"
 
print(re.search(r"Py[a-z]*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Pyn"))

# match one or more "o" chars and one or more "l"

print(re.search(r"o+l+", "goldfish"))

print(re.search(r"o+l+", "woolly"))

print(re.search(r"o+l+", "boil"))

# match zero or more "p" char followed by "each" string

print(re.search(r"p?each", "To each their own"))

print(re.search(r"p?each", "I like peaches"))

