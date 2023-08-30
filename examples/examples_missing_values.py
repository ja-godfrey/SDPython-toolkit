#%%
# Markdown Cell: # Importing Libraries

# First, let's import the necessary libraries.
#%%

import pandas as pd
import numpy as np

#%%
# Markdown Cell: # Define Functions for Handling Missing Values

# Below are the utility functions for handling missing values in a Pandas DataFrame. 
# These functions are designed to make the data cleaning process more streamlined.

# Let's go ahead and define them.

# Your functions here (from the previous Python file you created)

#%%
# Markdown Cell: # Load the Data

# For this demonstration, we will use the Titanic dataset. 
# This dataset has several missing values in columns like 'Age', 'Cabin', and 'Embarked' which makes it a good candidate.

titanic_data = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
titanic_data.head()

#%%
# Markdown Cell: # Initial Data Exploration

# Let's quickly explore the data to find out the number of missing values in each column.

missing_data = titanic_data.isnull().sum()
missing_data

#%%
# Markdown Cell: ## Impute Missing Numeric Values

# The `Age` column has missing values. We will use the `impute_missing_numeric()` function to fill these.

titanic_data = impute_missing_numeric(titanic_data, 'Age', strategy='median')
titanic_data.isnull().sum()

#%%
# Markdown Cell: ## Impute Missing Categorical Values

# The `Cabin` and `Embarked` columns have missing values. 
# For the purpose of this example, let's impute these using the `impute_missing_categorical()` function.

titanic_data = impute_missing_categorical(titanic_data, 'Cabin', strategy='constant')
titanic_data = impute_missing_categorical(titanic_data, 'Embarked', strategy='mode')
titanic_data.isnull().sum()

#%%
# Markdown Cell: ## Drop Columns with Excessive Missing Values

# Sometimes it's beneficial to remove columns that have an excessive number of missing values.
# Let's use `drop_missing()` function to drop such columns if they exist.

titanic_data = drop_missing(titanic_data, threshold=0.7)
titanic_data.isnull().sum()

#%%
# Markdown Cell: ## Drop Rows with Missing Values in Specific Columns

# For some critical columns, it might be best to completely remove the rows that contain missing values.
# We can achieve this using `drop_rows_with_missing()` function.

# Since we've already imputed all missing values, let's artificially introduce some missing values in the 'Fare' column for demonstration.

titanic_data.loc[1:10, 'Fare'] = np.nan
titanic_data.isnull().sum()

titanic_data = drop_rows_with_missing(titanic_data, 'Fare')
titanic_data.isnull().sum()

#%%
# Markdown Cell: # Summary

# As we can see, the utility functions make it very straightforward to handle missing values.
# We managed to impute or remove all missing values in the Titanic dataset effectively.
