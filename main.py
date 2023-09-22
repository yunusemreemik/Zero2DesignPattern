import animals.dogs as dg
import animals.cats as ct

my_dog = dg.Dog("Karabas", 2, "Brown", "Golden Retriever")

print(f"{my_dog.name} is {my_dog.age} years old.")

a_dog = my_dog.speak()
b_bog = my_dog.hunger()

my_cat = ct.Cat("Yumak",1,"White","Siamese")

print(f"{my_cat.name} is {my_cat.age} years old.")

my_cat.speak()

pass