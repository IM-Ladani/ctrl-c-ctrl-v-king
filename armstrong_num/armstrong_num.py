def armstrong(n):
    #convert number into string
    string = str(n)
    #make empty list to store each number as string
    digit = []
    for num in string:
        digit.append(num)
    int_digit = []
    #converting list elements, string to integer 
    for x in digit:
        int_digit.append(int(x))  
        
    lenth = int(len(string))
    #make list to store cube of numbers
    cube_digit = [] 
    for i in int_digit:
          cube_digit.append(i**lenth)
          #make total of all number in list
          total = sum(cube_digit)
    if n == total:
          print("given number is armstrong number.")
    else:
          print("given number is not armstrong number.")         
armstrong(123)          