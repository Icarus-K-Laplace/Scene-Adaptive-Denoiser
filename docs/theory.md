# Theoretical Formulation

## 1. The Core Conflict
In infrared hot targets as noise.

## 2. Our Solution: Soft Fusion
We propose a soft fusion formulation:
$$ \hat{I} = (1 - \alpha) I_{obs} + \alpha I_{restored} $$

The key is the design of $\alpha$, which represents the **probability of being noise**.

## 3. Deriving Alpha
We model $\alpha$ as a joint probability:
$$ \alpha \approx P(\text{Noise} | \text{Local}, \text{Global}) $$

This is decomposed into three factors:
1.  **Local Likelihood ($L$)**: How different is the pixel from its neighbors?
2.  **Saliency Prior ($S$)**: Is this pixel part of a hot target? (Inversely related to noise probability)
3.  **Scene Modulator ($\gamma$)**: Is the overall scene high-contrast?

$$ \alpha = \gamma \cdot \text{Sigmoid}(L) \cdot (1 - S) $$

This formulation ensures that even if a pixel looks like noise locally (high $L$), it will be preserved if it is part of a salient target (high $S$).
