def multiply(matrix1, matrix2, matrixSizeRows1, matrixSizeColumns1, matrixSizeRows2, matrixSizeColumns2):
    resultantMatrix = []
    countAdd=0
    countMultiply=0
    for i in range(matrixSizeRows1):
        resultantRow = []
        for j in range(matrixSizeColumns2):
            dot_product = 0
            for k in range(matrixSizeColumns1):
                dot_product += matrix1[i][k] * matrix2[k][j]
                countMultiply +=1
                countAdd +=1   
            countAdd -= 1
            resultantRow.append(dot_product)
        resultantMatrix.append(resultantRow)
    for row in resultantMatrix:
        print(' '.join(map(str, row)))
    print(countMultiply, countAdd)

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

if matrixSizeColumns1 != matrixSizeRows2 :
    print("-1")
else:
    multiply(matrix1, matrix2, matrixSizeRows1, matrixSizeColumns1, matrixSizeRows2, matrixSizeColumns2)