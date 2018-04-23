#coding=utf-8

import os
import sys
import pickle
import numpy as np
import xgboost as xgb
import scipy

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
    y_train = np.array(pickle.load(ifs))
    print('opening file y has been done!')

    print('X_train shape: ', X_train.shape)
    print('X_test shape: ', X_test.shape)
    print('y_train shape: ', y_train.shape)

    """ train """
    data_train = xgb.DMatrix(X_train, label= y_train)
    data_test = xgb.DMatrix(X_test)
    xgb_params = {
        'booster' : 'gbtree',
        'nthread' : 4,
        'silent' : True,
        'objective' : 'binary:logistic',
        'eta' : 0.05, # learning rate
        'max_depth' : 14,
        'min_child_weight' : 3,
        'colsample_bytree' : 1.0,
        'subsample' : 0.895, # 1.0
        # 'gamma' : 0.17,
        # 'lambda' : 2.5,
        # 'scale_pos_weight' : 1.0,
        # 'num_parallel_tree' : 1,
        'eval_metric' : 'auc'
    }
    print(xgb_params)
    model = xgb.train(xgb_params, data_train, \
                num_boost_round = 1000, \
                early_stopping_rounds= 5, \
                evals= [(data_train, 'train')])
    y_train_pred = model.predict(data_train)
    ofs = open('../dataset/y_train.pkl', 'wb')
    pickle.dump(y_train_pred, ofs)
    y_test = model.predict(data_test)
    ofs = open('../dataset/y_test.pkl', 'wb')
    pickle.dump(y_test, ofs)
    