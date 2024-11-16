import math

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

d = b**2 - 4*a*c

if d == 0:
    root = -b / (2*a)
    print("The equation has one real repeated root: R1 = R2 =", root)
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The equation has two distinct real roots: R1 =", root1, "and R2 =", root2)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print("The equation has two complex roots: R1 =", real_part, "+", imaginary_part, "i and R2 =", real_part, "-", imaginary_part, "i")