

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

matrix = []
for i in range(width):
    t = str(input("Enter Tube: ")).split(",")
    if t[0] == 'BLANK':
        matrix.append([])
        print(matrix)
        continue
    matrix.append(t)
    print(matrix)

print(matrix)
