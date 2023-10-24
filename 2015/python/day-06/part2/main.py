"""
Input:
- A 1000 X 1000 grid so coordinate pairs are specified within this range
- Instructions: turn on, turn off and toggle

Output: total brightness of all lights combined after following Santa's instructions

Constraints: 
- The lights all start at 0.
- Turn on: increase the brightness of those lights by 1.
- Turn off: decrease the brightness of those lights by 1, to a minimum of zero.
- Toggle: increase the brightness of those lights by 2.
"""

import re
from typing import List, Tuple

# let's set the state as false for off and true for on

grid = [[0] * 1000 for _ in range(1000)]
pattern = re.compile(r'(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)')

def extract_using_regex(instruction_string: str) -> Tuple[str, List[int], List[int]]:
    match = pattern.match(instruction_string)
    return (match.group(1), [int(match.group(2)), int(match.group(3))], [int(match.group(4)), int(match.group(5))])

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

def calculate_total_brightness(input_file: str) -> int:
    total_brightness = 0

    with open(input_file, "r") as file:
        for line in file:
            # instruction, start_coords, end_coords = extract_from(line)
            instruction, start_coords, end_coords = extract_using_regex(line)
            
            # toggle, turn on or turn off lights
            for row in range(start_coords[0], end_coords[0]+1):
                for col in range(start_coords[1], end_coords[1]+1):
                    if "toggle" in instruction:
                        grid[row][col] += 2
                    elif "on" in instruction:
                        grid[row][col] += 1
                    else:
                        if grid[row][col] > 0:
                            grid[row][col] -= 1

    # go over everything to calculate what's lit
    total_brightness = sum(sum(row) for row in grid)

    return total_brightness


if __name__ == "__main__":
    input_file_path = "input.txt"
    total_brightness = calculate_total_brightness(input_file=input_file_path)
    print(f"Total brightness is {total_brightness}.")


                    