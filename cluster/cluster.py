import scipy.cluster.hierarchy as hac

def cluster(file):
    f = open(file, 'r')
    fo = open('cluster.txt', 'w').close()

    f_lines = f.readlines()
    for index, line in enumerate(f_lines):
        f_lines[index] = line.rstrip()

    for index, line in enumerate(f_lines):
        f_lines[index] = line.split()



    w, h = len(f_lines[0]) - 1, len(f_lines)
    matrix = [[0 for x in range(w)] for y in range(h)]

    # print f_lines
    # print matrix
    # print len(f_lines)
    # print len(matrix)
    # print len(matrix[0])

    for i in range(0,len(matrix)):
        matrix[i] = f_lines[i][2:]

    print (f_lines[0])
    print(matrix[0])

    # z = hac.linkage(matrix)
    # print z



    out = open("cluster.txt", "a")

cluster('report.txt')
