# fruits = ["apple" ,"banana", "cherry"]

# print(fruits[0])

# fruits[1] ="grape"

# fruits.append("orange")

# fruits.remove("cherry")

# print(fruits)

# fruits.pop()

# print(fruits)

# point = (3,5,"t",2.55,5,7)
# # Bu satır aşağıdaki tuple yapısını açıklamak içindir.
# x,y,d,t,y,u = point

# print("x:" ,point[-1])

# print("y:" ,y)

# print("d:" ,d)

# print("t:" ,t)

students = [{
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "History"]
},{
    "name": "Jonah",
    "age": 33,
    "courses": ["History"]
},{
    "name": "Robert",
    "age": 24,
    "courses": ["Math"]
}
]

print(students[0]["name"])
students[0]["age"] = 23
students[0]["courses"].append("Science")
print(students)

print(students[0:1])

numbers=[1,2,4,5]
squad_numbers = [x**3 for x in numbers]
print(squad_numbers)
even_squad_numbers = [x**3 for x in numbers if x**3%2==0]
print(even_squad_numbers)
