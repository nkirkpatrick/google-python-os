import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  f = open(filename)
  # Read the rows of the file
  rows = csv.reader(f)
  next(rows)
    # Process each row
  for row in rows:
    name, color, ftype = row
    # Format the return string for data rows only
    return_string += "a {} {} is {}\n".format(color, name, ftype)
  
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

# read and print csv example
#f = open("csv_file.txt")
#csv_f = csv.reader(f)

#for row in csv_f:
#    name, phone, role = row
#    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

#f.close()

#import csv
#with open('software.csv') as software:
#    reader = csv.DictReader(software)
#    for row in reader:
#        print(("{} has {} users").format(row["name"], row["users"]))