# -*- coding: utf-8 -*-
"""Topsis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10xSk4UzSFraLVYN5mPOGvM7Q05FByxk_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load data
data = pd.read_csv('data.csv', index_col='Model')

# Normalize the data
normalized_data = data.div(np.sqrt((data**2).sum(axis=0)), axis=1)

# Define weights for each criterion
weights = {'Accuracy': 0.4, 'Speed': 0.3, 'Versatility': 0.3}

# Multiply normalized data by weights
weighted_normalized_data = normalized_data * np.array(list(weights.values()))

# Define positive and negative ideal solutions
positive_ideal = weighted_normalized_data.max()
negative_ideal = weighted_normalized_data.min()

# Calculate the distance to positive and negative ideal solutions
positive_distance = np.sqrt(((weighted_normalized_data - positive_ideal)**2).sum(axis=1))
negative_distance = np.sqrt(((weighted_normalized_data - negative_ideal)**2).sum(axis=1))

# Calculate the closeness to the ideal solution
closeness = negative_distance / (positive_distance + negative_distance)

# Add the closeness score to the original data
data['Topsis Score'] = closeness

# Rank models based on Topsis Score
data['Rank'] = data['Topsis Score'].rank(ascending=False)

# Save results to result.csv
result = data[['Topsis Score', 'Rank']].sort_values(by='Rank')
result.to_csv('result.csv')

# Plotting
plt.figure(figsize=(10, 6))
result['Topsis Score'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Topsis Score for Text Sentence Similarity Models')
plt.xlabel('Model')
plt.ylabel('Topsis Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot to a file
plt.savefig('topsis_score_plot.png')

# Display the plot
plt.show()