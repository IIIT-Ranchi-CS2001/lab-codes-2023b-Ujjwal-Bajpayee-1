#write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop

n=int(input("ENTER THE NUMBER U WANT TO FIND SQUARE TILL THAT NUMBER : "))
while n>0:
    print(n,n*n)
    n=n-1