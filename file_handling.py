import csv
import json
new_student = {
                "name": "Jonah",
                "age": 33,
                "courses": ["History"]
            }

with open("myfiles/students.json","r") as json_file :

    data = json.load(json_file)

data.append(new_student)
print(data[-1])

with open("myfiles/students.json","w") as json_file :
    json.dump(data,json_file)

with open("myfiles/second.csv","x+") as csv_file :
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["Name","Age"])
    csv_writer.writerow(["Ayşe","22"])
    csv_writer.writerow(["Mehmet","23"])



with open("myfiles/second.csv","r") as csv_file :
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        
        print(row)


# file = open("myfiles/first.txt" , "a+")

# print(file.read())

# file.write("\nThis is my seventh message!")

# file.close()