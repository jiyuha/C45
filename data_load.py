class Data(object):
    def __init__(self, keys, values):
        for (key, value) in zip(keys, values):
            self.__dict__[key] = value
        self.id = 0
        self.winner = ''
        self.usedCategorical = []
        self.predict = None


class Attribute:
    def __init__(self):
        self.name = None
        self.type = None


class Leaf:
    def __init__(self):
        self.rule = ''
        self.dataset = []
        self.terminateBuilding = False
        self.branch = 0
        self.parent = None
        self.id = None
        self.branchAttribute = None
        self.classes = None
        self.decision = []


def attribute_set(attribute, data):
    # attribute 의 데이터 타입(범주형 or 연속형)을 판단
    if len(set(map(lambda x: x.__getattribute__(attribute.name), data))) <= 20:
        attribute.type = 'Categorical'
    else:
        attribute.type = 'Continuous'


