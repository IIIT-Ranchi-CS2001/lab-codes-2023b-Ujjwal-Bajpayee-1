#Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.
n=int(input("ENTER THE NUMBER : "))
limit=int(input("ENTER THE LIMIT : "))
for i in range(1,limit+1):
    print(n,"*",i,"=",n*i)
