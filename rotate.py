import numpy as np


def rotate(array):
    temp = np.zeros_like(array.transpose())
    for j in range(len(array)):
        for i in range(len(array[0])):
            temp[i][j] = array[j][len(array[0])-i-1]
    return temp

def ninety_degrees(array):
    temp = np.zeros_like(array.transpose())
    for j in range(len(array)):
        for i in range(len(array[0])):
            temp[i][j] = array[j][len(array[0])-i-1]
    return temp
a = np.array([[1, 2, 3], [4,5,6], [7,8,9]])
temp = np.zeros_like(a.transpose())
print(len(a[0]))
print(a[0][2])