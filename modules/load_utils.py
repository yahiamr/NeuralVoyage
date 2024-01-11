# loading data utils
import pandas as pd
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

def load_csv(filename, missing_values=None, preprocess_funcs=None):
    """
    Load data from a CSV file with optional preprocessing.

    Args:
        filename (str): Path to the CSV file.
        missing_values (list, optional): List of values to be treated as missing. Defaults to None.
        preprocess_funcs (list of functions, optional): A list of functions to preprocess the data.

    Returns:
        DataFrame: Pandas DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(filename, na_values=missing_values)
        if preprocess_funcs:
            for func in preprocess_funcs:
                data = func(data)
        return data
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        return None

# Preprocessing functions
def drop_missing_values(df):
    """
    Preprocessing function to drop rows with missing values.

    Args:
        df (DataFrame): Pandas DataFrame to preprocess.

    Returns:
        DataFrame: DataFrame after dropping missing values.
    """
    return df.dropna()

def convert_to_datetime(df, column_name):
    """
    Convert a column to datetime.

    Args:
        df (DataFrame): Pandas DataFrame to preprocess.
        column_name (str): Name of the column to convert.

    Returns:
        DataFrame: DataFrame with the column converted to datetime.
    """
    df[column_name] = pd.to_datetime(df[column_name])
    return df

def normalize_column(df, column_name):
    """
    Normalize a column in the DataFrame.

    Args:
        df (DataFrame): Pandas DataFrame to preprocess.
        column_name (str): Name of the column to normalize.

    Returns:
        DataFrame: DataFrame with the column normalized.
    """
    df[column_name] = (df[column_name] - df[column_name].mean()) / df[column_name].std()
    return df

# Example usage
if __name__ == "__main__":
    preprocessing_steps = [drop_missing_values, lambda df: convert_to_datetime(df, 'date_column')]
    data = load_csv('path_to_file.csv', preprocess_funcs=preprocessing_steps)
    print(data.head())