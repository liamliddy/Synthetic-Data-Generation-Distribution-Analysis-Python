# Synthetic-Data-Generation-Distribution-Analysis-Python
🧪Synthetic Data Generation & Analysis (python)
Developed a Python program to automate the creation of synthetic datasets from real CSV files.
This project demonstrates Python skills in data validation, analysis, and synthetic data generation.

The program allows users to:

Load and inspect datasets from CSV files

Validate data (handle missing rows, detect headers, log errors)

Analyze distributions of categorical and numeric values

Generate synthetic data based on original distributions

Compare synthetic data to the original dataset using margin-of-error analysis

📌 Features

Data Loading & Validation

Select input files from a folder (0_input)

Detect and handle missing or empty rows

Ask users if the first row is a header

Log errors to errors_on_input.csv

Data Exploration

Display the first 50 rows of data

Count unique values per column: brand, weight, counts, price

Summarize large datasets

Synthetic Data Generation

Generate user-specified number of synthetic rows

Sample values for each column based on original dataset distributions

Distribution Comparison

Evaluate how closely synthetic data matches original data

Calculate differences in percentages and check against a user-defined margin of error

🛠 Technical Highlights

Python Libraries: csv, os, random

Techniques:

File I/O & CSV handling

Input validation & error handling

Random sampling for synthetic data

Distribution analysis & margin-of-error computation

Key Accomplishments:

Automated synthetic dataset creation while preserving statistical characteristics

Built robust validation mechanisms to ensure data integrity

Quantified similarity between synthetic and original datasets
