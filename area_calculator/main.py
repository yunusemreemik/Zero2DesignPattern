import shapes.Rectangle as rc
import shapes.Circle as cr

rectangle = rc.Rectangle("Dikdörtgen",5,10)

rectangle_area = rectangle.calculate_area()

print(f"{rectangle.name} alanı : {rectangle_area}")

circle = cr.Circle("Daire",7)

circle_area = circle.calculate_area()

print(f"{circle.name} alanı : {circle_area}")