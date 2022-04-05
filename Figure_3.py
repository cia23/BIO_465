import matplotlib.pyplot as plt
from Functions_for_Figure3_Supp1 import analyze_correlation

# all data files to be analyzed
all_files = ['Data/22329341.csv','Data/33242424_TableS1_DEG(Phospho).csv',
         'Data/33242952_TableS1_Dataset2_Parkin_colony.csv','Data/29635916_S2_MaxQuant_log2.csv',
         'Data/32242669_protein_water_normalized.csv','Data/34515489.csv','Data/28217993_DataS12_normalized.csv',
         'Data/35091530_TableS6.csv','Data/33749263.csv','Data/32242669_peptide_water_normalized.csv',
         'Data/29121770_Supple.Table2.csv','Data/30371095.csv','Data/34677046.csv','Data/32378902_TableS3.csv',
         'Data/30371095_UnnamedTable_MTS_N-termini_identified.csv','Data/30394099_30K_35%.csv',
         'Data/33175545_TableS3.csv','Data/34783559_B.csv','Data/29195270_S-7.csv','Data/35091530_TableS5.csv',
         'Data/34742921.csv','Data/29195270_S-3.csv','Data/32108472_LiCl_sucrose_ProteinGroup.csv','Data/33594990.csv',
         'Data/32108472_LiCl_sucrose_peptide_output.csv','Data/30394099_30K_100%.csv',
         'Data/32108472_Trypsin_shaving_peptide_output.csv','Data/24712744_S2_Sheet1.csv','Data/34780180_S2.csv',
         'Data/30371095_TableS5_STS_dependent_termini.csv','Data/29972301_S6_Protein_Intensities.csv',
         'Data/26151086_TableS1_All_Quantified_Protein.csv','Data/27535590_TableS-2.csv','Data/32878984_raw.csv',
         'Data/24712744_S5_replicate2.csv','Data/32181667_TableS1.csv','Data/34783559.csv',
         'Data/32975419_Table_S21.csv','Data/28102081_Table_S1.csv','Data/33242424_TableS1_DEG(protein).csv',
         'Data/24712744_S4_replicate3.csv','Data/29718670_S12.csv','Data/35166117_TableS1_imputed.csv',
         'Data/29718670_S10.csv','Data/32242669_protein_PMSI_raw.csv','Data/27794609_single_digestion.csv',
         'Data/24677030.csv','Data/32242669_protein_PMSI_normalized.csv','Data/29718670_S8.csv',
         'Data/33337894_TableS3.csv','Data/32975419_Table_S17.csv',
         'Data/30371095_TableS3_Proteolysis_in_mitochondrial_pt.csv','Data/30213844.csv',
         'Data/29634277_S2_intensity.csv','Data/34806897.csv','Data/23672200.csv','Data/35166117_TableS7.csv',
         'Data/32242669_peptide_PMSI_normalized.csv','Data/33054241.csv','Data/32338516_TableS2_Sheet1.csv',
         'Data/26080680_table4.csv','Data/32975419_Table_S18.csv','Data/31682457_TableS3a.csv',
         'Data/32181667_TableS2.csv','Data/31131048.csv','Data/33508502.csv','Data/33453410.csv',
         'Data/24712744_S5_replicate1.csv','Data/35091530_TableS4.csv','Data/32108472_Trypsin_shaving_ProteinGroup.csv',
         'Data/30767541_S3_Metaproteomics_cecum_content.csv','Data/29718670_S14.csv','Data/25728785_N-end_rule_TMT.csv',
         'Data/34673282.csv','Data/31859514_S1.csv','Data/35091530_TableS2.csv','Data/24712744_S5_replicate3.csv',
         'Data/32543193_TableS3.csv','Data/30767541_S3_Metaproteomics_colon_content.csv',
         'Data/26080680_table6_sheet2.csv','Data/29250956_Table_S2.csv','Data/30394099_60K_25%.csv',
         'Data/35091530_TableS3.csv','Data/32519869_TableS1_Whole_Tissue_Proteome_Matrix.csv',
         'Data/35166117_TableS5_raw.csv','Data/28217993_DataS12_raw.csv','Data/29718670_S9.csv',
         'Data/29250956_Table_S1.csv','Data/29634277_S2_LFQ.csv','Data/35089061.csv','Data/35085786_Proteins.csv',
         'Data/32878984_normalized.csv','Data/32975419_Table_S19.csv','Data/34647699.csv','Data/32975419_Table_S16.csv',
         'Data/27794609_double_digestion.csv','Data/32108472_ECF_peptide_output.csv',
         'Data/30371095_TableS4_BAM7_dependent_termini.csv','Data/33175545_TableS2.csv','Data/30239205.csv',
         'Data/29718670_S7.csv','Data/30394099_30K_75%.csv','Data/32242669_protein_water_raw.csv',
         'Data/30371095_TableS2_TAILSMT_BAM7vsSTSvsDMSO.csv','Data/30767541_S3_Metaproteomics_colon_mucus.csv',
         'Data/30814501.csv','Data/34874173_Table_S3.csv','Data/32108472_ECF_ProteinGroup.csv',
         'Data/35166117_TableS1_raw.csv','Data/32242669_peptide_water_raw.csv','Data/27025989_S1_raw.csv',
         'Data/35166117_TableS3_raw.csv','Data/34874173_Table_S1.csv','Data/33515806_Table3.csv',
         'Data/29718670_S11.csv','Data/30394099_30K_25%.csv','Data/35166117_TableS3_imputed.csv',
         'Data/35166117_TableS5_imputed.csv','Data/35093608_Table_S5.csv','Data/24712744_S4_replicate2.csv',
         'Data/26080680_table2.csv','Data/30394099_30K_50%.csv','Data/29367434.csv','Data/34780180_S1.csv',
         'Data/26080680_table6_sheet1.csv','Data/26080680_table7.csv','Data/24712744_S4_replicate1.csv',
         'Data/29195270_S-9.csv','Data/32242669_peptide_PMSI_raw.csv','Data/33515806_Table4.csv',
         'Data/29195270_S-1.csv','Data/30371095_TableS1_TAILSMT_data.csv','Data/33242424_TableS1_DEG(RNA).csv',
         'Data/29250956_Table_S4.csv','Data/29196338.csv','Data/34855411_Proteins.csv','Data/32975419_Table_S20.csv',
         'Data/31682457_TableS4a.csv','Data/34919406.csv']

all_corr_coef = []

# obtains correlation values for each file and adds to all_corr_coef, an aggregated list
for file in all_files:
    correlations = analyze_correlation(file, True, "None", 0, graph=False)
    all_corr_coef += correlations

# sort, plot, and save plot of aggregated correlation coefficients
all_corr_coef.sort()
plt.hist(all_corr_coef, 50)
plt.title("Aggregated column-column correlation coefficients across all datasets")
plt.xlabel("Correlation coefficient")
plt.ylabel("Frequency")
plt.savefig("Figure_3")
plt.show()

