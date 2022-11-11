"""A. IQ Test - Code Forces"""
matrix = []
for arr in range(4):
    # Fill matrix with [arr/line]
    matrix.append(list(input()))
# Loop over line(Array)
for i in range(3):
    # Loop over values in line(Array) 
    for k in range(3):
        square = matrix[i][k] + matrix[i][k+1] + matrix[i+1][k] + matrix[i+1][k+1]
        # if ### or .... -> yes after flipping one value, more -> existed already
        if square.count('#') >= 3 or square.count('.') >= 3:
            print('YES')
            # Exit whole code
            exit()
print('NO')
