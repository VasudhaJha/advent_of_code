import hashlib

def lowest_number(secret_key: str):
    current_number = 1

    while True:
        input_string = secret_key + str(current_number)
        hash = hashlib.md5(input_string.encode()).hexdigest()
        if hash[:6] == "000000":
            print(f"Lowest number: {current_number}")
            break

        current_number += 1

if __name__ == "__main__":
    with open("input.txt", "r") as input:
        secret_key = input.read()
        lowest_number(secret_key)