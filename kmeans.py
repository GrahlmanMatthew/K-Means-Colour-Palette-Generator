import sys
import math
import random
import numpy as np

# Generates a random RGB Colour tuple
def colour():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Calculates the Euclidean Distance between a Colour and a Point
def euclidean_distance(clr, pnt):
    diff_r, diff_g, diff_b = math.pow((clr[0] - pnt[0]), 2), math.pow((clr[1] - pnt[1]), 2), math.pow((clr[2] - pnt[2]), 2)
    sum = diff_r + diff_g + diff_b
    euclid_dis = math.sqrt(sum)
    return math.sqrt(euclid_dis)

# K-Means Clustering Algorithm
def kmeans(k, colours_list):

    # Step #1 - randomly select K points (*not from dataset in this case)
    k_points = []
    for x in range(0, k):
        k_points.append([colour()])

    # Begin "Training"
    for counter in range(0, k * 2):
        cluster_members = []    # list of lists to track colour-cluster memberships
        for x in range(0, k):
            cluster_members.append([])

        # Step #2 - determines cluster ownership for each colour in the image
        for col in colours_list:
            bf = sys.maxsize        # best fit
            clust_id = -1
            for point in k_points:
                cluster_rgb = (point[0][0], point[0][1], point[0][2])
                if (dist := euclidean_distance(col[0], cluster_rgb)) < bf:
                    bf = dist
                    clust_id = k_points.index(point)
            cluster_members[clust_id].append(col[0])

        # Step #3 - computes location of new centroids
        index = 0
        for cluster in cluster_members:
            num_members = len(cluster)
            sum_r, sum_g, sum_b = 0, 0, 0
            if not num_members == 0:
                for member in cluster:
                    sum_r, sum_g, sum_b = sum_r + member[0], sum_g + member[1], sum_b + member[2]
                avg_r, avg_g, avg_b = int(sum_r / num_members), int(sum_g / num_members), int(sum_b / num_members)
                k_points[index] = [(avg_r, avg_g, avg_b)]
            else:
                k_points[index] = [(255, 255, 255)]
            index = index + 1
    
    return np.array(k_points, dtype=np.uint8)