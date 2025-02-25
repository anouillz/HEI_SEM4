import numpy as np
import pandas as pd


def compute_conditional_entropy(csv_file, given_class):
    """
    Compute the conditional entropy H(R | C = given_class).
    :param csv_file: Path to the CSV file containing the data.
    :param given_class: The specific class C for which we compute H(R | C).
    :return: The conditional entropy H(R | C) in bits.
    """
    # Load data
    df = pd.read_csv(csv_file, index_col=0)

    # Ensure the given class exists in the dataset
    if given_class not in df.index:
        raise ValueError(f"Class '{given_class}' not found in the dataset.")

    # Extract row for the given class
    class_distribution = df.loc[given_class]

    # Compute total number of individuals in the given class
    total_given_class = class_distribution.sum()

    # Avoid division by zero
    if total_given_class == 0:
        raise ValueError(f"No individuals found for class '{given_class}'.")

    # Compute P(r | C)
    prob_r_given_c = class_distribution / total_given_class

    # Compute H(R | C)
    conditional_entropy = -np.nansum(prob_r_given_c * np.log2(prob_r_given_c.where(prob_r_given_c > 0)))

    print(f"Conditional Entropy H(R | C={given_class}): {conditional_entropy:.4f} bits")


# Example usage
# Replace "lab02-class-race-table.csv" with your actual CSV file
compute_conditional_entropy("data/lab01-classe-race-tableau.csv", "Guerrier·e")
