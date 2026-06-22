text = "banana"
freq = {}
for char in text:
    if char not in freq:
        freq[char] = 0
    freq[char] = freq.get(char,0) + 1
for key, values in freq.items():
    print(key, values)