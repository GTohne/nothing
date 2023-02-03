
def SparseMatrixMultiply(A, B):#减少计算次数
    res = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != 0:#non-zero
                for k in range(len(B[0])):
                    if B[j][k] != 0:#non-zero
                        res[i][k] += A[i][j] * B[j][k]
    return res
if __name__ == '__main__':
    A = [[1,0,0],[-1,0,3]]
    B = [[7,0,0],[0,0,0],[0,0,1]]
    result = SparseMatrixMultiply(A, B)

