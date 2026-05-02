def find_vowel(str):
    string = str.replace(" ","").lower()
    
    vowels = ['a','e','i','o','u']
    count = 0
    vowels_in_string = []
    
    for char in string:
        if char in vowels:
            vowels_in_string.append(char)
            count += 1
    print(vowels_in_string)
    print(f'There is {count} vowels in this string')
            
find_vowel('manav')         