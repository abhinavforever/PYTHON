rows = int(input("no. of rows: "))
cols = int(input("no. of cols: "))
list_outer = []
list_inner = []
# each row
for i in range(0, rows, 1):
    # each column
    for j in range(0, cols, 1):
        list_inner.append(int(input()))
        if (j == cols-1):
            list_outer.append(list_inner)
            list_inner = []
for i in range(0, rows, 1):
    print(list_outer[i])
    
for i in range(0, cols, 1):
    print(list_outer[0][i], end=" ")
for i in range(1, rows, 1):
    print(list_outer[i][cols-1], end=" ")
for i in range(-2, -(cols+1), -1):
    print(list_outer[rows-1][i], end=" ")
for i in range(-2, -rows, -1):
    print(list_outer[i][0], end=" ")
for i in range(1, 2, 1):
    print(list_outer[1][i], end=" ")
