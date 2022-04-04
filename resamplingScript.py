import pandas as pd
import random


def resample_data(data):
    """
    sample uniformly at random for the set of real values
    :param data: dataframe
    :return: column values sampled from real data
    """

    numCols = len(data.columns)
    numRows = len(data.index)

    newCol = []
    for row in range(numRows):

        col = random.randint(0, numCols - 1)

        value = data.loc[row][col]

        # print(value)
        newCol.append(value)

    return newCol


file = "27025989_S1_raw.csv"
data = pd.read_csv(file, na_values=['-', 'ND'], header=[0])
data = data.fillna(0)


generated1 = resample_data(data)
generated2 = resample_data(data)

data['Fake1'] = generated1
data['Fake2'] = generated2
print(data)

data.to_csv('27025989_S1_fake_resampled.csv')
