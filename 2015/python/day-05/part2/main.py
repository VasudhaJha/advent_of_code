import re

non_overlapping_pairs_pattern = re.compile(r'(..).*\1')
repeating_letter_with_one_in_the_middle_pattern = re.compile(r'(.).\1')

def contains_non_overlapping_pairs(string: str) -> bool:
    result = non_overlapping_pairs_pattern.search(string)
    return bool(result)

def contains_repeating_letter(string: str) -> bool:
    result = repeating_letter_with_one_in_the_middle_pattern.search(string)
    return bool(result)

def calculate_nice_strings(input_file: str) -> int:
    num_nice_strings = 0
    with open(input_file, "r") as input_file:
        for string in input_file:
            if contains_non_overlapping_pairs(string) and contains_repeating_letter(string):
                num_nice_strings += 1

    return num_nice_strings

if __name__ == "__main__":
    input_file_path = "input.txt"
    nice_strings = calculate_nice_strings(input_file=input_file_path)
    print(f"{nice_strings} are nice.")
            
