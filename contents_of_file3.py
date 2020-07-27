import os
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
  with open(filename) as csv_file:
    #Read the rows of the file into a dictionary
    csv_reader = csv.DictReader(csv_file):
    # Process each item of the dictionary
    for row in csv_reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


#import csv

#with open('employee_birthday.txt', mode='r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
##    print(f'Processed {line_count} lines.')

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


