#Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.
s=input("ENTER THE STRING : ")
for i in s:
    if i.isalnum()==False:
        print("False")
        break
else:
    print("True")