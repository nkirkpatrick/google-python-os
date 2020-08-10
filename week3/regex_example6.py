import re

# repeating letter "a" and all characters

def repeating_letter_a(text):
    result = re.search(r"[Aa].*[Aa].*", text)
    return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True