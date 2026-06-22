"""Find the second-largest number in a given array"""
nums = [5, 7, 6]
largest = nums[0]
second_largest = nums[0]
for num in nums:
    if num > largest:
        second_largest = largest # if new largest found move the first largest in the second
        largest = num
    elif  num > second_largest: # else if check it's larger than the second one
        second_largest = num
print(largest)
print(second_largest)