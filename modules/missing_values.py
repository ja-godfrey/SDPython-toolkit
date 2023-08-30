"""
Handling Missing Values Toolkit

This Python module provides a collection of utility functions to handle missing
values in a Pandas DataFrame. The aim is to make the imputation and removal of
missing values as simple and consistent as possible.

Functions:
    - impute_missing_numeric: Imputes missing values in a numeric column based on a specified strategy.
    - impute_missing_categorical: Imputes missing values in a categorical column based on a specified strategy.
    - drop_missing: Drops columns with missing values that exceed a given threshold.
    - drop_rows_with_missing: Drops rows with missing values in a specified column.
"""

import pandas as pd
import numpy as np

def impute_missing_numeric(data, column, strategy='mean'):
    """
    Impute missing values for a numeric column.

    Parameters:
        - data (pd.DataFrame): The data frame containing the column to be imputed.
        - column (str): The column name to be imputed.
        - strategy (str): The imputation strategy ('mean', 'median', 'mode', 'constant').

    Returns:
        pd.DataFrame: DataFrame with imputed values in the specified column.
    """
    if strategy == 'mean':
        impute_value = data[column].mean()
    elif strategy == 'median':
        impute_value = data[column].median()
    elif strategy == 'mode':
        impute_value = data[column].mode()[0]
    elif strategy == 'constant':
        impute_value = 0
    else:
        raise ValueError(f"Invalid strategy: {strategy}")
        
    data[column].fillna(impute_value, inplace=True)
    return data

def impute_missing_categorical(data, column, strategy='mode'):
    """
    Impute missing values for a categorical column.

    Parameters:
        - data (pd.DataFrame): The data frame containing the column to be imputed.
        - column (str): The column name to be imputed.
        - strategy (str): The imputation strategy ('mode', 'constant').

    Returns:
        pd.DataFrame: DataFrame with imputed values in the specified column.
    """
    if strategy == 'mode':
        impute_value = data[column].mode()[0]
    elif strategy == 'constant':
        impute_value = 'Unknown'
    else:
        raise ValueError(f"Invalid strategy: {strategy}")

    data[column].fillna(impute_value, inplace=True)
    return data

def drop_missing(data, threshold=0.7):
    """
    Drop columns with missing values exceeding the given threshold.

    Parameters:
        - data (pd.DataFrame): The data frame to be processed.
        - threshold (float): Missing value ratio threshold.

    Returns:
        pd.DataFrame: DataFrame with columns dropped based on missing value threshold.
    """
    missing_ratio = data.isnull().mean()
    drop_columns = missing_ratio[missing_ratio > threshold].index.tolist()
    data.drop(columns=drop_columns, inplace=True)
    return data

def drop_rows_with_missing(data, column):
    """
    Drop rows with missing values in the specified column.

    Parameters:
        - data (pd.DataFrame): The data frame to be processed.
        - column (str): The column name to check for missing values.

    Returns:
        pd.DataFrame: DataFrame with rows dropped based on missing values in the specified column.
    """
    data.dropna(subset=[column], inplace=True)
    return data

# Usage examples, please uncomment the following lines to test.
# df = pd.DataFrame({'col1': [1, 2, np.nan, 4, 5],
#                    'col2': ['a', 'b', 'c', np.nan, 'e'],
#                    'col3': [1.1, 2.2, 3.3, 4.4, np.nan]})
# print("Before:\n", df)
# print("After impute_missing_numeric:\n", impute_missing_numeric(df, 'col1', 'median'))
# print("After impute_missing_categorical:\n", impute_missing_categorical(df, 'col2', 'mode'))
# print("After drop_missing:\n", drop_missing(df))
# print("After drop_rows_with_missing:\n", drop_rows_with_missing(df, 'col3'))
