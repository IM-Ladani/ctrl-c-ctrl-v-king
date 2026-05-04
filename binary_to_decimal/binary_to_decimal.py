def is_valid_binary(binary_str):
    for digit in binary_str:
        if digit != "0" and digit != "1":
            return False
    return True
digits=[]
def binary_to_decimal(binary_str):
    for digit in binary_str:
        digits.append(int(digit))
    lenth = len(digits)
    reverse_digits = digits[::-1]
    values = []
    for i in range(lenth):
        value = (2**i)*reverse_digits[i]
        values.append(value)
    decimal = sum(values)
    print(f"The value of {binary_str} is: {decimal}")
     
binary_num = str(input("Enter any binary number: "))
if is_valid_binary(binary_num):
    binary_to_decimal(binary_num)
else:
    print("invalid binary number")                  