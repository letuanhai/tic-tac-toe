cells = input("Enter cells:")
c = list(cells)
print("---------")
print("|", " ".join(c[:3]), "|", sep=" ")
print("|", " ".join(c[3:6]), "|", sep=" ")
print("|", " ".join(c[6:]), "|", sep=" ")
print("---------")

# Make an array of possible winning positions
win_pos = [
    c[0] + c[1] + c[2],
    c[0] + c[3] + c[6],
    c[0] + c[4] + c[8],
    c[2] + c[4] + c[6],
    c[2] + c[4] + c[6],
    c[2] + c[5] + c[8],
    c[6] + c[7] + c[8],
    c[1] + c[4] + c[7],
    c[3] + c[4] + c[5],
]

empty_cell = "_" in c
count_x = c.count("X")
count_o = c.count("O")

if ("XXX" in win_pos and "OOO" in win_pos) or abs(count_x - count_o) > 1:
    print("Impossible")
elif "OOO" in win_pos:
    print("O wins")
elif "XXX" in win_pos:
    print("X wins")
elif empty_cell:
    print("Game not finished")
else:
    print("Draw")
