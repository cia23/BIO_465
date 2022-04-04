import pandas as pd
import random


def random_data(real_data):
    """
    :param real_data: dataframe
    :return: list of n values falling in the original range of the real data
    """

    numRows = len(real_data.index)

    newCol = []
    for row in range(numRows):

        theRow = real_data.iloc[row]

        scale_adj = 10000000.0

        minimum = min(theRow) * scale_adj
        maximum = max(theRow) * scale_adj

        value = random.uniform(minimum, maximum)

        valueToAdd = value / scale_adj

        newCol.append(valueToAdd)

    return newCol


random.seed(0)

file = "27025989_S1_raw.csv"
data = pd.read_csv(file, na_values=['-', 'ND'], header=[0])
data = data.fillna(0)


generated1 = random_data(data)
generated2 = random_data(data)

data['Fake1'] = generated1
data['Fake2'] = generated2
print(data)

data.to_csv('27025989_S1_fake_random.csv')