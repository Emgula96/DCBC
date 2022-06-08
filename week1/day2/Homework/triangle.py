n = 5
for rows in range(n):
    for j in range(rows, n):
        print(' ', end=' ')
    for j in range(rows):
        print('*', end=' ')
    for j in range(rows-1):
        print('*',end=' ')
    print()