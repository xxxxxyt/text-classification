#coding=utf-8

import os
import sys
import pickle
import numpy as np
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":

    number_of_train_sample = 321910

    """ read in data """
    X_path = '../dataset/freq_mat.pkl'
    y_path = '../dataset/label.pkl'
    ifs = open(X_path, 'rb')
    X = pickle.load(ifs)[0 : number_of_train_sample]
    print('opening file X has been done!')
    ifs = open(y_path, 'rb')
    y = pickle.load(ifs)[0 : number_of_train_sample]
    print('opening file y has been done!')
    
    