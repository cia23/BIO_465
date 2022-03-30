# Digit Frequencies BIO 465
## Introduction
This project builds off a paper from Bradshaw and Payne analyzing digit frequencies in biological data to detect fraud (https://dx.doi.org/10.1371%2Fjournal.pone.0260395). 
This paper analyzes 140 proteomic datasets from 67 academic, peer-reviewed papers to discover patterns in digit frequencies. We found that the first digit of a number 
follows a pattern similar to that of the Newcomb-Benford law. When comparing columns within a single dataset, it was found that there is little variability in the digit 
frequencies between columns. (To see a full draft of the manuscript, visit https://docs.google.com/document/d/1L5loCc_JwXfoHBkXb_mrY3Z7GwjbNahswjlfWn1POYM/edit?usp=sharing)
## Technologies and Setup
Project is created using:
* Python version 3.9

To run this project, download and import the following packages:
*   pandas
*   numpy
*   matplotlib

## Running the Data
To run the scripts, download all the data in this GitHub repository. If the data is in the same directory as the scripts, you will be able to run the scripts and generate
results. Other numeric datasets can be used if put in the Data folder. Input the name and path to the dataset of interest in the all_files variable and run the script.
