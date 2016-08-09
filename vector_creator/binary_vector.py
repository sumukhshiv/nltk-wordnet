# takes in Functions.txt and motionIndex.txt
# outputs a vector for each object (sorted, not the same order as Functions.txt)
# output found in output.txt, found in same directory as this and accompanying files

def vector_creator(file1, file2):
    f = open(file1, 'r')
    g = open(file2, 'r')

    fo = open('output.txt', 'w').close()

    f_lines = f.readlines()
    g_lines = g.readlines()

    for index, line in enumerate(f_lines):
        f_lines[index] = line.rstrip()

    for index, line in enumerate(f_lines):
        f_lines[index] = line.split()


    w, h = len(g_lines), 175 # harcoded because Functions.txt goes to O174, but only 162 entries found in file
    matrix = [[0 for x in range(w)] for y in range(h)]

    for index, line in enumerate(f_lines):
        f_lines[index][0] = f_lines[index][0][1:]

    out = open("output.txt", "a")
    for i in f_lines:
        obj_num = int(float(i[0]))
        for x in i[2:]:
            motion_num = int(float(x[1:]))
            matrix[obj_num][motion_num] = 1



    #writes it out to output.txt
    for i in range(0,len(matrix)):
        out.write(str(i) + ": ")
        for x in matrix[i]:
            out.write(str(x) + " ")
        out.write(" \n")






vector_creator('Functions.txt', 'motionIndex.txt')
