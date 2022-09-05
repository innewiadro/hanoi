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

        if response not in ("AB","AC","BA","BC","CA","CB"):
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
    pass


def display_disk(width):
    pass


def main():
    print("""Wieża hanoi
    
    Przenieś wieżę dysków, po jedym dysku naraz, na inną wieże. Większych dysków nie można umieszczać na mniejszych.""")

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
            