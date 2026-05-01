def palindrome(str):
    string = str.replace(" ","").lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        print("this string is palindrome")
    else:
        print("this string is not palindrome")   
    
palindrome("radar")   