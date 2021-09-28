import pandas as pd
import MAPSC45 as mc
import data_load
import time
from viztree import viztree
import pickle
import os


if __name__ == '__main__':
    total_time = time.time()
    start_time = time.time()
    filename = 'wine'
    df = pd.read_csv("dataset/"+filename+".csv")
    train_data, test_data = mc.data_split(df, 0.3)
    print(time.time() - start_time)
    attribute_name = [i.replace(' ', '') for i in df]

    # ===========================================================

    #train_data_value, test_data_value = mc.preprocessingData(train_data.to_numpy(), test_data.to_numpy())
    #train_data_value = train_data.to_numpy()
    test_data_value = test_data.to_numpy()
    train_data_value = df.to_numpy()
    #test_data_value = df.to_numpy()

    # ===========================================================

    train_data = [data_load.Data(attribute_name, train_data_value[i])
                  for i in range(train_data_value.shape[0])]  # train_data 의 모든 instance 들을 Data 클래스의 객체로 넣어줌
    for i in range(len(train_data)):
        train_data[i].id = i  # returnToOriginData 에 쓰기 위해 instance 마다 id를 부여
    test_data = [data_load.Data(attribute_name, test_data_value[i]) for i in
                 range(test_data_value.shape[0])]  # test_data 의 모든 instance 들을 Data 클래스의 객체로 넣어줌
    for i in range(len(test_data)):
        test_data[i].id = i  # returnToOriginData 에 쓰기 위해 instance 마다 id를 부여

    # ===========================================================
    # 데이터의 모든 attribute 를 Attribute 클래스의 객체로 넣어줌
    attribute = []
    for _name in attribute_name:
        _name = data_load.Attribute()
        attribute.append(_name)
    for _index in range(len(attribute)):
        attribute[_index].name = attribute_name[_index]
        data_load.attribute_set(attribute[_index], train_data)
        data_load.attribute_set(attribute[_index], test_data)

    # ===========================================================
    print(time.time() - start_time)
    config = {'algorithm': 'C4.5'}
    start_time = time.time()
    max_depth = 7
    if not os.path.exists('tree/'+filename+'_' + str(max_depth) + '.p'):
        tree = mc.createTree(train_data, test_data, attribute, config, filename, max_depth=max_depth)
    else:
        with open('tree/'+filename+'_' + str(max_depth) + '.p', 'rb') as file:
            tree = pickle.load(file)
        print("=================================")
        print('Creating time : ', time.time() - start_time)
    tree.test_data = test_data
    # ===========================================================
    start_time = time.time()
    tree.fit()
    print("=================================")
    print('Fitting time : ', time.time() - start_time)
    # ===========================================================
    start_time = time.time()
    viztree(tree.leaf, tree.root)  # Test set tree
    print("=================================")
    print('Visualizing : ', time.time() - start_time)
    # ===========================================================
    start_time = time.time()
    TP, FN, FP, TN = mc.evaluate(tree.test_data)
    print('Evaluate time : ', time.time() - start_time)
    # ===========================================================
    print('\nAccuracy : ', ((TP + TN)/len(test_data)) * 100, '%')
    if (TP + FP) > 0:
        print('Precision : ', (TP / (TP + FP)) * 100, '%')
    if (TP + FN) > 0:
        print('Recall : ', (TP / (TP + FN)) * 100, '%')
    if ((TP + FP) > 0) and ((TP + FN) > 0):
        print('F1 Score : ', ((2 * (TP / (TP + FP)) * (TP / (TP + FN))) / ((TP / (TP + FP)) + (TP / (TP + FN)))) * 100, '%')

    print('\n\nTotal time : ', time.time() - total_time)