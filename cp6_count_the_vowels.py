"""Count the number of vowels in a string"""
text = "programming"
my_str = 'aioeu'
count = 0
for ch in text:
    if ch in my_str:
        count += 1
print(count)