# Theoretical Formulation: Scene-Adaptive Denoising

## 1. The Core Conflict
In infrared image restoration, we face a fundamental conflict:
*   **Noise Removal** requires smoothing high-frequency components (outliers).
*   **Target Preservation** requires keeping high-frequency components (edges, hot spots).

Standard filters use a hard threshold: `if pixel_diff > T then smooth`. This binary decision often misclassifies small, hot targets as noise, leading to signal loss.

## 2. Our Solution: Soft Probabilistic Fusion
Instead of a hard switch, we propose a soft fusion formulation:
$$ \hat{I} = (1 - \alpha) I_{obs} + \alpha I_{restored} $$

Here, $\alpha \in [0, 1]$ represents the **probability of being noise**.

## 3. Deriving Alpha ($\alpha$)
We model $\alpha$ as a joint probability conditioned on local and global cues:
$$ \alpha \approx P(\text{Noise} | \text{Local}, \text{Global}) $$

This is decomposed into three factors:

### A. Local Impulse Likelihood ($L$)
Measures how much a pixel deviates from its neighborhood statistics.
$$ L(x) = \frac{|I(x) - \mu_{local}|}{\sigma_{local} + \epsilon} $$
High $L$ suggests a potential outlier.

### B. Thermal Saliency Prior ($S$)
In thermal images, targets are often rare (high Z-score) and have structure (high gradient).
$$ S(x) = \text{Sigmoid}(Z_{global}) \cdot \|\nabla I\| $$
High $S$ means the pixel is likely a target, so we should **reduce** $\alpha$.

### C. Scene Modulator ($\gamma$)
A global parameter that adjusts aggressiveness based on the scene's dynamic range.
$$ \gamma = f\left(\frac{I_{max}}{I_{mean}}\right) $$
If the scene has extreme hot spots, $\gamma$ decreases to prevent over-smoothing.

## 4. Final Equation
combining these terms, we get the adaptive weight:
$$ \alpha = \gamma \cdot \text{Sigmoid}(L) \cdot (1 - S) \cdot (1 - \text{Structure}) $$

This formulation ensures that even if a pixel looks like noise locally (high $L$), it will be preserved if it is part of a salient target (high $S$) or a strong edge.
