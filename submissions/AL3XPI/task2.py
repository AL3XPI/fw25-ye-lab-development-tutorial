# submissions/<username>/task2.py

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load a CSV and return a pandas DataFrame.
    Requirements:
    - Must read the file at `path` using pandas.
    - Ensure the 'healthy' column is boolean dtype.
    """
    # TODO 4: Replace with your implementation
    
    df = pd.read_csv(path)

    if 'healthy' in df.columns:
        df['healthy'] = df['healthy'].astype(bool)
    else:
        raise ValueError("'healthy' column is not boolean dtype")

    return df

    #### End of TO-DO 4 ####


def count_by_species(df: pd.DataFrame) -> pd.Series:
    """
    Return counts per species.
    Requirements:
    - Index: species
    - Values: integer counts
    - Sort primarily by count (descending); ties handled consistently.
    """
    # TODO 5: Write your code here.

    return df['species'].value_counts()

    #### End of TO-DO 5 ####


def average_weight_by_species(df: pd.DataFrame) -> pd.Series:
    """
    Return mean weight (kg) per species.
    Requirements:
    - Index: species
    - Values: float means
    - Sort descending by mean weight.
    """
    # TODO 6: Write your code here.

    avg_weight = df.groupby('species')['weight_kg'].mean()
    avg_weight = avg_weight.sort_values(ascending=False)
    
    return avg_weight


    #### End of TO-DO 6 ####


def heaviest_n(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """
    Return the top-n heaviest rows by 'weight_kg'.
    Requirements:
    - If n < 0, raise ValueError
    - Sort descending by weight_kg, tie-break by id ascending
    - Return DataFrame with reset index
    """
    # TODO 7: Write your code here.

    if n < 0:
        raise ValueError("n must be >= 0")

    sorted_df = df.sort_values(by=['weight_kg', 'id'], ascending=[False, True])
    heaviest_n_df = sorted_df.head(n).reset_index(drop=True)

    return heaviest_n_df


    #### End of TO-DO 7 ####
