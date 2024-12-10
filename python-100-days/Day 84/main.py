import numpy as np

game_field = np.array([[1, 0, 2],
                       [2, 1, 0],
                       [0, 0, 1]])


def three_in_row(row: np.ndarray):
    first_elem = row[0]
    if first_elem == 0:
        return False

    for elem in row:
        if first_elem != elem:
            return False

    return True


def get_winnable_row(array: np.ndarray):
    result = False
    for i in range(3):
        result = three_in_row(array[i]) or three_in_row(array[:, i])
        if result:
            break

    return result or three_in_row(array.diagonal()) or three_in_row(np.rot90(array).diagonal())


def draw_game_area(array: np.ndarray):
    for x, array_row in enumerate(array):
        row = []
        for value in array_row:
            if value == 1:
                row.append(" O")
            elif value == 2:
                row.append(" X")
            else:
                row.append("  ")

        print(" |".join(row))
        if x != 2:
            print("-"*11)


draw_game_area(game_field)
print(get_winnable_row(game_field))
