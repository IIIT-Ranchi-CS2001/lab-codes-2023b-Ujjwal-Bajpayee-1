def count_letters(input_string):
    letter_count = {}
    for letter in input_string:
        if letter.isalpha():  
            letter = letter.lower()  
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

input_string = input("Enter a string: ")
result = count_letters(input_string)

for letter, count in result.items():
    print(f"{letter}: {count}")