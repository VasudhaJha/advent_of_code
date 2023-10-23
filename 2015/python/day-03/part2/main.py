
def is_santa_turn(idx: int) -> bool:
    return idx % 2 == 0

def houses_with_presents(input_file: str) -> int:

    unique_positions = set()
    unique_positions.add((0, 0)) # for the first house (starting position)

    s_x, s_y = 0, 0
    r_x, r_y = 0, 0
    santa_turn = False
    with open(input_file, "r") as direction_file:
        directions = direction_file.read()

        for idx, direction in enumerate(directions):
            x, y = 0, 0

            if is_santa_turn(idx):
                # its santa's turn to deliver
                x, y = s_x, s_y
            else:
                # its robo santa's turn
                x, y = r_x, r_y
                santa_turn = False

            if direction == "^": # north
                x = x - 1
            elif direction == "v": # south
                x = x + 1
            elif direction == ">": # east
                y = y + 1
            else: # west
                y = y - 1
                
            unique_positions.add((x, y))
            
            if is_santa_turn(idx):
                s_x, s_y = x, y
            else:
                r_x, r_y = x, y
    
    return len(unique_positions)

if __name__ == "__main__":
    input_file_path = "input.txt"
    unique_houses = houses_with_presents(input_file=input_file_path)
    print(f"{unique_houses} houses got atleast 1 present")
