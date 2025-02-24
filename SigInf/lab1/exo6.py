import pandas as pd
import numpy as np


def exo1_compute_probabilities(csv_file):
    # Load data from the CSV file
    df = pd.read_csv(csv_file, index_col=0)

    # Compute the total number of adventurers
    total_adventurers = df.to_numpy().sum()

    # Probability of being a Bard
    p_bard = df.loc["Barde"].sum() / total_adventurers

    # Probability of being a Half-elf
    p_half_elf = df["Demi-elfe"].sum() / total_adventurers

    # Probability of being a Monk and a Half-orc
    p_monk_half_orc = df.loc["Moine", "Demi-orque"] / total_adventurers

    # Display results
    probabilities = pd.DataFrame({
        "Event": ["Being a Bard", "Being a Half-elf", "Being both a Monk and a Half-orc"],
        "Probability": [p_bard, p_half_elf, p_monk_half_orc],
        "Percentage": [p_bard * 100, p_half_elf * 100, p_monk_half_orc * 100]
    })

    print(probabilities)


def exo2_compute_joint_entropy(csv_file):
    # Load data from the CSV file
    df = pd.read_csv(csv_file, index_col=0)

    # Compute the total number of adventurers
    total_adventurers = df.to_numpy().sum()

    # Compute joint probabilities P(c, r)
    joint_probabilities = df / total_adventurers

    # Compute joint entropy H(C, R)
    joint_entropy = -np.nansum(joint_probabilities * np.log2(joint_probabilities))

    print(f"Joint Entropy H(C, R): {joint_entropy:.4f} bits")


def exo4_compute_joint_entropy(prob_matrix):
    """
    Compute the joint entropy of two random variables given their joint probability matrix.
    :param prob_matrix: A 2D NumPy array or Pandas DataFrame representing the joint probability distribution.
    :return: The joint entropy H(X, Y) in bits.
    """
    # Convert to NumPy array if input is a Pandas DataFrame
    prob_matrix = np.array(prob_matrix)

    # Compute joint entropy
    joint_entropy = -np.nansum(prob_matrix * np.log2(prob_matrix, where=prob_matrix > 0))

    print(f"Joint Entropy: {joint_entropy:.4f} bits")

    #return joint_entropy

example_matrix = np.array([
    [0.1, 0.15, 0.05],
    [0.2, 0.1, 0.1],
    [0.1, 0.05, 0.15]
])



# Test the functions
#exo1_compute_probabilities("data/lab01-classe-race-tableau.csv")
#exo2_compute_joint_entropy("data/lab01-classe-race-tableau.csv")
exo4_compute_joint_entropy(example_matrix)
