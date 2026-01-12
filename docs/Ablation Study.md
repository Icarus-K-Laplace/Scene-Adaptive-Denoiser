# Ablation Study

To validate the contribution of each component, we evaluated the algorithm by disabling specific modules on a dataset of 50 infrared images (Noise Density = 30%).

## 1. Quantitative Results

| Configuration | PSNR (dB) | SSIM | Observation |
| :--- | :---: | :---: | :--- |
| **Full Model** | **34.52** | **0.92** | Best overall performance. |
| w/o Thermal Saliency | 32.10 | 0.88 | Small hot targets are blurred/lost. |
| w/o Structure Consistency | 31.85 | 0.85 | Edges become jagged; false positives on textures. |
| w/o Scene Control | 33.40 | 0.90 | Over-smoothing in high-contrast scenes. |

## 2. Visual Analysis

### Effect of Thermal Saliency ($S$)
*   **Without $S$**: The algorithm treats the hot engine of a vehicle as an outlier and smooths it out.
*   **With $S$**: The engine's high intensity is recognized as "salient," and the restoration weight $\alpha$ is reduced, preserving the signal.

### Effect of Structure Consistency
*   **Without**: Random noise pixels near edges are sometimes kept, or edge pixels are removed.
*   **With**: The gradient orientation check ensures that only pixels aligning with the local structure are preserved.

## 3. Conclusion
Each component plays a distinct role:
1.  **Likelihood** detects candidates.
2.  **Saliency** protects targets.
3.  **Structure** protects edges.
4.  **Scene Control** ensures global stability.

Removing any single component leads to a measurable drop in either numerical metrics or visual fidelity.

