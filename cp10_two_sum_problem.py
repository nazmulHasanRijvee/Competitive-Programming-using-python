"""Two sum problem, find two numbers in an array whose sum equals the target"""
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i in range(len(nums)):
    needed = target - nums[i]
    if needed in seen: # checking if the needed values is found in the dictionary or not
        output = [seen[needed], i]
        print(output)
    else:
        seen[nums[i]] = i # if not found then store current value and its index for future look up