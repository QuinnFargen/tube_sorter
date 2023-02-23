

from Sorting import TubeSorter

print("""
    ----------------------------------
    Welcome to The Ball Sorter
    ----------------------------------
    *** Enter balls as # or letter
    *** Enter tubes or rows comma seperated
    *** Enter empty tube as BLANK
    """)

# method = str(input("Will you enter COLS or ROWS: "))
width = int(input("How many tubes: "))
height = int(input("How many balls per tube: "))

tubes = []
for i in range(width):
    t = str(input("Enter Tube: ")).split(",")
    if t[0] == 'BLANK':
        tubes.append([])
        continue
    tubes.append(t)

print("""Tubes to be sorted: 
"""); print(tubes)

game = TubeSorter(matrix= tubes)

game.Sorter()

