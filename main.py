import pandas as pd
import MAPSC45 as mc
import data_load
import time
#from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    start_time = time.time()
    df = pd.read_csv("dataset/wine.csv")
    train_data, test_data = mc.data_split(df, 0.3)
    attribute_name = [i.replace(' ', '') for i in df]

    # ===========================================================

    train_data_value = train_data.to_numpy()
    test_data_value = test_data.to_numpy()

    # ===========================================================

    train_data = [data_load.Data(attribute_name, train_data.iloc[i]) for i in
                  range(train_data_value.shape[0])]  # train_data 의 모든 instance 들을 Data 클래스의 객체로 넣어줌
    for i in range(len(train_data)):
        train_data[i].id = i  # returnToOriginData 에 쓰기 위해 instance 마다 id를 부여
    test_data = [data_load.Data(attribute_name, test_data.iloc[i]) for i in
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

    # ===========================================================

    config = {'algorithm': 'C4.5'}
    rule_decision = mc.fit(train_data, attribute, config)
    print("=================================")
    print('Fitting time : ', time.time() - start_time, 'seconds')
    print("=================================")
    test_data = mc.predict(test_data, rule_decision)
    TP, FN, FP, TN = mc.evaluate(test_data)
    print('Accuracy : ', ((TP + TN)/len(test_data)) * 100, '%')
    print('Precision : ', (TP / (TP + FP)) * 100, '%')
    print('Recall : ', (TP / (TP + FN)) * 100, '%')
    print('F1 Score : ', ((2 * (TP / (TP + FP)) * (TP / (TP + FN))) / ((TP / (TP + FP)) + (TP / (TP + FN)))) * 100, '%')

