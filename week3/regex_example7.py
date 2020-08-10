import re

print(re.search(r".com", "welcome"))

print(re.search(r"\.com", "welcome"))

print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))

print(re.search(r"\w*", "And_this_is_another"))

# \w - alpha, numeric, underscore
# \d - digit matching
# \s - white space chars
# \b - word boundries