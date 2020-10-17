#!/usr/bin/env python3

import re

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (mdouglas)"

# print(re.search(r"ticky: INFO: ([\w ]*) ", line))
# Search for Info Tickets
y = re.search(r"ticky: INFO: ([\w ]*) ", line)
print(y.group(1))

# Username extraction for Info Tickets
x = re.search(r"\((\w*)\)", line)
print("Username: " + x.group(1))

# Add Info Count to Username Dictionary

line2 = "Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (noel)"

# print(re.search(r"ticky: ERROR: ([\w ]*) ", line2))

# Connection to DB failed error
y = re.search(r"ticky: ERROR: ([\w ]*) ", line2)
print("Error Message: " + y.group(1))

# Add Error Message Count to Error Dictionary

# Username extraction for Error Messages

x = re.search(r"\((\w*)\)", line2)
print(x.group(1))

# Add Error Count to User Dictionary


#string_one = 'file_record_transcript.pdf'
#string_two = 'file_07241999.pdf'
#string_three = 'testfile_fake.pdf.tmp'

#pattern = '^(file.+)\.pdf$'
#a = re.search(pattern, string_one)
#b = re.search(pattern, string_two)
#c = re.search(pattern, string_three)

#print(a.group() if a is not None else 'Not found')
#print(b.group() if b is not None else 'Not found')
#print(c.group() if c is not None else 'Not found')




