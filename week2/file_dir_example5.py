import os

working_dir = "/Users/norbertkirkpatrick/Documents/Python/Google-Python-OS/week2"
os.chdir(working_dir)

# dir examples
print(os.getcwd())

if not os.path.exists("test1"):
    os.mkdir("test1")
os.chdir("test1")

print(os.getcwd())
os.chdir(working_dir)
os.rmdir("test1")

print(os.listdir(working_dir))

for name in os.listdir(working_dir):
    fullname = os.path.join(working_dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(name))
    else:
        print("{} is a file".format(name))

for name in os.listdir(working_dir):
    fullname = os.path.join(working_dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))




