# Data Cleaning and Preprocessing Toolkit Functions

This toolkit provides a set of custom Python functions to simplify and standardize various data cleaning and preprocessing tasks. These functions serve as a more specialized interface for common tasks and are designed to complement libraries like Pandas, Scikit-learn, and NLTK.

## Table of Contents

1. [Handling Missing Values](#handling-missing-values)
2. [Outlier Detection & Handling](#outlier-detection--handling)
3. [Feature Engineering](#feature-engineering)
4. [Text Cleaning](#text-cleaning)
5. [Data Integrity Checks](#data-integrity-checks)
6. [Handling Imbalance](#handling-imbalance)

---

### Handling Missing Values

- `impute_missing_numeric(data, column, strategy='mean')`: Customized imputation strategies for numeric columns.
- `drop_missing(data, threshold=0.7)`: Drops columns with missing values above a certain threshold.

### Outlier Detection & Handling

- `z_score_outliers(data, column, threshold=3)`: Detect outliers based on z-scores.
- `iqr_outliers(data, column)`: Detect outliers based on the interquartile range.
- `handle_outliers(data, column, method='cap', strategy='mean')`: Handle outliers with various custom methods.

### Feature Engineering

- `bin_numeric(data, column, bins)`: Binning of numeric data into custom intervals.
- `log_transform(data, column)`: Log transformation for skewed data.
- `date_parts(data, column)`: Extracts parts from a date column.

### Text Cleaning

- `remove_punctuation(text)`: Remove punctuation from a text column.
- `remove_stopwords(text, language='english')`: Stopwords removal based on language.
- `stem_text(text)`: Text stemming.
- `lemmatize_text(text)`: Text lemmatization.

### Data Integrity Checks

- `check_unique(data, column)`: Report unique values and their frequencies.
- `check_duplicated(data)`: A detailed report on duplicated rows.

### Handling Imbalance

- `upsample_minority(data, target_column)`: Up-sample the minority class in imbalanced datasets.
- `downsample_majority(data, target_column)`: Down-sample the majority class in imbalanced datasets.

