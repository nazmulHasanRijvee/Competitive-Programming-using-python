# Don't use text[::-1], reversed() method
text = 'python'
result = ''
for i in range(1, len(text) + 1):
    result += text[-i]
print(result)

"""OR This"""
# result = ""
#
# for ch in text:
#     result = ch + result