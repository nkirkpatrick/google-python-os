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

    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} is a {row["color"]} {row["type"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

contents_of_file("flowers.csv")