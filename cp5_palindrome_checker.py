"""Find if the String is palindrome"""
text = "racecar"
result = ''
for ch in text:
    result = ch + result
print(result == text) # if else shorthand