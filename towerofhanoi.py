import copy
import sys

TOTAL_DISC = 6
SOLVED_TOWER = list(range(TOTAL_DISC, 0, -1))


def get_player_move(towers):
    while True:
        print("type the letters for the tower from and to the tower for")
        print("for instance, type AB to move A disk from tower a to tower B")
        response = input(">").upper().strip()

        if response == "QUIT":
            print("thx for game!")
            sys.exit()

        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("type one of the combinations AB, AC, BA, BC, CA, CB")
            continue

        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            print("there is no disk")
        elif len(towers[to_tower]) == 0:
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("larger disks cannot be placed on smaller ones")
            continue
        else:
            return from_tower, to_tower


def display_towers(towers):
    for level in range(TOTAL_DISC, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)
            else:
                display_disk(tower[level])
        print()
    empty_space = " " * TOTAL_DISC
    print(f"{empty_space} A{empty_space}{empty_space} B{empty_space}{empty_space}C\n.")


def display_disk(width):
    empty_space = " " * (TOTAL_DISC - width)

    if width == 0:
        print(f"{empty_space}||{empty_space}", end="")
    else:
        disk = "@" * width
        num_label = str(width).rjust(2, "_")
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")


def main():
    print("""Tower hanoi
    
    Move a tower of disks, one disk at a time, to another tower.
     Larger disks cannot be placed on top of smaller ones.""")

    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:
        display_towers(towers)

        from_tower, to_tower = get_player_move(towers)

        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        if SOLVED_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)
            print("You win! Good job!")
            sys.exit()


if __name__ == "__main__":
    main()
