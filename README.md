# 📊 Multiple Linear Regression – Student Performance Prediction

A complete implementation of **Multiple Linear Regression** using **scikit-learn** to predict student exam performance based on multiple academic and lifestyle factors.  
This project follows an **industry-style ML workflow**, from data generation to model evaluation and visualization.

---

## 🚀 Project Overview

Unlike simple linear regression, real-world problems depend on **multiple variables**.  
This project predicts a student's **final exam score** using five independent features that realistically influence academic performance.

The goal is not just prediction, but **interpretability** — understanding how each feature contributes to the outcome.

---

## 🧠 Features Used

| Feature | Description |
|------|-----------|
| `study_hours` | Average daily study hours |
| `sleep_hours` | Average daily sleep duration |
| `attendance_percentage` | Class attendance (%) |
| `previous_score` | Previous academic performance |
| `stress_level` | Stress level on a scale of 1–10 |

**Target Variable:**  
- `final_score`

---

## 🧪 Dataset

- **Type:** Synthetic but realistic
- **Size:** 10,000 samples
- **Purpose:** Mimics professional education analytics datasets
- **Storage:** `data/performance.csv`

The dataset was generated with controlled noise to simulate real-world variability.

---

## ⚙️ Model Used

- **Algorithm:** Multiple Linear Regression
- **Library:** scikit-learn
- **Train-Test Split:** 80 / 20
- **Random State:** Fixed for reproducibility

---

## 📈 Model Performance

| Metric | Value |
|------|------|
| **R² Score** | **0.87** |
| **Mean Absolute Error (MAE)** | **3.95** |
| **Mean Squared Error (MSE)** | **24.7** |

📌 **Interpretation:**
- The model explains **87% of the variance** in final scores.
- Low MAE indicates strong real-world prediction accuracy.
- Errors are well within an acceptable academic range.

---

## 📊 Visualizations

All plots are stored in the `visualize/` directory as `.png` files.

### Included Visuals:
- Feature vs Target scatter plots
- Coefficient importance bar chart
- Standardized coefficient comparison
- Residual distribution plots

These visualizations help validate:
- Linearity assumptions
- Feature influence
- Model reliability

---


