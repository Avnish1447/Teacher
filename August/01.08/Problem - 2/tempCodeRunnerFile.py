def solve():
    row_of_one = -1
    col_of_one = -1
    for i in range(1, 6):
        row = list(map(int, input().split()))
        for j in range(1, 6):
            if row[j-1] == 1:
                row_of_one = i
                col_of_one = j
                break
        if row_of_one != -1:
            for _ in range(5 - i):
                input()
            break
    row_moves = abs(row_of_one - 3)
    col_moves = abs(col_of_one - 3)

    total_moves = row_moves + col_moves
    print(total_moves)

solve()