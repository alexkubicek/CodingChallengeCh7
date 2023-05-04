import math


global all_clusters


def get_distance(one, two):
    global OGMATRIX
    distance = 0
    for point in one:
        for second_point in two:
            distance += OGMATRIX[point][second_point]
    distance /= (len(one)) * (len(two))
    return distance


def join_clusters(two_clusters):
    global matrix
    new_cluster = []
    for c in two_clusters:
        for cl in c:
            new_cluster.append(cl)
    print(two_clusters)
    print(new_cluster)
    new_cluster = tuple(new_cluster)
    del matrix[two_clusters[0]]
    del matrix[two_clusters[1]]
    new_distances = {}
    for key in matrix.keys():
        new_distances[key] = get_distance(key, new_cluster)
        matrix[key][new_cluster] = new_distances[key]
        del matrix[key][two_clusters[0]]
        del matrix[key][two_clusters[1]]
    new_distances[new_cluster] = float(0)
    matrix[new_cluster] = new_distances
    return new_cluster


def get_closest(cur_clusters):
    global age, all_clusters, my_cluster_counter
    min_dist = math.inf
    closest_clusters = ()
    closest_clust_nums = ()
    for cluster in cur_clusters:
        for second_cluster in cur_clusters:
            cur_distance = matrix[all_clusters[cluster]][all_clusters[second_cluster]]
            if cur_distance == 0:
                continue
            if cur_distance < min_dist:
                min_dist = cur_distance
                closest_clust_nums = (cluster, second_cluster)
                closest_clusters = (all_clusters[cluster], all_clusters[second_cluster])
    age[my_cluster_counter] = min_dist/2
    return closest_clusters, closest_clust_nums


def UPGMA():
    global n, matrix, age, my_cluster_counter, all_clusters
    all_clusters = {}
    clusters = []
    T = {}
    for my_int in range(n):
        all_clusters[my_int] = (my_int,)
        clusters.append(my_int)
        T[my_int] = ()
        age[my_int] = 0
    while len(clusters) > 1:
        print(age)
        closest = get_closest(clusters)
        closest_nums = closest[1]
        closest = closest[0]
        for clus in closest:
            for point in clus:
                print(point, end=" ")
        print()
        newest = join_clusters(closest)
        T[my_cluster_counter] = closest_nums
        all_clusters[my_cluster_counter] = newest
        clusters.append(my_cluster_counter)
        my_cluster_counter += 1
        for my_int in range(2):
            clusters.remove(closest_nums[my_int])
    # print(T)
    # exit(1)
    root = T[my_cluster_counter - 1]
    stack = [root]
    edges = {}
    while len(stack) > 0:
        cur = stack.pop()
    for parent in T.keys():
        for child in T[parent]:
            edges[(parent, child)] = age[parent] - age[child]
            edges[(child, parent)] = edges[(parent, child)]
    return edges


FILEPATH = "./dataset_873232_8.txt"

inFile = open(FILEPATH)

n = int(inFile.readline().strip("\n\t "))

matrix = {}
OGMATRIX = {}
i = 0
while line := inFile.readline():
    OGMATRIX[i] = {}
    matrix[(i,)] = {}
    j = 0
    line = line.strip("\n\t ").split(" ")
    for num in line:
        OGMATRIX[i][j] = float(num)
        matrix[(i,)][(j,)] = (float(num))
        j += 1
    i += 1

# print(matrix)
# print(OGMATRIX)
inFile.close()
age = {}
my_cluster_counter = n
answer = UPGMA()
key_list = list(answer.keys())
key_list.sort()
for key in key_list:
    print(str(key[0]) + "->" + str(key[1]) + ":" + "{:0.2f}".format(answer[key]))
