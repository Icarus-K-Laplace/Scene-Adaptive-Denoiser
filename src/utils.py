import numpy as np
import cv2

def add_salt_pepper_noise(image, density=0.1, seed=None):
    """
    Add salt-and-pepper noise to an image.
    """
    if seed is not None:
        np.random.seed(seed)
    
    noisy = image.copy()
    h, w = image.shape
    n_noise = int(h * w * density)
    
    coords = np.random.permutation(h * w)[:n_noise]
    rows, cols = np.unravel_index(coords, (h, w))
    
    n_salt = n_noise // 2
    noisy[rows[:n_salt], cols[:n_salt]] = 255
    noisy[rows[n_salt:], cols[n_salt:]] = 0
    
    return noisy

def calculate_psnr(img1, img2):
    """
    Calculate Peak Signal-to-Noise Ratio (PSNR).
    """
    mse = np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2)
    if mse == 0:
        return float('inf')
    return 20 * np.log10(255.0 / np.sqrt(mse))

def read_image(path):
    """Read grayscale image."""
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")
    return img
