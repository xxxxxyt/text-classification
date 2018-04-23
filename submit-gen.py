#coding=utf-8

import os
import sys
import pickle
import numpy as np

if __name__ == "__main__":
    """ read in data """
    ifs = open('../dataset/sample_submission.csv', 'r')
    id = ifs.read().split('\n')
    id = id[1 : -1]
    id = [line.split(',')[0] for line in id]
    ifs = open('../dataset/y_test.pkl', 'rb')
    y_test = pickle.load(ifs)
    m = len(id)
    print('len id : ', m)
    print('len y_test: ', len(y_test))
    submit = [(id[i] + ',' + str(y_test[i])) for i in range(m)]
    submit.insert(0, 'id,pred')

    """ write out data """
    ofs = open('../dataset/submit.csv', 'w')
    ofs.write('\n'.join(submit))
