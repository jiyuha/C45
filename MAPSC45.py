import numpy as np
import pandas as pd
import Training


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


def fit(data, attribute, config):
    # 나중에 함수들 다시 정리
    result = [i for i in Training.buildDecisionTree(data, attribute, config, start=True, max_depth=10)]
    rule_decision = []
    for i in result:
        rule_decision.append([i.rule, max(list(map(lambda x: x.Decision, i.dataset)),
                                          key=list(map(lambda x: x.Decision, i.dataset)).count)])
    for i in rule_decision:
        print(i[0])
    return rule_decision


def predict(test_data, rule_decision):
    for obj in test_data:
        for rule in rule_decision:
            if eval(rule[0]):
                obj.predict = rule[1]
    return test_data


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
