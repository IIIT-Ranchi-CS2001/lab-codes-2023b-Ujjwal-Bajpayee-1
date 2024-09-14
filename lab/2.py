#find perimeter and area of a rectangle(use heron's formula)
#find all three angles of triangle given
import math

a=input("Enter the first side :")
b=input("Enter the second side :")
c=input("Enter the third side :")

print("YOUR THREE SIDES ARE",a,b,c)
semi_perimeter=(int(a)+int(b)+int(c))/2
print(f"Perimeter of the triangle is {semi_perimeter}")
a=math.sqrt(semi_perimeter*(semi_perimeter-int(a))*(semi_perimeter-int(b))*(semi_perimeter-int(c)))
print(f"Area of the triangle is {a}")

angle1=math.acos((int(b)**2+int(c)**2-int(a)**2)/(2*int(b)*int(c)))
angle2=math.acos((int(a)**2+int(c)**2-int(b)**2)/(2*int(a)*int(c)))
angle3=math.acos((int(a)**2+int(b)**2-int(c)**2)/(2*int(a)*int(b)))
print(f"First angle of the triangle is {math.degrees(angle1)}")
print(f"Second angle of the triangle is {math.degrees(angle2)}")
print(f"Third angle of the triangle is {math.degrees(angle3)}")


