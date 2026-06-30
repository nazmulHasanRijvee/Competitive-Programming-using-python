"""Moving all the zeroes in an array to the last using two pointer"""
# Constraints:
# Don't create another list or use.pop() method
# Think in terms of two pointer
# Read and write pointer pattern
numbers = [0, 1, 0, 3, 12]
write = 0
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[write] = numbers[i]
        write += 1
for i in range(write,len(numbers)):
    numbers[i] = 0
print(numbers)