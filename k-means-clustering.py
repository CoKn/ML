import random
import math
import copy

dp_list = []
cc_list = []
accuracy = 0


def create_data():
    """function to create m random data points in n dimensions"""
    print('How many data points do you want to create?')
    input_data = input()
    print('How many dimensions should your data points have?')
    input_dimensions = input()
    global dp_list
    for i in range(0, int(input_data)):
        dp_list.append(list())
        dp_list[i].append(list())
        dp_list[i].append(list())
        for j in range(int(input_dimensions)):
            dp_list[i][1].append(random.randint(0, 50))
    print(dp_list)
    return dp_list


def create_cc():
    """function to create cluster centers"""
    print('How many clusters do you want to have?')
    input_cluster_number = input()
    global cc_list
    for i in range(0, int(input_cluster_number)):
        if cc_list is []:
            cc_list.append(dp_list[random.randint(0, len(dp_list) - 1)][1])
        else:
            cc_list.append(dp_list[random.randint(0, len(dp_list) - 1)][1])
            while cc_list[i] in cc_list[:-1]:
                cc_list[i] = dp_list[random.randint(0, len(dp_list) - 1)][1]
    print(cc_list)
    return cc_list


def define_accuracy():
    """function to define the accuracy of the clusters"""
    print('Set your accuracy.')
    global accuracy
    accuracy = float(input())
    while 0 > accuracy or accuracy > 1:
        print('The accuracy can not be higher than 1!')
        accuracy = float(input())
    return accuracy


def cluster_data():
    """function to calculate the euclidean distance and selecting a cluster for each data point"""
    distance_list = []
    euclidean_d = []
    for i in range(len(dp_list)):
        for j in range(len(cc_list)):
            for k in range(len(cc_list[0])):
                distance_list.append((dp_list[i][1][k] - cc_list[j][k]) ** 2)
            euclidean_d.append(math.sqrt(sum(distance_list)))
            distance_list.clear()
        dp_list[i][0] = euclidean_d.index(min(euclidean_d))
        euclidean_d.clear()
    return dp_list


def relocate_clusters():
    """function to relocate cluster centers"""
    for i in range(len(cc_list)):
        for j in range(len(cc_list[i])):
            sum_list = []
            n = 0
            mean = 0
            for k in range(len(dp_list)):
                if i == dp_list[k][0]:
                    sum_list.append(dp_list[k][1][j])
                    n += 1
            if n > 0:
                mean = sum(sum_list) / n
            cc_list[i][j] = mean
    return cc_list


def loop_functions():
    """loop functions cluster_data and relocate_clusters until the centers dose not change any more"""
    old = copy.deepcopy(relocate_clusters())
    cluster_data()
    new = copy.deepcopy(relocate_clusters())
    cluster_data()
    while old != new:
        acc_list = []
        difference_list = []
        for i in range(len(old)):
            for j in range(len(old[i])):
                difference_list.append(math.sqrt((old[i][j] - new[i][j])**2))
                acc_list.append(old[i][j] * (1 - accuracy))
        if sum(difference_list) <= sum(acc_list):
            break
        old = new
        new = copy.deepcopy(relocate_clusters())
        print(new)
    print('Final centers at: ' + str(new))
    return new


create_data()
create_cc()
define_accuracy()
cluster_data()
loop_functions()
