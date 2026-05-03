def anagram(str1,str2):
    #remove spaces and convert string into lowercase
    string = str1.replace(" ","").lower()
    #make a list to store all alphabets in string
    str1_alphabets = []
    for i in string:
        str1_alphabets.append(i)
        #sort the list
        sorted_alphabets1 = str1_alphabets.sort()
    string2 = str2.replace(" ","").lower()
    #make second list to store alphabets of second string
    str2_alphabets = []
    for j in string2:
                str2_alphabets.append(j)
                #sort second list
                sorted_alphabets2 = str2_alphabets.sort()
    #compare both sorted lists
    if sorted_alphabets1 == sorted_alphabets2:
                print("given strings are anagrams")
    else:
                print("Given strings are not anagrams")           
anagram("listen","silent")                