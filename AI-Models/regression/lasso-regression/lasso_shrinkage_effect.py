# Visual example of coefficient paths
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import lasso_path

# Generate sample data
np.random.seed(42)
X = np.random.randn(100, 5)
y = 2*X[:, 0] + 0.5*X[:, 1] + np.random.randn(100)*0.1

# Compute Lasso path
alphas, coefs, _ = lasso_path(X, y, alphas=np.logspace(-2, 2, 100))

# Plot coefficient paths
plt.figure(figsize=(10, 6))
for coef in coefs:
    plt.semilogx(alphas, coef)
plt.xlabel('Lambda (α)')
plt.ylabel('Coefficients')
plt.title('LASSO Coefficient Paths')
plt.grid(True)
plt.show()