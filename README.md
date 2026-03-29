# 🛡️ SafeGuard AI

### *"The security that knows when it really matters."*
*Fewer false alarms. More control. True peace of mind.*

<br>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Prototype-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

<br>

<a href="README.it.md"><img src="https://flagcdn.com/w20/it.png" width="20" alt="IT"/> Leggi in italiano</a> &nbsp;·&nbsp; <img src="https://flagcdn.com/w20/gb.png" width="20" alt="EN"/> **English**

<br>

> **SafeGuard AI** is a smart home security prototype that uses machine learning to distinguish real threats from harmless events — so your alarm only goes off when it truly matters.

<br>

[📦 Source Code](#-source-code) · [🚀 Getting Started](#-getting-started) · [⚙️ How It Works](#%EF%B8%8F-how-it-works) · [📊 Results](#-results) · [👥 Team](#-team)

---

## ⚠️ The Problem

Traditional home security systems treat every movement the same way. A gust of wind, your cat jumping off the couch, a branch hitting the window — all of them trigger the same alarm as a real intruder would.

This creates a vicious cycle:

- 🔔 **Too many false alarms** → users start ignoring alerts
- 😤 **Unnecessary stress** → constant interruptions and anxiety
- 🚨 **Emergency service overload** → resources wasted on non-events
- 📉 **Loss of trust** → the system becomes background noise

---

## 💡 The Solution

SafeGuard AI applies **multi-sensor fusion + machine learning** to understand *context*, not just detect raw signals.

Instead of asking *"did something move?"*, it asks **"what is actually happening?"**

```
Motion sensor + Sound sensor + Temperature/Fume sensor
                        ↓
             Random Forest Classifier
                        ↓
     NORMAL · ANIMAL · PERSON · EMERGENCY
                        ↓
          Smart response — only when needed
```

| Event | What it means | System Response |
|---|---|---|
| 🟢 `NORMAL` | Wind, vibration, background noise | No action |
| 🟡 `ANIMAL` | Pet or small animal detected | Logged silently |
| 🟠 `PERSON` | Human presence detected | Owner notified |
| 🔴 `EMERGENCY` | Fire, break-in, critical threat | Emergency services alerted |

---

## 🎯 Who Is It For?

SafeGuard AI is designed for **families, homeowners, and professionals** — especially anyone living in a dynamic environment with pets, children, or frequent visitors who are tired of dealing with false alarms.

![SafeGuard AI Product Concept](assets/safeguardai-product.png)

---

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| **Sensors** | Motion (PIR), Sound (dB), Temperature / Fume |
| **ML Model** | Random Forest Classifier (`scikit-learn`) |
| **Processing** | Edge computing — local inference, no cloud dependency |
| **Language** | Python 3.8+ |
| **Libraries** | `numpy`, `pandas`, `matplotlib`, `scikit-learn` |

---

## 📦 Source Code

The full implementation is available in a single self-contained script:

```
safeguard-ai/
│
├── safeguard_ai.py                # Main pipeline (dataset → EDA → train → simulate)
├── assets/
│   ├── safeguardai-logo.png
│   ├── safeguardai-product.png
│   └── safeguardai-use.png
├── safeguard_eda_plot.png         # Auto-generated: sensor averages per class
├── safeguard_confusion_matrix.png # Auto-generated: model evaluation
└── README.md
```

👉 [`safeguard_ai.py`](./safeguard_ai.py)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-org/safeguard-ai.git
cd safeguard-ai
```

### 2. Install dependencies

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 3. Run

```bash
python safeguard_ai.py
```

---

## ⚙️ How It Works

The script runs a complete ML pipeline in five stages:

**① Dataset Generation**
400 synthetic sensor events are simulated with realistic value ranges per class:

| Class | Count | Motion | Sound (dB) | Temp Δ (°C) |
|---|---|---|---|---|
| NORMAL | 160 | 5–30 | 15–45 | −0.3 – 0.3 |
| ANIMAL | 110 | 35–70 | 30–65 | −0.2 – 0.4 |
| PERSON | 90 | 60–100 | 45–90 | 0.3 – 1.5 |
| EMERGENCY | 40 | 70–100 | 80–130 | 2.0 – 8.0 |

**② Exploratory Data Analysis (EDA)**
Average sensor values are plotted per class to visualize feature separation between event types.

**③ Model Training**
A `RandomForestClassifier` (50 estimators) is trained on an 80/20 split with a fixed random seed for reproducibility.

**④ Evaluation**
Accuracy score and confusion matrix are computed and saved automatically as PNG files.

**⑤ Live Event Simulator**
Three example events are classified end-to-end with automated responses:

```text
'Falling leaf'     → NORMAL:     No action needed.
'Cat on the sofa'  → ANIMAL:     Logged. No alarm triggered.
'Possible fire'    → EMERGENCY:  ALERT — Call emergency services!
```

![SafeGuard AI in Daily Use](assets/safeguardai-use.png)

---

## 📊 Results

The model achieves strong classification performance thanks to the well-separated sensor distributions across event classes. Two output files are generated at runtime:

- **`safeguard_eda_plot.png`** — bar chart of average sensor readings per event type
- **`safeguard_confusion_matrix.png`** — heatmap of predicted vs. actual labels

| Parameter | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Estimators | 50 trees |
| Train / Test split | 80% / 20% |
| Random seed | 42 |
| Features | `motion`, `sound`, `temp_delta` |

---

## 👥 Team

Developed by students as part of the **Artificial Intelligence course** within the **[RiseVET](https://risevet.eu) program** — an educational initiative promoting hands-on experimentation with AI, IoT, and emerging technologies.

- **Flavio Lanzafame** — [@flaviolanzafame](https://github.com/flaviolanzafame)
- **Luigi Larecchiuta** — [@Luigi879](https://github.com/Luigi879)
- **Carmelo Vicari** — [@carmelo19vicari](https://github.com/carmelo19vicari)
- **Carmelo Vicari** — [@VicariCarmelo8](https://github.com/VicariCarmelo8)

---

## 📄 License

Released under the [MIT License](LICENSE).

---

<div align="center">

Built with Python · scikit-learn · pandas · matplotlib

</div>
