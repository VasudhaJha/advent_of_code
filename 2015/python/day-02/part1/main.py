def calculate_wrapping_paper_area(input_file: str) -> int:
    total_wrapping_paper_area = 0
    with open(input_file, "r") as file:
        for line in file:
            l, w, h = map(int, line.split("x"))
            side_areas = [l * w, w * h, h * l]

            smallest_side_area = min(side_areas)
            wrapping_paper_area = 2 * sum(side_areas)

            total_wrapping_paper_area += smallest_side_area + wrapping_paper_area
    
    return total_wrapping_paper_area

if __name__ == "__main__":
    input_file_path = "input.txt"
    total_wrapping_paper_needed = calculate_wrapping_paper_area(input_file=input_file_path)
    print(f"total square feet of wrapping paper is: {total_wrapping_paper_needed} feet")