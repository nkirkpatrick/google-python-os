import re

result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazar")
print(result)

result = re.search(r"aza", "maze")
print(result)

# first char begins with the letter "x"
print(re.search(r"^x", "xenon"))

# first char begins with "p" followed by any char followed by "ng"
print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "clapping"))

print(re.search(r"p.ng", "sponge"))

# ignore case 
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

