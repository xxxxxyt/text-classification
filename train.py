#coding=utf-8

import os
import sys
import pickle
import numpy as np
import xgboost as xgb
import scipy
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":

    number_of_train_sample = 321910

    """ read in data """
    X_path = '../dataset/freq_mat.pkl'
    y_path = '../dataset/label.pkl'
    ifs = open(X_path, 'rb')
    X_train_test = pickle.load(ifs).tocsr()
    X_train = X_train_test[0 : number_of_train_sample]
    X_test = X_train_test[number_of_train_sample : ]
    print('opening file X has been done!')
    ifs = open(y_path, 'rb')
    y = np.array(pickle.load(ifs))
    print('opening file y has been done!')

    print('X_train shape: ', X_train.shape)
    print('X_test shape: ', X_test.shape)
    print('y shape: ', y.shape)

    """ train """
    data_train = xgb.DMatrix(X_train, label= y)
    xgb_params = {
        'seed' : 0,
        'colsample_bytree' : 0.7,
        'silent' : 1,
        'subsample' : 0.7,
        'learning_rate' : 0.1,
        'objective' : 'binary:logistic',
        'max_depth' : 4,
        'num_parallel_tree' : 1,
        'min_child_weight' : 2,
        'eval_metric' : 'auc',
        # 'base_score' : prior,
        'nthread' : 8,
        'eta' : 0.1
    }
    model = xgb.cv(xgb_params, data_train, \
                   num_boost_round= 10, \
                   watchlist= [(data_train, 'train')], \
                   nfold= 4, seed= 0, \
                   stratified= True, \
                   early_stopping_rounds= 1, \
                   verbose_eval= 1, \
                   show_stdv= True)
