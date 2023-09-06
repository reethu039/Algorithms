def add(matrix1, matrix2, matrixSizeRows, matrixSizeColumns):
    resultantMatrix = []
    count=0
    for i in range(matrixSizeRows):
        resultantRow = []
        for j in range(matrixSizeColumns):
            resultantRow.append(matrix1[i][j] + matrix2[i][j])
            count+=1
        resultantMatrix.append(resultantRow)
    for row in resultantMatrix:
        print(' '.join(map(str, row)))
    print(count)

MatrixSize1 = list(map(int, input("").split()))
matrixSizeRows1 = MatrixSize1[0]
matrixSizeColumns1 = MatrixSize1[1]
matrix1 = []

for i in range(matrixSizeRows1):
    row1 = list(map(int, input().split()))
    matrix1.append(row1)

MatrixSize2 = list(map(int, input("").split()))
matrixSizeRows2 = MatrixSize2[0]
matrixSizeColumns2 = MatrixSize2[1]
matrix2 = []

for i in range(matrixSizeRows2):
    row2 = list(map(int, input().split()))
    matrix2.append(row2)

if matrixSizeRows1 != matrixSizeRows2 or matrixSizeColumns1 != matrixSizeColumns2:
    print("-1")
else:
    add(matrix1, matrix2, matrixSizeRows1, matrixSizeColumns1)