def are_adjacent_characters(char_1: str, char_2: str):
    if char_1 == "a" and char_2 == "b":
        return True
    elif char_1 == "c" and char_2 == "d":
        return True
    elif char_1 == "p" and char_2 == "q":
        return True
    elif char_1 == "x" and char_2 == "y":
        return True
    else:
        return False

def calculate_nice_strings(input_file: str) -> int:
    num_nice_strings = 0
    with open(input_file, "r") as string_file:
        for string in string_file:
            num_vowels, char_appears_twice, is_followed_by_next_char = 0, False, False
            
            i = 0
            while i < len(string):
            
                if i < len(string) - 1:
                    if are_adjacent_characters(string[i], string[i+1]):
                        is_followed_by_next_char = True
                        break

                    if string[i+1] == string[i]:
                        char_appears_twice = True

                if string[i] in "aeiou":
                    num_vowels += 1

                i += 1
            
            if num_vowels >= 3 and char_appears_twice == True and is_followed_by_next_char == False:
                num_nice_strings += 1
    
    return num_nice_strings

if __name__ == "__main__":
    input_file_path = "input.txt"
    nice_strings = calculate_nice_strings(input_file=input_file_path)
    print(f"{nice_strings} are nice.")
            
