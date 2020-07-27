with open("/Users/norbertkirkpatrick/Documents/Python/Google-Python-OS/week2/spider.txt") as file:
    for line in file:
        print(line.upper())

with open("/Users/norbertkirkpatrick/Documents/Python/Google-Python-OS/week2/spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("/Users/norbertkirkpatrick/Documents/Python/Google-Python-OS/week2/spider.txt")
lines = file.readlines()
file.close()

lines.sort()
print(lines)

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")





