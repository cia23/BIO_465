import pandas as pd
import random

def random_data(real_data):
    """
    :param real_data: dataframe
    :return: list of n values falling in the original range of the real data
    """

    random.seed(0)
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


def generate_random(data):
    data = data.fillna(0)

    generated1 = random_data(data)
    data['random'] = generated1
    return data


def resample_data(data):
    random.seed(0)
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


def generate_resampled(data):
    data = data.fillna(0)
    generated1 = resample_data(data)
    data['resampled'] = generated1
    return data


def generate_imputed_mean(data):
    data['mean'] = data.mean(axis=1)
    return data


def generate_imputed_median(data):
    data['median'] = data.median(axis=1)
    return data
