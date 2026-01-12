# Scene-Adaptive-Denoiser
Scene-Adaptive-Denoiser: A unified framework for infrared impulse noise removal. It replaces binary detection with a continuous, saliency-guided soft fusion strategy. By integrating thermal target priors, structure consistency, and global scene modulation, it robustly protects hot targets while cleaning background noise.
# Scene-Adaptive-Denoiser 🌡️

### A Unified Target-Aware Framework for Infrared Impulse Noise Removal

> **Developed independently by an undergraduate student.**
> This project challenges the traditional "detect-then-restore" paradigm. Instead of hard classification, it introduces a continuous, saliency-guided soft restoration mechanism tailored for thermal imaging.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 💡 The "Why" Behind This Project

Most impulse noise removal algorithms (like AMF, ACWM) treat images as a grid of numbers. They focus solely on local statistics, often ignoring the **semantic context**.

**My Observation:**
In infrared (thermal) images, "hot" targets (people, vehicles) and structural edges are the most critical information. A blind statistical filter often blurs these salient features while removing noise.

**My Hypothesis:**
> *Can we design a filter that "knows" what is important?*
> A good denoiser should be **conservative** on salient targets/edges and **aggressive** on the background, modulated by the **global scene complexity**.

This led to the **Scene-Adaptive Unified Framework**.

---

## 🔬 Key Innovations

### 1. Thermal Saliency Protection
Instead of treating all pixels equally, I introduce a **Thermal Saliency Map** ($S$). It combines global intensity statistics (Z-score) and local gradient magnitude to identify "hot" targets.
$$ S(x) = \sigma(ZResult: Edges are preserved even under heavy noise.*

### 3. Scene-Adaptive Global Control
A novel **Gamma ($\gamma$) Factor** estimates the scene's "aggressiveness" based on its dynamic range.
$$ \gamma = f(\frac{I_{max}}{I_{mean}}) $$
*Result: The algorithm automatically becomes more conservative in high-contrast scenes.*

### 4. Soft Confidence Fusion
Instead of a binary "noise vs. clean" decision, I use a continuous **Confidence Map** ($C$) to blend the original pixel with the restoration candidate.
$$ I_{out} = (1 - \alpha) I_{in} + \alpha I_{med}, \quad \alpha \propto \gamma \cdot C \cdot (1-S) $$

---

## 📊 Performance

Tested on `scene1.png` (Infrared):

| Metric | Standard Median | **Scene-Adaptive (Ours)** |
|:---:|:---:|:---:|
| **Target Preservation** | Blurred edges | **Sharp thermal targets** |
| **Background Noise** | Residual artifacts | **Clean background** |
| **Adaptability** | Fixed parameter | **Auto-tuning per image** |

*> Note: This---

## 📂 Code Structure

- `src/denoiser.py`: The unified implementation. Single-pass, $O(N)$ complexity.
- `docs/theory.md`: Detailed explanation of the saliency and consistency formulations.

---

## 🧑‍🎓 Author's Note

This algorithm represents my attempt to move beyond "tuning parameters" to "designing logic". By integrating global scene understanding with local pixel restoration, I created a system that behaves more like a human observer—protecting what matters and cleaning what doesn't.

---

## 📄 License

MIT License
