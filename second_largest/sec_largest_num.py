largest = float('-inf')
second_largest = float('-inf')

nums = [1,4,6,3,8,9,2]

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num> second_largest and num != largest:
        second_largest = num
print(second_largest)        