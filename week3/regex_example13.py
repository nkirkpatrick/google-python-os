import re

# split examples

print(re.split(r"[.?!]{1,}", "One sentence.. Another One? And the last one!"))

print(re.split(r"([.?!])", "One sentence. Another One? And the last one!"))

# sub examples

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an e-mail for go_nuts95@my.example.com"))

print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

