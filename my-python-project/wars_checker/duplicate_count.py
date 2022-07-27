def duplicate_count(text):
    string_list_uniques = set(list(text.lower()))
    string_list = list(text.lower())
    dist_counter = 0
    result_counter = 0
    for x in string_list_uniques:
        dist_counter = 0
        for y in string_list:
            if y == x:
                dist_counter = dist_counter + 1
                if dist_counter > 1:
                    result_counter = result_counter + 1
                    break
    return result_counter


print(duplicate_count("abcdee"))
print(duplicate_count("abcdeehhhhhh aaaaaa zxczxczxc 2222224444"))

# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets (both
# uppercase and lowercase) and numeric digits.
