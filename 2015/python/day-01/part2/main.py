def find_first_position_to_basement(instruction_file: str) -> int:
    floor_number = 0 # since we start from the ground floor
    with open(instruction_file, "r") as instruction_file:
        instructions = instruction_file.read()

        for position, instruction in enumerate(instructions):
            if instruction == "(":
                floor_number += 1
            elif instruction == ")":
                floor_number -= 1
            
            if floor_number == -1:
                return position + 1
    
    return 0

if __name__ == "__main__":
    input_file_path = "input.txt"
    first_basement_position = find_first_position_to_basement(instruction_file=input_file_path)
    print(f"The position of the first character leading to basement is: {first_basement_position}")