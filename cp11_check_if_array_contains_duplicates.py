"""Check if array contains duplicates"""

# Return True if any value appears at least twice in the give array
# otherwise false
# Constraints, don't use nums.count or collections.counter
nums = [1, 2, 3, 1]


def check_duplicates(numbers):

    seen = set()  # Using set because we only need to remember the seen number. Dictionary can be used too

    for num in numbers:
        if num in seen:
            return True

        else:
            seen.add(num)
    return False


if __name__ == "__main__":
    print(check_duplicates(nums))
