def lcm_finder(int1, int2):
    multiples_of_int1 = []
    for i in range(1, int2+1):
        multiple1 = int1*i
        multiples_of_int1.append(multiple1)
    multiples_of_int2 = []   
    for j in range(1,int1+1):
           multiple2 = int2*j
           multiples_of_int2.append(multiple2)
    common = list(set(multiples_of_int1) & set(multiples_of_int2))      
    lcm = min(common)
    print(f"The lcm of {int1} & {int2} is: {lcm}")
lcm_finder(12,18)          