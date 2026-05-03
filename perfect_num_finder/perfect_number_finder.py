def perfect_num(n):
    #make empty list to store divisors 
    divisors = []
    #run loop to find all divisors
    for i in range(1, n):
        if n%i == 0:
            #appending all divisors in list
            divisors.append(int(i))        
    total = sum(divisors)
    #comparing n and total to find that n is perfect number or not..
    if n == total:
        print("Given number is Perfect number") 
    else:
        print("Given number is not perfect number") 
perfect_num(6)            
perfect_num(28)
perfect_num(12)            