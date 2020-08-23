import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

# result groups

print(result.groups())
print(result[0])
print(result[1])
print(result[2])

print("{} {}".format(result[2], result[1]))

