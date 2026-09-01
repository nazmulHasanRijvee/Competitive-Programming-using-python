"""Use Two pointers pattern to determine whether it is a palindrome"""


# Examples:
# "madam" -> true
# "racecar" -> true
# Constraint don't reverse the string text[::-1]
# Compare first vs last then second first vs second last and so on
# racecar ->   racecar
# ^     ^       ^   ^
def is_palindrome(chk_str):

    str_len = len(chk_str)
    for i in range(str_len // 2):
        if chk_str[i] != chk_str[-1 - i]:
            return False  # if first and last doesn't match then break the loop and return false

    return True  # if all matches and makes it here return true


if __name__ == "__main__":
    print(is_palindrome("madam"))
