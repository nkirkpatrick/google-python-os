import re
def transform_comments(line_of_code):
  result = re.sub(r"[#]{1,}", r"//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

# split examples

# print(re.split(r"[.?!]{1,}", "One sentence.. Another One? And the last one!"))

# print(re.split(r"([.?!])", "One sentence. Another One? And the last one!"))

# sub examples

# print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an e-mail for go_nuts95@my.example.com"))

# print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
