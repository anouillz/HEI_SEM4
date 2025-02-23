import numpy as np
import pandas as pd


def compute_joint_entropy(joint_prob_matrix):
    # compute joint entropy
    # no 0 values so no error with log_2
    p = joint_prob_matrix[joint_prob_matrix > 0]
    return -np.sum(p * np.log2(p))


filename = "data/lab01-classe-race-tableau.csv"

try:
    # first col contains class name
    df = pd.read_csv(filename, index_col=0)
    print("Tableau:")
    print(df)

    # Convert into probabilities
    counts = df.values.astype(float)
    total = counts.sum()
    joint_prob = counts / total

    # compute joint entropy
    entropy_joint = compute_joint_entropy(joint_prob)
    print(f"\nEntropie jointe H(C,R) : {entropy_joint:.4f} bits")

except FileNotFoundError:
    print(f"Fichier '{filename}' non trouvé. Utilisation d'un exemple de matrice uniforme.")

    num_races = 7
    num_classes = 11
    joint_prob_uniform = np.full((num_classes, num_races), 1 / (num_classes * num_races))
    entropy_joint_uniform = compute_joint_entropy(joint_prob_uniform)
    print(f"Entropie jointe pour une distribution uniforme : {entropy_joint_uniform:.4f} bits")
