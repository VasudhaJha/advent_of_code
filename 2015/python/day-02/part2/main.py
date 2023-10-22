from typing import List

def calculate_total_feet_ribbon_required(input_file: str) -> int:
    total_ribbon_required: int = 0

    with open(input_file, "r") as file:
        for line in file:
            l, w, h = map(int, line.split("x"))
            ribbon_for_bow = l * w * h
            min_two_sides = calculate_min_two_sides([l, w, h])
            ribbon_to_wrap = 2 * sum(min_two_sides)

            total_ribbon_required += ribbon_for_bow + ribbon_to_wrap

    return total_ribbon_required

def calculate_min_two_sides(sides: List[int]) -> List[int]:
    # Iterate through the list
    min1 = float('inf')
    min2 = float('inf')
    for side in sides:
        if side <= min1:
            min2 = min1
            min1 = side
        elif side <= min2:
            min2 = side
    
    return [min1, min2]

if __name__ == "__main__":
    input_file_path = "input.txt"
    total_ribbon_needed = calculate_total_feet_ribbon_required(input_file=input_file_path)
    print(f"total ribbon needed is: {total_ribbon_needed} feet")