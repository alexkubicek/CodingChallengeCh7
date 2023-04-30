import math


def LimbLength(matrix, j, num_nodes):
    minVal = math.inf
    for i in range(num_nodes):
        if i == j:
            continue
        for k in range(num_nodes):
            if k == j:
                continue
            temp = (matrix[i][j] + matrix[j][k] - matrix[i][k])/2
            if temp < minVal:
                minVal = temp
    return minVal


FILEPATH = './dataset_873229_11.txt'

inFile = open(FILEPATH)

size = int(inFile.readline().strip("\n\t "))
leaf = int(inFile.readline().strip("\n\t "))

distance_matrix = []
while line := inFile.readline().strip("\n\t "):
    distance_matrix.append([])
    split_line = line.split(' ')
    for node in split_line:
        distance_matrix[-1].append(int(node))

print(int(LimbLength(distance_matrix, leaf, size)))
