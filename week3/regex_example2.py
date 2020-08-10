import re

# check if string contains "a" followed by any char "e" follow by any char "i" followed by any char
def check_aei (text):
    result = re.search(r"a.e.i", text)
    return result != None


print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True