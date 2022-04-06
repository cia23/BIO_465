# Digit Frequencies BIO 465
## Introduction
This project builds off a paper from Bradshaw and Payne analyzing digit frequencies in biological data to detect fraud (https://dx.doi.org/10.1371%2Fjournal.pone.0260395). 
This paper analyzes 139 proteomic datasets from 66 academic, peer-reviewed papers to discover patterns in digit frequencies. We found that the first digit of a number 
follows a pattern similar to that of the Newcomb-Benford law. When comparing columns within a single dataset, it was found that there is little variability in the digit 
frequencies between columns. (To see a full draft of the manuscript, visit https://docs.google.com/document/d/1L5loCc_JwXfoHBkXb_mrY3Z7GwjbNahswjlfWn1POYM/edit?usp=sharing)
## Technologies and Setup
Project is created using:
* Python version 3.9

To run this project, download and import the following packages:
*   pandas
*   numpy
*   matplotlib
*   seaborn
*   random
*   copy

## Running the Data
To run the scripts, download all the data in this GitHub repository. The data used to generate figures is stored in the Data folder. To analyze other datasets, input the filepath into the desired script where files are read in for that script. All figures generated in the scripts will be saved to a folder labeled 'Figures'.

### Figure 1
Figure 1 can be created using the Make_Figure1 file. This figure analyzes and plots digit frequencies for all the files in the study. It will take 1-2 minutes to run and will output a boxplot.

### Figure 2
Figure 2 can be created using the Make_Figure2 file. This figure analyzes and plots the digit frequencies from a paper known to have fraudulent data. It will take <30 seconds to run and will output a scatter plot.

### Figure 3
Figure 3 can be created using the Make_Figure3 file. This figure analyzes and plots the correlations between the columns of all files. It will take 1-2 minutes to run and will output a histogram of correlation data. Figure 3 uses functions in the Helper_Functions file. 

### Figure 4
Figure 4 can be created using the Make_Figure4 file. This figure analyzes different ways data can be fabricated and plots the correlations between the columns of real and fake data. This is only done for 1 dataset, but can be done for any dataset in the Data folder. It will take <30 seconds to run and will output 5 histograms of correlation data. Figure 4 uses functions in the Helper_Functions and Create_Fake_Data files.
