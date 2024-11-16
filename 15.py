#to find the no of palindrome words in a given sentence
s=input("ENTER THE SENTENCE : ")
count=0
words=s.split()
for i in words:
   if i==i[::-1]:
       count+=1
       
print("NO OF PALINDROME WORDS : ",count)

