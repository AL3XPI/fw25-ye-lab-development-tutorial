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
    
    pass

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

    pass

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

    pass


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

    pass


    #### End of TO-DO 7 ####
