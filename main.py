name = "Yunus Emre"
surname = "Yıldız"

surnames = ["Yıldız", "Aksoy", "Demir"]
surnames1 = ["Yıldız", "Aksoy", "Demir"]
[(x, y) for x in surnames for y in surnames1]

if surname in surnames:
    print(True)
elif surnames not in surnames:
    print(False)
else:
    print(False)

for soyad in surnames:
    #print(soyad)
    if surname == soyad:
        print(True)
        print(soyad)
    else:
        print(False)
        print(soyad)
        
a = 0
while a < 4:
    print("Elma")
    print(a)
    if a == 2:
        continue
    a+=1
    

print(name[0])

print(surnames[0])

print("")