#For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
#The length of the string S
#The first occurrence of the letter ‘e’
#The total number of occurrences of ‘a’
#Generate “Ta Ta Black Sheep”


s="Ba Ba Black Sheep"
print(len(s))
print()
print(s.find('e'))
print(s.count('a'))
print(s.replace('Ba', 'Ta'))
