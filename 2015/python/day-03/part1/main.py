def houses_with_presents(input_file: str) -> int:

    unique_positions = set()
    unique_positions.add((0, 0)) # for the first house (starting position)

    x, y = 0, 0

    with open(input_file, "r") as direction_file:
        directions = direction_file.read()

        for direction in directions:
            if direction == "^": # north
                x = x - 1
            elif direction == "v": # south
                x = x + 1
            elif direction == ">": # east
                y = y + 1
            else: # west
                y = y - 1
                
            unique_positions.add((x, y))
    
    return len(unique_positions)

if __name__ == "__main__":
    input_file_path = "input.txt"
    unique_houses = houses_with_presents(input_file=input_file_path)
    print(f"{unique_houses} houses got atleast 1 present")
