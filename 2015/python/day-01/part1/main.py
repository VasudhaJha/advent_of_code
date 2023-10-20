def find_floor(instruction_file: str) -> int:
    floor_number = 0 # since he starts on the ground floor

    with open(instruction_file, "r") as instruction_file:
        instructions = instruction_file.read()
        for instruction in instructions:
            if instruction == "(":
                floor_number += 1
            else:
                floor_number -= 1
        
    return floor_number

if __name__ == "__main__":
    input_file_path = "input.txt"
    floor = find_floor(instruction_file=input_file_path)
    print(f"To which floor do the instructions take Santa? {floor}")
