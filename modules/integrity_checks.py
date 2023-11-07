import pandas as pd

def print_column_type_distributions(df):
    """
    Prints the distribution of data types for each column in the given DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame for which to print type distributions.
    """

    # Function to get the type distribution in a column
    def get_type_distribution(column):
        # Count occurrences of each type
        type_counts = column.apply(lambda x: type(x)).value_counts()
        
        # Calculate the percentage distribution
        type_distribution = (type_counts / len(column)) * 100

        return type_distribution

    # Iterate over each column and print type distribution
    for col in df.columns:
        distribution = get_type_distribution(df[col])
        print(f"Column '{col}' has the following type distribution:\n{distribution}\n")

# Example usage
# print_column_type_distributions(your_dataframe)
