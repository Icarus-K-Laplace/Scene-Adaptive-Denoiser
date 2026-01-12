import numpy as np
import cv2

class SceneAdaptiveUnifiedDenoiser:
    """
    Final Unified Target-Aware Impulse Denoiser
    ----------------------------------------------------
    Integrated components:
    1. Thermal Saliency: Protects hot targets.
    2. Structure Consistency: Preserves real edges.
    3. Scene-Adaptive Control: Adjusts global aggressiveness.
    4. Soft Restoration: Continuous blending instead of hard switching.
    ----------------------------------------------------
    No learning, single-pass, O(N) complexity.
    """

    def __init__(self, window_size=7, tau1=2.0, tau2=3.0, scene_percentile=98, eps=1e-6):
        self.w = window_size
        self.tau1 = tau1
        self.tau2 = tau2
        self.scene_percentile = scene_percentile
        self.eps = eps

    def thermal_saliency(self, img):
        """
        Compute thermal saliency map.
        Combines global intensity rarity (Z-score) and local gradient strength.
        High values indicate potential thermal targets.
        """
        mu = img.mean()
        sigma = img.std() + self.eps

        # Global intensity rarity (Sigmoid of Z-score)
        z = (img - mu) / sigma
        z = 1.0 / (1.0 + np.exp(-z)) 

        # Local gradient strength
        gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
        gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
        grad = np.sqrt(gx * gx + gy * gy)
        grad = grad / (grad.max() + self.eps)

        return z * grad

    def impulse_likelihood(self, img):
        """
        Estimate local likelihood of impulse noise.
        Based on deviation from local mean normalized by local std.
        """
        mean = cv2.blur(img, (self.w, self.w))
        var = cv2.blur((img - mean) ** 2, (self.w, self.w))
        std = np.sqrt(var + self.eps)
        return np.abs(img - mean) / (std + self.eps)

    def structure_consistency(self, img):
        """
        Measure local geometric consistency.
        Real edges have consistent gradient orientation; noise is random.
        """
        gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
        theta = np.arctan2(gy, gx)

        # Variance of local orientation
        mean_theta = cv2.blur(theta, (3, 3))
        var_theta = cv2.blur((theta - mean_theta) ** 2, (3, 3))

        # Consistent structure -> low variance -> high weight
        return np.exp(-var_theta)

    def confidence(self, D):
        """Map noise score to [0, 1] confidence."""
        return 1.0 / (1.0 + np.exp(-(D - self.tau1) / (self.tau2 - self.tau1 + self.eps)))

    def scene_control(self, img):
        """
        Global scene-adaptive control parameter (Gamma).
        Analyzes dynamic range to determine how aggressive the filter should be.
        """
        high_val = np.percentile(img, self.scene_percentile)
        ratio = high_val / (img.mean() + self.eps)

        # Map ratio to (0.6, 1.0)
        gamma = 1.0 / (1.0 + np.exp(ratio - 2.5))
        gamma = 0.6 + 0.4 * gamma
        return gamma

    def denoise(self, noisy):
        """Main denoising pipeline."""
        # Normalize input
        if noisy.dtype == np.uint8:
            img = noisy.astype(np.float32) / 255.0
        else:
            img = noisy.astype(np.float32)

        # 1. Compute components
        saliency = self. = likelihood * (1.0 - saliency)
        C = self.confidence(noise_score)

        # 4. Global scene modulation
        gamma = self.scene_control(img)

        # 5. Final alpha map (Restoration strength)
        alpha = gamma * C * (1.0 - protected)
        alpha = np.clip(alpha, 0.0, 1.0)

        # 6. Candidate restoration (Median)
        median_img = cv2.medianBlur((img * 255).astype(np.uint8), 3)
        median        return (out * 255).astype(np.uint8)
