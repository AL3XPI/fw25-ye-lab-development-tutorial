# submissions/*/task1.py

"""
Copy this file to: submissions/<your-github-username>/task1.py
Then implement the functions. Do NOT import new modules, or change function names and signatures.
"""

def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    # TODO 1: Replace the placeholder below with your code.
    # HINT: Use sum() and len().

    if not values:
        raise ValueError("mean() arg is empty list")

    return sum(values) / len(values)

    #### End of TO-DO 1 ####

def moving_average(values, window):
    """
    Return a simple moving average list for the given window size.
    Example:
      values=[1,2,3,4], window=2 -> [1.5, 2.5, 3.5]
    """
    # TODO 2: Write your implementation here.
    # Remember: window must be positive and <= len(values).

    if window <= 0 or window > len(values):
        raise ValueError("window must be pos and <= to the num of elements in values")

    avg_list = []
    for n in range(len(values) - window + 1):
        slice = values[n : n + window]
        moving_avg = sum(slice) / window
        avg_list.append(moving_avg)

    return avg_list

    #### End of TO-DO 2 ####

def top_k(values, k):
    """
    Return the largest k values in descending order.
    Stable for ties relative to original order among equals.
    """
    # TODO 3: Write your implementation here.
    # TIP: Use sorted(..., reverse=True)

    if k < 0 or k > len(values):
        raise ValueError("k must be >= 0 and <= len(values)")

    sorted_vals = sorted(values, reverse = True)

    return sorted_vals[0:k]

    #### End of TO-DO 3 ####
