"""
Input:
- A 1000 X 1000 grid so coordinate pairs are specified within this range
- Instructions: turn on, turn off and toggle

Output: The number of lights that are lit after following all the instructions

Constraints: The lights all start turned off.
"""

from typing import List, Tuple

# let's set the state as false for off and true for on

grid = [[False] * 1000 for _ in range(1000)]

def extract_from(instruction_string: str) -> Tuple[str, List[int], List[int]]:
    components = instruction_string.split()
    instruction = ""

    # 1. extract instruction
    i = 0
    if components[i] == "toggle":
        instruction = "toggle"
        i += 1
    else:
        instruction = components[i+1]
        i += 2

    # 2. extract start coords
    start_coords = [int(coord) for coord in components[i].split(',')]

    i += 2

    # 3. extract end coords
    end_coords = [int(coord) for coord in components[i].split(',')]
    return (instruction, start_coords, end_coords)

def calculate_lit_lights(input_file: str) -> int:
    num_lit_lights = 0

    with open(input_file, "r") as file:
        for line in file:
            instruction, start_coords, end_coords = extract_from(line)

            # toggle, turn on or turn off lights
            for row in range(start_coords[0], end_coords[0]+1):
                for col in range(start_coords[1], end_coords[1]+1):
                    if instruction == "toggle":
                        grid[row][col] = not grid[row][col]
                    elif instruction == "on":
                        grid[row][col] = True
                    else:
                        grid[row][col] = False

    # go over everything to calculate what's lit
    for row in grid:
        for cell in row:
            if cell:
                num_lit_lights += 1

    return num_lit_lights


if __name__ == "__main__":
    input_file_path = "input.txt"
    num_lights = calculate_lit_lights(input_file=input_file_path)
    print(f"{num_lights} are lit.")


                    