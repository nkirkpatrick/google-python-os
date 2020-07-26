def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    filesize = file.write(comments)
  return(filesize)

print(create_python_script("program.py"))


#with open("./week2/novel.txt", "w") as file:
#    file.write("It was a dark and stormy night")