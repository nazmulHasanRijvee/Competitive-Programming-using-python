"""Remove duplicates from a sorted array"""

# Use Read and Write two pointer pattern
# don't create another list, modify existing one and don't use Set
numbers = [1, 1, 2, 2, 3, 4, 4]
write = 1  # starts from 1 because 0 index is already unique and no previous element to compare to
for i in range(1, len(numbers)):
    if (
        numbers[i] != numbers[write - 1]
    ):  # compare against the last unique value which is the previous index of write
        numbers[write] = numbers[i]
        write += 1
while write < len(numbers):  # while loop use because after each pop loop length changes
    numbers.pop(write)
print(numbers)
