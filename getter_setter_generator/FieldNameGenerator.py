if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        field_values = [line.strip() for line in file.readlines()]

        for field in field_values:
            print("String get" + f"{field[0].capitalize()}{field[1:]}();")
