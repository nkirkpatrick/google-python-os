import re

# extract PID from a string

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid("mycomputer bad_process[12345]: Package update error"))

print(extract_pid("99 elephants in a [cage]"))

