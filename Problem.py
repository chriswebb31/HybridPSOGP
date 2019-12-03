import math
import pandas as pd
import numpy as np

class Problem:
    def __init__(self, train_data, test_data):
        self.train_data = train_data
        self.test_data = test_data

    def defineProblem(self):
        self.targets = []
        self.values = []
        data = pd.read_csv(self.train_data)
        for record in data.values:
            self.values.append(record[1:])
            self.targets.append(record[0])

    def testProblem(self, solution):
        self.test_targets = []
        self.test_values = []
        data = pd.read_csv(self.test_data)
        for record in data.values:
            self.test_values.append(record[1:])
            self.test_targets.append(record[0])
        total = 0
        for i in range(len(self.test_targets)):
            total += abs(np.sum(np.multiply(self.test_values[i], solution)) - self.test_targets[i])
        average_cost = total / len(self.test_targets)
        # print(average_cost)
        return average_cost
