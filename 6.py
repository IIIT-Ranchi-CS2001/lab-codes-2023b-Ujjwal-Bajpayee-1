#to check a string is palindrome or not 
a=input("ENTER A WORD TO CHECK PALINDROME : ")
if a==a[::-1]:
    print("PALINDROME")
else:
    print("NOT PALINDROME")