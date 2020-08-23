import re
def multi_vowel_words(text):
  pattern = r"\w*[aeiou]{3,}\w*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []


# match first word with 5 characters
#print(re.search(r"[a-zA-Z]{5}", "a ghosty"))
#print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# match all words with 5 characters
#print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# match all words with exactly 5 charcters - \b - word boundries
#print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))

# match words with 5 to 10 characters
#print(re.findall(r"\w{5,10}", "I really like strawberries"))

# match words with 5 or more characters 
#print(re.findall(r"\w{5,}", "I really like strawberries"))

#print(re.findall(r"s\w{,20}", "I really like strawberries"))


