"""Two sum problem, find two numbers in an array whose sum equals the target"""

nums = [3, 2, 4]
target = 6
seen = {}
for i in range(len(nums)):
    needed = target - nums[i]
    if needed in seen:  # checking if the needed value is found in the dictionary or not
        output = [seen[needed], i]
        print(output)
        break  # break if the answer is found
    else:
        seen[nums[i]] = i  # if not found then store current value and its index for future look up
