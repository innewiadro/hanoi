import copy
import sys

TOTAL_DISC = 6
SOLVED_TOWER = list(range(TOTAL_DISC, 0, -1))


def main():
    print("""Wieża hanoi
    
    Przenieś wieżę dysków, po jedym dysku naraz, na inną wieże. Większychdysków nie można umieszczać na mniejszych.""")

    towers = {"A":copy.copy(SOLVED_TOWER), "B":[], "C": []}

    while True:
        displays(towers)


def get_player_move(towers):
    pass

def display_towers(towers):
    pass


def display_disk(width):
    pass