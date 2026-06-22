nums = [5, 2, 8, 1, 4]
largest = 0
second_largest = 0
for num in nums:
    if num > largest:
        largest = num
nums.remove(largest)
for num in nums:
    if num > second_largest:
        second_largest = num
print(largest)
print(second_largest)