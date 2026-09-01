"""Determine if Parentheses are Valid Using Stack"""


# Example: s = '(){}[]' -> true
# s = '{[]}' -> true and s = '(]' -> false
def is_valid_parentheses(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            recent = stack.pop()

            # using .get() to handle the edge case if abc is
            # given instead of () {} [] parentheses the dictionary
            # will throw error, Key not found
            if pairs.get(ch, "0") != recent:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid_parentheses("()[]"))
