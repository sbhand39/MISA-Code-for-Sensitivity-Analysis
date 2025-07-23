# MISA code for sensitivity analysis
This repository contains the code used to perform the Moment Independent Sensitivity Analysis (MISA) presented in the paper:

"Circular economy for phosphorus from human urine to food systems generates water, climate and eutrophication benefits" 

Authors: Dilan P. Evans, Sarishma Bhandari, Dwarakanath Ravikumar, and Treavor H. Boyer

# Purpose
The Moment Independent Sensitivity Analysis (MISA) quantifies the contribution of uncertainty in the life cycle inventory data as MISA Delta Index. A higher MISA Delta Index value indicates that the given input is more sensitive to the total emissions for a given impact category (Global Warming, Eutrophication, etc).

# Repository Structure
- `MISA code.py`                                         → Main script for running MISA Delta Index
- `Beef Burger Patty_Sensitivity Analysis.xlsx`          → Contains mean and standard deviation for inputs used in Beef Burger Patty production using conventional and urine derived Phosphorous (P) fertilizer
- `Plant-based Burger Patty_Sensitivity Analysis.xlsx`   → Contains mean and standard deviation for inputs used in Plant-based Burger Patty production using conventional and urine-derived P fertilizer
- `Urine-derived P fertilizer_Sensitivity Analysis`      → Contains mean and standard deviation for inputs used in urine-derived P fertilizer
- `Result.xlsx`                                          → Results of MISA Delta Index for the production of four alternatives (Conventional Beef Burger Patty, Urine-derived Beef Burger Patty, Conventional Plant-based Burger Patty and Urine-derived Plant-based Burger Patty) and urine-derived P fertilizer. 
- `README.md`                                            → This file

# Required Python Packages
Follwing Packages are required to run the MISA code:
numpy
pandas
matplotlib
scipy

The python packages can be downloaded using the follwing commmands:
→ Spyder's Console: !pip install numpy pandas matplotlib scipy
→ Anaconda Prompt: conda install numpy pandas matplotlib scipy

# Real Space and Log space 
Real Space: This is the original distribution of the data. In environmental studies, such data is often assumed to follow a lognormal distribution, meaning its logarithm is normally distributed.

Log Space: Also referred to as the "underlying normal space," it is obtained by taking the natural logarithm of data points from real space. This transformation is used when the data is assumed to follow a lognormal distribution, so the log-transformed data becomes normally distributed.

The expected mean for the amount of an input (AM_m) is obtained from the literature. The geometric standard deviation (GSD) for this amount (AM_GSD) is derived using the Pedigree Matrix (refer the SI Table S1, S3, S6). These values, which are in real space, are converted to the mean and standard deviation in log space using Equations 1 and 2:

Equation 1: μ (mean) = ln(E(X)) − (1/2 × σ²)

Equation 2: σ (standard deviation) = ln(e^GSD)

The expected mean and standard deviation for a given input in a specific impact category (e.g., GHG_m and GHG_sd) are obtained from uncertainty analysis using SimaPro. A Monte Carlo simulation with 500 runs was conducted for each input across all four alternatives and the urine-derived P fertilizer process. These values, originally in real space, are converted to log space using Equations 3 and 4:

Equation 3: μ (mean) = ln((E(X))² / √((E(X))² + (SD(X))²))

Equation 4: σ (standard deviation) = √(ln(((E(X))² + (SD(X))²) / (E(X))²))

Note: For amounts, the conversion of GSD from real space to log space is different because GSD is not the same as an expected standard deviation. To convert GSD from real space to log space, take the natural logarithm of the GSD.

# How to Modify the Code to calculate MISA Delta Index:
Line 7: Specify the path to the input Excel file.
Line 8: Enter the relevant sheet name (e.g., BB_UD_GHG).
Line 19: Indicate the column name corresponding to the impact category being analyzed (e.g., GHG_m, GHG_sd).
Line 49: Define the path where the output file should be saved.
Line 53: Provide the desired name for the output file

# Contact
For questions, please contact:
Sarishma Bhandari
Arizona State University
Email: sbhand39@asu.edu
