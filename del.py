def multiply(matrix1, matrix2, matrixSizeRow1, matrixSizeColumn1, matrixSizeRow2, matrixSizeColumn2):
    resultantMatrix = []
    countMultiply = countAdd = 0
    for i in range(matrixSizeRow1):
        resultantRow = []
        for j in range(matrixSizeColumn2):
            dot_product=0
            for k in range(matrixSizeColumn1):
                dot_product = matrix1[i][k] * matrix2[k][j]
                countMultiply+=1
                countAdd+=1
            countAdd-=1
            resultantRow.append(dot_product)
        resultantMatrix.append(resultantRow)
        
        for row in resultantMatrix:
            print(" ".join(map(str, row)))
        print(countMultiply, countAdd)
    
matrixSize1 = list(map(int, input("").split()))
matrixSizeRow1 = matrixSize1[0]
matrixSizeColumn1 = matrixSize1[1]
matrix1=[]

for i in range(matrixSizeRow1):
    row1 = list(map(int, input("").split()))
    matrix1.append(row1)
    
matrixSize2 = list(map(int, input("").split()))
matrixSizeRow2 = matrixSize2[0]
matrixSizeColumn2 = matrixSize2[1]
matrix2=[]

for i in range(matrixSizeRow2):
    row2 = list(map(int, input("").split()))
    matrix2.append(row2)
    
if matrixSizeColumn1!=matrixSizeRow2:
    print("-1")
else:
    multiply(matrix1, matrix2, matrixSizeRow1, matrixSizeColumn1, matrixSizeRow2, matrixSizeColumn2)