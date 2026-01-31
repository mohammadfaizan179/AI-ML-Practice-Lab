import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def load_image_grayscale(path):
    """Load image and convert to grayscale."""
    img = Image.open(path).convert('L')  # 'L' mode for grayscale
    return np.array(img)


def save_image(matrix, path):
    """Save matrix as image."""
    img = Image.fromarray(np.clip(matrix, 0, 255).astype('uint8'))
    img.save(path)


def low_rank_approximation(A, k):
    """Compute rank-k approximation using SVD."""
    U, S, VT = np.linalg.svd(A, full_matrices=False)
    S_k = np.diag(S[:k])
    U_k = U[:, :k]
    VT_k = VT[:k, :]
    A_k = np.dot(U_k, np.dot(S_k, VT_k))
    return A_k


def main(image_path, k, output_path):
    original = load_image_grayscale(image_path)
    compressed = low_rank_approximation(original, k)

    # Save and show images
    save_image(compressed, output_path)

    # Display both
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(original, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(f"Low-Rank Approximation (k={k})")
    plt.imshow(compressed, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


# Example usage
if __name__ == "__main__":
    image_path = "../../images/cat.jpg"      # Path to your image
    output_path = "../../images/cat_compressed.jpg"
    k = 50  # rank to retain; smaller = more compression
    main(image_path, k, output_path)
