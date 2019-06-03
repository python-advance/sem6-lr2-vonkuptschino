import threading
#
def calc_element(row, col):
    res = 0
    for i, item in enumerate(row):
        res += item * col[i]
    return res

def calc_row(rowA, B):
    cols = [[row[i] for row in B] for i in range(len(B[0]))]
    res = list(map(lambda x: calc_element(rowA, x), cols))
    print(res)
    return res

def calc_numpy(A, B):
	import numpy
	print(numpy.dot(A, B))

if __name__ == "__main__":

	A = [[7, 8, 4, 1], [7, 8, 2, 1], [1, 2, 3, 1], [4, 3, 2, 1]]
	B = [[9, 8, 4, 1], [8, 7, 1, 1], [1, 2, 3, 1], [4, 3, 2, 1]]

	for row in A:
		print('tread for row {}'.format(row))
		threading.Thread(target=calc_row, args=(row, B)).start()

	print('\n\n')
	calc_numpy(A,B)