import re
def convert_phone_number(phone):
  result = re.sub(r"\b([0-9]{3})-([0-9]{3}-[0-9]{4})\b", r"(\1) \2" , phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


# sub examples

#print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an e-mail for go_nuts95@my.example.com"))

#print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))