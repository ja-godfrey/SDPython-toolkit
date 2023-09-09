# Importing Libraries
import pandas as pd
import numpy as np
import sys

sys.path.append("../")
from modules.missing_values import impute_missing_numeric, impute_missing_categorical, drop_missing, drop_rows_with_missing

# Load the Titanic dataset
titanic_data = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")

# Introduce missing values for demonstration purposes
np.random.seed(42) # For reproducibility
mask = np.random.rand(len(titanic_data)) < 0.3 # Randomly select 30% of the data
titanic_data.loc[mask, 'Age'] = np.nan
titanic_data.loc[mask, 'Fare'] = np.nan
titanic_data.loc[mask, 'Pclass'] = np.nan

# Initial Data Exploration
print("Initial missing values count:")
print(titanic_data.isnull().sum())
print("\n" + "-"*50 + "\n")

# Impute Missing Numeric Values
titanic_data = impute_missing_numeric(titanic_data, 'Age', strategy='median')
print("'Age' column missing values count post imputation:", titanic_data['Age'].isnull().sum())

# If 'Pclass' was missing values (it's not in this example, but for completeness sake)
if 'Pclass' in titanic_data.columns:
    titanic_data = impute_missing_categorical(titanic_data, 'Pclass', strategy='mode')
    print("'Pclass' column missing values count post imputation:", titanic_data['Pclass'].isnull().sum())

print("\n" + "-"*50 + "\n")

# Drop Columns with Excessive Missing Values
titanic_data = drop_missing(titanic_data, threshold=0.7)
print("Missing values count post dropping excessive columns:")
print(titanic_data.isnull().sum())
print("\n" + "-"*50 + "\n")

# Drop Rows with Missing Values in Specific Columns
print("'Fare' column missing values count:", titanic_data['Fare'].isnull().sum())
titanic_data = drop_rows_with_missing(titanic_data, 'Fare')
print("'Fare' column missing values count post row drop:", titanic_data['Fare'].isnull().sum())
print("\n" + "-"*50 + "\n")

# Summary
print("Final missing values count:")
print(titanic_data.isnull().sum())


# %%
