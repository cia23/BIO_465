import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


PERCENT_TO_KEEP = .1
MIN_TO_KEEP = 100


# get the frequencies of each number from inputted list
def get_frequencies(nums):
    freqs_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in nums:
        if not pd.isna(num):
            freqs_list[num] += 1
    freqs_df = pd.DataFrame(freqs_list, index=range(0, 10), columns=['freq'])

    return freqs_df


# returns the first digit after the decimal point
def first_after_decimal(num):
    # if (abs(num) < 1):
    #     return int((abs(num) * 10) % 10)
    if pd.isna(num):
        return
    return int((abs(float(num)) * 10) % 10)


# returns the non-zero digit
def first_digit(num):
    if pd.isna(num):
        return
    if float(num) == 0:
        return
    num = num * 100000
    return int(str(abs(num))[0])


# drop columns with low variance (keeps PERCENT_TO_KEEP rows of data) and return dataframe
def drop_low_variance(df):
    df_variance = df.copy(deep=True)
    variance = df_variance.var(axis=1)
    df_variance['variance'] = variance
    df_variance.sort_values(by='variance', ascending=False, inplace=True)
    drop = int(len(df_variance) * PERCENT_TO_KEEP)
    drop = drop if drop > MIN_TO_KEEP else MIN_TO_KEEP
    dropped_df = df_variance.drop(df_variance.index[drop:])
    return dropped_df.drop(['variance'], axis=1)


# get specified digit for each column and makes a dictionary with key as col_name, and value a list of digits
# for the column
def get_column_digits(df):
    _digits = []  #
    _digit_dict = {}

    for column in df:
        nums = df[column]
        # last_digit = [first_after_decimal(num) for num in nums]
        digit = [first_digit(num) for num in nums]
        _digits += digit
        _digit_dict[column] = digit

    return _digits, _digit_dict

# get the percentage of each digit in each column and creates dataframe
def get_col_freqs(digits_dict):
    col_freq = pd.DataFrame(index=range(0, 10))
    for key in digits_dict.keys():
        frequencies = get_frequencies(digits_dict[key])
        frequencies['Percentage'] = frequencies['freq'] / sum(frequencies['freq']) * 100
        col_freq[key] = frequencies['Percentage']
        message = (f"{key}"
                   f"{frequencies}"
                   f"")
#         print(message)

    return col_freq

# get the correlation coefficients between all columns in dataset, returns as df and a list
def get_corr_coef(df):
    num_cols = len(df.columns)
    col_names = df.columns
    corr = pd.DataFrame(index=df.columns, columns=df.columns)
    corr_results = []
    for i in range(num_cols):
        for j in range(num_cols):
            if j <= i:
                continue
            else:
                coef = np.corrcoef(df[col_names[i]], df[col_names[j]])[0, 1]
                corr.iat[i, j] = coef
                corr_results.append(coef)
    return corr, corr_results

# Creates and saves a boxplot of digit frequencies by column
# def graph_frequencies(data_type, col_frequencies):
#     transposed = col_frequencies.transpose()[0:].copy()
#     plt.boxplot(transposed, sym="r.", medianprops=dict(color="black"))
#     plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
#     plt.ylabel("Frequency (percentage)")
#     plt.xlabel("Digit")
#     plt.title(f"Digit frequency of first number {data_type}")
#     plt.show()


# Creates and save a histogram of correlation coefficients between columns
def graph_correlation(data_type, top, corr_list):
    title = f"Correlation coefficients for {data_type} data"
    plt.hist(corr_list, 25, range=(0, 1))
    plt.ylim(top=top)
    plt.title(title)
    plt.xlabel("Correlation coefficient")
    plt.ylabel("Frequency")
    plt.savefig(f"Figures/Figure4_{data_type}")
    plt.show()

# Takes a dataset and analyzes it to determine correlation between columns, returns a list of correlation coefficients
def analyze_correlation(input_data, is_path, data_type="None", top=0, graph=True):
    if is_path:
        file = input_data
        data = pd.read_csv(file, na_values=['-', 'ND', 'Null', 'NA'], header=[0])
    else:
        data = input_data
    cleaned_data = data

    # use this if you want to drop low variance
    high_var_data = drop_low_variance(cleaned_data)

    digits, digit_dict = get_column_digits(high_var_data)

    column_frequencies = get_col_freqs(digit_dict)
    column_frequencies = column_frequencies.drop(0)

#     if graph:
#         graph_frequencies(data_type, column_frequencies)

    corr_df, correlations_list = get_corr_coef(column_frequencies)

    if graph:
        graph_correlation(data_type, top, correlations_list)

    return correlations_list



