def pi_organizer(pi):
    if pi > 3 :
        print("buyuktur uc")
        return True
    elif pi <= 3:
        print("buyuk degıldır uc")
        return False
    
    print("tanımsız")
    return False

def is_capital(city_name,capitals):
    if city_name in capitals:
        print(city_name + " yes it is")
        return True
    elif city_name.capitalize() in capitals:
        print(city_name.capitalize() + " yes but not actualy")
        return True
    else:
        return False

def my_filter(input,cptls):
    if isinstance(input,str):
        out = is_capital(input,capitals=cptls)
    else:
        out = pi_organizer(input)
    return out

capitals = ["Seul","Berlin","Tokyo"]
input = [3,6,12,"berlin",4.324,"tokyo",1.4243,"istanbul",0.3425,"seul",1000222]

for inp in input:
    
    output = my_filter(input=inp,cptls=capitals)

    print(output)