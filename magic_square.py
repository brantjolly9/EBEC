# Function to determine if a given matrix is a Lo Shu magic square

# Encase whole program in funct for reusability
def funct(matrix):

    # Assume the square is magical
    shu = True


    def rowSum(row):
        sum = 0
        for num in row:
            sum += num
        return sum

    # Find the row sum and check if it is 15
    for row in matrix:
        if rowSum(row) != 15:
            shu = False
            
    for i in range(3):
        colSum = 0
        for row in matrix:
            colSum += row[i]

    if colSum != 15:
        shu = False

    l2r = 0
    r2l = 0
    for i in range(3):
        l2r += matrix[i][i]
        r2l += matrix[2-i][2-i]

    if l2r != 15 and r2l != 15:
        shu = False
        
    print('Your matrix is:')
    for row in matrix:
        print(f'{row[0]} {row[1]} {row[2]}')

    if shu:
        print('It is a Lo Shu square!\n')
    else:
        print('It is not a Lo Shu magic square.\n')

matrix = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
matrix1 = [[4, 9, 2], [4, 5, 6], [7, 8, 9]]
matrix2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
matricies = [matrix, matrix1, matrix2]
for matrix in matricies:
    funct(matrix)




