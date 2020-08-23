import re

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return None
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))






