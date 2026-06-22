"""Count frequency of letters in a string"""
text = "banana"
freq = {}
for char in text:
    #.get() method safely gets the key and if Key is missing create it with initial value 0
    freq[char] = freq.get(char,0) + 1
for key, values in freq.items():
    print(key, values)