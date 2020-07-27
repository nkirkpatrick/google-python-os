file = open("/Users/norbertkirkpatrick/Documents/Python/Google-Python-OS/week2/spider.txt")
print(file.readline())

print(file.readline())

print(file.read())

file.close()

with open("/Users/norbertkirkpatrick/Documents/Python/Google-Python-OS/week2/spider.txt") as file:
    print(file.readline())

