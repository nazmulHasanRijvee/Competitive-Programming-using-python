"""Find if Valid Anagram or not"""


# Two strings are called anagrams if they contain the same characters
# with the same frequencies, but possibly in a different order
# Example: s = "listen"
#          t = "silent"
# anagrams. Output should be true.
# Constraints don't used sorted() method or Counter() method
def valid_anagram(s, t):

    if len(s) != len(t):
        return False

    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in t:
        freq[char] = freq.get(char, 0) - 1
        if freq.get(char, 0) < 0:
            return False

    return True


if __name__ == "__main__":
    print(valid_anagram("listen", "silent"))
