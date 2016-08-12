from sklearn.cluster import AffinityPropagation
from sklearn import metrics as met
import matplotlib.pyplot as plt
from itertools import cycle


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

    # print (f_lines[0])


    # z = hac.linkage(matrix)
    # print z

    X = met.pairwise_distances(matrix)
    af = AffinityPropagation().fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_

    n_clusters_ = len(cluster_centers_indices)

    print('Estimated number of clusters: %d' % n_clusters_)
    # print("Homogeneity: %0.3f" % met.homogeneity_score(labels_true, labels))
    # print("Completeness: %0.3f" % met.completeness_score(labels_true, labels))
    # print("V-measure: %0.3f" % met.v_measure_score(labels_true, labels))
    # print("Adjusted Rand Index: %0.3f"
    #       % met.adjusted_rand_score(labels_true, labels))
    # print("Adjusted Mutual Information: %0.3f"
    #       % met.adjusted_mutual_info_score(labels_true, labels))
    # print("Silhouette Coefficient: %0.3f"
    #       % met.silhouette_score(X, labels, metric='sqeuclidean'))

    i = 0
    output_arr = []
    while i < n_clusters_:
        output_arr.append([])
        i += 1
    labels_list = labels.tolist()
    print labels_list

    index = 0
    for x in labels_list:
        output_arr[x].append(index)
        index += 1


    print(labels_list)
    print(output_arr)



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
    # out = open("cluster.txt", "a")

cluster('report.txt')
