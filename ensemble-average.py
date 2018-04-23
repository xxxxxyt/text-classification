#coding=utf-8

import os
import sys
import pickle
import numpy as np

if __name__ == "__main__":

    res_dir = [
        # '90478',
        # '90484',
        # '90489', 
        # '90497',
        # '90511',
        # '90522',
        # '90531',
        # '90570',
        '90628_',
        '90637',
        '90679',
        'new'
    ]

    y_test = np.zeros(40239)
    y_train = np.zeros(321910)
    n = len(res_dir)

    for i in range(n):
        dir = '../dataset/predict/' + res_dir[i] + '/'
        ifs = open(dir + 'y_test.pkl', 'rb')
        tmp = pickle.load(ifs)
        y_test += tmp
        # ifs = open(dir + 'y_train.pkl', 'rb')
        # tmp = pickle.load(ifs)
        # y_train += tmp

    y_test /= n
    # y_train /= n

    print(y_test)
    # print(y_train)

    # """
    # ofs = open('../dataset/y_train.pkl', 'wb')
    # pickle.dump(y_train, ofs)
    ofs = open('../dataset/y_test.pkl', 'wb')
    pickle.dump(y_test, ofs)
    # """
