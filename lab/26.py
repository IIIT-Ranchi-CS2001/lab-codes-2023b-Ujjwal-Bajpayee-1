from math import factorial



def exp(x : float, pow : int, num : int, i : int) -> float :
    if num == 1:
        return 1
    if num == i:
        return 0
    else:
        return x**pow/factorial(pow) - exp(x,pow+2, num, i+1)

x = float(input("Enter x:"))
n = int(input("Enter n:"))

print(exp(x,0,n,1))