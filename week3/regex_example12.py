import re

# repetition qualifiers 

# match first word with 5 characters
print(re.search(r"[a-zA-Z]{5}", "a ghosty"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# match all words with 5 characters
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# match all words with exactly 5 charcters - \b - word boundries
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))

# match words with 5 to 10 characters
print(re.findall(r"\w{5,10}", "I really like strawberries"))

# match words with 5 or more characters 
print(re.findall(r"\w{5,}", "I really like strawberries"))

print(re.findall(r"s\w{,20}", "I really like strawberries"))




