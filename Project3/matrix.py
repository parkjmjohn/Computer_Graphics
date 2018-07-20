import math

def print_matrix( matrix ):
    for row in range(len(matrix[0])):
        ret=""
        for col in range(len(matrix)):
            ret+=str(matrix[col][row])+"\t"
        print ret

def ident( matrix ):
    ret = new_matrix(len(matrix), len(matrix[0]))
    for row in range(0, len(matrix)):
    	for col in range(0, len(matrix[0])):
    		if col==row:
    			ret[row][col]=1
    return ret

def scalar_mult( matrix, s ):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = int(matrix[row][col] * s)
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    matrix=[]
    for row in range(len(m2)):
        matrix.append([])
        for col in range(4):
            ret=m1[1][col]*m2[row][1]+m1[2][col]*m2[row][2]+m1[3][col]*m2[row][3]+m1[0][col]*m2[row][0]
            matrix[row].append(ret)
    return matrix

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
