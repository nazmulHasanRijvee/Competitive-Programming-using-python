"""Find the first non-repeating character in a string"""
text = "loveleetcode"
freq = {}
for char in text:
    freq[char] = freq.get(char,0) + 1 # .get() safely gets the value
for i in text:
    if freq[i] == 1:
        print(i)
        break