import numpy as np
import pandas as pd
import Training
from data_load import DT
import time
import pickle


def data_split(data, _portion: float):
    target_unique = data['Decision'].unique()
    data_0 = data[data['Decision'] == target_unique[0]]
    data_1 = data[data['Decision'] == target_unique[1]]

    sample_data_0 = int(len(data_0) * _portion)
    sample_data_1 = int(len(data_1) * _portion)

    train_data_0 = data_0.take(np.random.permutation(len(data_0))[:(1 - sample_data_0)])
    train_data_1 = data_1.take(np.random.permutation(len(data_1))[:(1 - sample_data_1)])
    train_data = pd.concat([train_data_0, train_data_1], axis=0)

    test_data_0 = data_0.take(np.random.permutation(len(data_0))[:sample_data_0])
    test_data_1 = data_1.take(np.random.permutation(len(data_1))[:sample_data_1])
    test_data = pd.concat([test_data_0, test_data_1], axis=0)

    return train_data, test_data


def createTree(train_data, test_data, attribute, config, filename, max_depth=7):
    start_time = time.time()
    result_leaf, leaf_list, root = Training.buildDecisionTree(train_data, attribute, config, max_depth=max_depth)
    print("\n=================================")
    print('Creating Tree : ', time.time() - start_time)
    print("=================================")
    result = [i for i in result_leaf]
    rule_decision = []
    for i in result:
        rule_decision.append([i.rule, max(list(map(lambda x: x.Decision, i.dataset)),
                                          key=list(map(lambda x: x.Decision, i.dataset)).count)])

    # ===========================================================
    tree = DT()
    tree.leaf = leaf_list
    tree.root = root
    tree.rule_decision = rule_decision
    with open('tree/'+filename + '_'+str(max_depth)+'.p', 'wb') as file:  # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
        pickle.dump(tree, file)

    return tree


def evaluate(test_data):
    TP, FN, FP, TN = 0, 0, 0, 0
    for i in test_data:
        if (i.Decision == 'good') and (i.predict == 'good'):
            TP += 1
        elif (i.Decision == 'good') and (i.predict == 'bad'):
            FN += 1
        elif (i.Decision == 'bad') and (i.predict == 'good'):
            FP += 1
        else:
            TN += 1
    return TP, FN, FP, TN


def preprocessingData(train_data_value, test_data_value):
    decision = set(map(lambda x: x[-1], train_data_value))
    for _index, _decision in enumerate(decision):
        for _data in train_data_value:
            if _data[-1] == _decision:
                _data[-1] = _index
        for _data in test_data_value:
            if _data[-1] == _decision:
                _data[-1] = _index
    return train_data_value, test_data_value
