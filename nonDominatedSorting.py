from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


import numpy as np
def sorting(nonDominated):
    '''
    for i in range(len(nonDominated)):
        for j in range(i+1,len(nonDominated)):
            if nonDominated[i][0]<=nonDominated[j][0] and nonDominated[i][1]<=nonDominated[j][1] and nonDominated[i][2]<= nonDominated[j][2]:

    vvv=list()
    vvv.append([1,2,3])
    vvv.append([4,3,0])
    vvv.append([1,1,1])
    '''
    abc=list()
    bca=list()
    for indexi,i in enumerate(nonDominated):
        for indexj,j in enumerate(nonDominated):
            if indexj!=indexi:
               if i[0]<=j[0] and i[1]<=j[1] and i[2]<=j[2] and i!=j:
                   abc.append(indexi)
                   bca.append(indexj)

    print abc
    if len(abc)<1:
        print "There is no dominated rules for all objective"
    aa=list()
    for k in range(3):
        aa.append(abc.count(k))
    print aa
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sequence_containing_x_vals =list()
    sequence_containing_y_vals =list()
    sequence_containing_z_vals =list()
    marker=list()
    color=list()
    size=list()
    '''
    for i in range(len(nonDominated)):
        if i<len(nonDominated)/3:
            marker.append('o')
            color.append('red')
            size.append(300)
        elif i>=len(nonDominated)/3 and i<2*(len(nonDominated))/3:
            marker.append('1')
            color.append('green')
            size.append(200)

        else:
            marker.append('2')
            color.append('blue')
            size.append(100)
    '''
    for i in range(len(nonDominated)):
        marker.append('o')
        color.append('red')
        size.append(50)

    for index,n in enumerate(nonDominated):
        sequence_containing_x_vals.append(n[0])
        sequence_containing_y_vals.append(n[1])
        sequence_containing_z_vals.append(n[2])
        m=marker[index]
        c=color[index]
        s=size[index]
        ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, c=c, marker=m,s=s)

    ax.set_xlabel('Cmax')
    ax.set_ylabel('Mean Lateness')
    ax.set_zlabel('Mean Flow Time')

    plt.show()


