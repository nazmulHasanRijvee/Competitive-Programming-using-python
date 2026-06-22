"""Find how many even numbers are in the given list"""
nums = [5, 2, 8, 1, 4, 7, 10]
count = 0
for num in nums:
    if num % 2 == 0:
        count += 1
print(count)