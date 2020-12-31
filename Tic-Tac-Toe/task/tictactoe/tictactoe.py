# write your code here
cells = input("Enter cells:")
c = list(cells)
print("---------")
print("|", " ".join(c[:3]), "|", sep=" ")
print("|", " ".join(c[3:6]), "|", sep=" ")
print("|", " ".join(c[6:]), "|", sep=" ")
print("---------")

three_x_in_row = (
    (c[0] == c[1] == c[2] == "X")
    or (c[0] == c[3] == c[6] == "X")
    or (c[0] == c[4] == c[8] == "X")
    or (c[2] == c[4] == c[6] == "X")
    or (c[2] == c[4] == c[6] == "X")
    or (c[2] == c[5] == c[8] == "X")
    or (c[6] == c[7] == c[8] == "X")
    or (c[1] == c[4] == c[7] == "X")
    or (c[3] == c[4] == c[5] == "X")
)
print(three_x_in_row)
three_o_in_row = (
    (c[0] == c[1] == c[2] == "O")
    or (c[0] == c[3] == c[6] == "O")
    or (c[0] == c[4] == c[8] == "O")
    or (c[2] == c[4] == c[6] == "O")
    or (c[2] == c[4] == c[6] == "O")
    or (c[2] == c[5] == c[8] == "O")
    or (c[6] == c[7] == c[8] == "O")
    or (c[1] == c[4] == c[7] == "O")
    or (c[3] == c[4] == c[5] == "O")
)
print(three_o_in_row)
empty_cell = "_" in c
count_x = c.count("X")
count_o = c.count("O")

if (three_o_in_row and three_x_in_row) or abs(count_x - count_o) > 1:
    print("Impossible")
elif three_o_in_row:
    print("O wins")
elif three_x_in_row:
    print("X wins")
elif empty_cell:
    print("Game not finished")
else:
    print("Draw")
