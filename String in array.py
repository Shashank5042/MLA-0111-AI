from itertools import permutations

def is_mapping_possible(arr, S):
    unique_chars = set(''.join(arr) + S)
    if len(unique_chars) > 10:
        return False

    for perm in permutations(range(10), len(unique_chars)):
        char_map = {char: num for char, num in zip(unique_chars, perm)}
        if sum_strings(arr, char_map) == string_to_int(S, char_map):
            return True
    return False

def sum_strings(arr, char_map):
    total = 0
    for string in arr:
        total += string_to_int(string, char_map)
    return total

def string_to_int(string, char_map):
    num = 0
    for char in string:
        num = num * 10 + char_map[char]
    return num

# Test the function with the given input
arr = ["SEND", "MORE"]
S = "MONEY"
print("Output:", "Yes" if is_mapping_possible(arr, S) else "No")
