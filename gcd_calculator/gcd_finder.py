def gcd_finder(int1, int2):
    nums = [int1, int2]
    largest = max(nums)
    common_divisor = []
    for i in range(1,largest+1):
        if int1 % i == 0 and int2 % i == 0:
            common_divisor.append(i) 
    gcd = max(common_divisor)
    print(f"the gcd of {int1} & {int2} is: {gcd}")
gcd_finder(18,48)  