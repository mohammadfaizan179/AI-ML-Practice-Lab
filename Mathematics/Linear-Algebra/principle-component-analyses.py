# Principal Component Analysis using NumPy
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the original data matrix (Students' data)
X = np.array([
    [6, 7, 80],   # Student A
    [8, 6, 90],   # Student B
    [5, 8, 75],   # Student C
    [10, 5, 95]   # Student D
])

# Step 2: Standardize the data (zero mean)
X_mean = np.mean(X, axis=0)
X_std = X - X_mean

# Step 3: Compute the covariance matrix
cov_matrix = np.cov(X_std.T)

# Step 4: Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 5: Sort the eigenvectors by descending eigenvalues
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Step 6: Select top 2 eigenvectors (principal components)
W = eigenvectors[:, :2]  # Projection matrix (3x2)

# Step 7: Transform the data to the new space
Z = X_std @ W  # Projected data (4x2)

# Step 8: Plot the projected data
plt.figure(figsize=(8, 6))
plt.scatter(Z[:, 0], Z[:, 1], color='blue', marker='o')

# Annotate points with student labels
labels = ['A', 'B', 'C', 'D']
for i, label in enumerate(labels):
    plt.text(Z[i, 0] + 0.3, Z[i, 1], label, fontsize=12)

plt.title("PCA: Projection onto First 2 Principal Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid(True)
plt.tight_layout()
plt.show()

# Print projected data
print("Projected Data (Principal Components):")
for i, row in enumerate(Z):
    print(f"Student {labels[i]}: PC1 = {row[0]:.3f}, PC2 = {row[1]:.3f}")
