"""Find the sum of all items in the array"""
# Without using sum() method
nums = [5, 2, 8, 1, 4]
total = 0 # space complexity 0(1)
for num in nums: # time complexity O(n)
    total += num
print(total)

"""OOP Solve"""
# class Solve:
#     def __init__(self, list_nums):
#         self.list = list_nums
#     def solve(self):
#         total2 = 0
#         for number in self.list:
#             total2 += number
#         print(total2)
# solved = Solve(nums)
# solved.solve()