# Without using max(), sorted() method
nums = [5, 2, 8, 1, 4]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)