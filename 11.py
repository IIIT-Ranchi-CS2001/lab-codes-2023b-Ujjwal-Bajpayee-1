#Write a python script to print the first n terms of the Fibonacci series using while loop
n=int(input("ENTER THE NUMBER OF TERMS : "))
a=0
b=1
count=0
while count<n:
    print(a)
    c=a+b
    a=b
    b=c
    count=count+1
    