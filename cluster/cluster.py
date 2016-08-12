from sklearn.cluster import AffinityPropagation
from sklearn import metrics as met
import matplotlib.pyplot as plt
from itertools import cycle


def cluster(file):
    f = open(file, 'r')
    g = open('objects.txt', 'r')
    fo = open('cluster.txt', 'w').close()
    fo = open('cluster_words.txt', 'w').close()

####### FILE PARSING #######
    f_lines = f.readlines()
    g_lines = g.readlines()

    for index, line in enumerate(f_lines):
        f_lines[index] = line.rstrip()

    for index, line in enumerate(g_lines):
        g_lines[index] = line.rstrip('\r\n')

    for index, line in enumerate(f_lines):
        f_lines[index] = line.split()

    w, h = len(f_lines[0]) - 1, len(f_lines)
    matrix = [[0 for x in range(w)] for y in range(h)]

    for i in range(0,len(matrix)):
        matrix[i] = f_lines[i][2:]
####### END FILE PARSING #######

####### DATA CLUSTERING #######
    X = met.pairwise_distances(matrix)
    af = AffinityPropagation(preference=-100).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_

    n_clusters_ = len(cluster_centers_indices)

    # print('Estimated number of clusters: %d' % n_clusters_)
####### END DATA CLUSTERING #######


####### OUTPUT ARRAY #######
    i = 0
    output_arr = []
    while i < n_clusters_:
        output_arr.append([])
        i += 1
    labels_list = labels.tolist()

    index = 0
    for x in labels_list:
        output_arr[x].append(index)
        index += 1

    # print(labels_list)
    # print(output_arr)
####### END OUTPUT ARRAY #######


####### FILE OUTPUT #######
    out = open("cluster.txt", "a")
    out2 = open("cluster_words.txt", "a")
    for x in output_arr:
        out.write(str(output_arr.index(x)) + " : ") # extra info -- " (" + str(len(x)) + " elements)"+
        out2.write(str(output_arr.index(x)) + " : ")
        for elem in x:
            out.write(str(elem) + " ")
            out2.write(g_lines[elem] + " ")
        out.write("\n")
        out2.write("\n")


    # print output_arr
####### END FILE OUTPUT #######


####### DATA PLOTTING #######
    # plt.close('all')
    # plt.figure(1)
    # plt.clf()
    #
    # colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    # for k, col in zip(range(n_clusters_), colors):
    #     class_members = labels == k
    #     cluster_center = X[cluster_centers_indices[k]]
    #     plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
    #     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
    #              markeredgecolor='k', markersize=14)
    #     for x in X[class_members]:
    #         plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
    #
    # plt.title('Estimated number of clusters: %d' % n_clusters_)
    # plt.show()
####### END DATA PLOTTING #######

print('*** Clustering Completed! Output recorded in cluster.txt. Output with object names recorded in cluster_words.txt. ***')

cluster('report.txt')
