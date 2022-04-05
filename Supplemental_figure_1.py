from Functions_for_Figure3_Supp1 import *

file_name = "Data/34647699.csv"
plot_top = 80 # ensures all the graphs are scaled the same
data = pd.read_csv(file_name, na_values=['-', 'ND'], header=[0])

# generate the fake data columns
random_data = generate_random(deepcopy(data))
resampled_data = generate_resampled(deepcopy(data))
imputed_mean_data = generate_imputed_mean(deepcopy(data))
imputed_median_data = generate_imputed_median(deepcopy(data))

# analyze correlation coefficients and generate graphs for each data set
analyze_correlation(data, False, "real", plot_top, graph=True)
analyze_correlation(random_data, False, "random", plot_top, graph=True)
analyze_correlation(resampled_data, False, "resampled", plot_top, graph=True)
analyze_correlation(imputed_mean_data, False,  "imputed mean", plot_top, graph=True)
analyze_correlation(imputed_median_data, False, "imputed median", plot_top, graph=True)
