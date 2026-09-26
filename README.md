# 🌾 ML-Based Price Prediction for Agri-Horticultural Commodities

<!-- markdownlint-disable MD013 MD033 -->

![Agricultural Price Prediction Header Wave](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=230&section=header&text=Agri-Horticultural%20Price%20Prediction&fontSize=34&fontAlignY=36&fontColor=ffffff&desc=Official%20Codebase%20•%20Springer%20Nature%20(SSWC)&descAlignY=58&descAlign=50&descColor=e2e8f0)

[![Typing SVG Animation](https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&pause=1000&color=10B981&center=true&vCenter=true&width=820&lines=🌱+Multi-Seasonal+Price+Forecasting+(Winter,+Rainy,+Summer);🌲+Random+Forest+Regressor+(R²+=+98.93%25)+vs+SVM+(R²+=+91.85%25);🏛️+Published+in+Springer+Nature+(Smart+Systems+&+Wireless+Comm.);🎓+Department+of+CSE,+Adamas+University;📄+DOI:+10.1007%2F978-3-032-21164-4_30)](https://doi.org/10.1007/978-3-032-21164-4_30)

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://github.com/Babin123456/ML-Based-Price-Prediction)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=for-the-badge)](https://scikit-learn.org)
[![Random Forest R²](https://img.shields.io/badge/Random%20Forest%20R²-98.93%25-10b981?style=for-the-badge)](./results/master_comparison_all.png)
[![SVM R²](https://img.shields.io/badge/SVR%20R²-91.85%25-06b6d4?style=for-the-badge)](./results/master_comparison_all.png)
[![Springer Nature](https://img.shields.io/badge/Springer%20Nature-Chapter%2030-0070a8?logo=springer&logoColor=white&style=for-the-badge)](https://link.springer.com/chapter/10.1007/978-3-032-21164-4_30)
[![EurekaMag](https://img.shields.io/badge/EurekaMag-107899461-3e7619?style=for-the-badge)](https://eurekamag.com/research/107/899/107899461.php)
[![DOI](https://img.shields.io/badge/DOI-10.1007%2F978--3--032--21164--4__30-10b981?style=for-the-badge)](https://doi.org/10.1007/978-3-032-21164-4_30)
[![License: MIT](https://img.shields.io/badge/License-MIT-8b5cf6?style=for-the-badge)](LICENSE)
[![Project Views Counter](https://komarev.com/ghpvc/?username=Babin123456-ML-Price-Prediction&color=10b981&style=for-the-badge&label=PROJECT+VIEWS)](https://github.com/Babin123456/ML-Based-Price-Prediction)

> [!IMPORTANT]
> **Official Research Publication — Springer Nature:**  
> This repository hosts the official implementation, multi-seasonal datasets, and visualization pipelines for the published research paper:  
> **"ML-Based Price Prediction for Agri-Horticultural Commodities"**  
> Published in: *Smart Systems and Wireless Communication*, **Smart Innovation, Systems and Technologies (SIST, Vol. 484)**, **Springer Nature Switzerland / Springer, Cham**, pp. 378–389, 2026.  
>
> 🔗 **Official Springer Link:** [link.springer.com/chapter/10.1007/978-3-032-21164-4_30](https://link.springer.com/chapter/10.1007/978-3-032-21164-4_30)  
> 🔗 **Official Google Share Link:** [share.google/D4xw5wSU0QzhLgppF](https://share.google/D4xw5wSU0QzhLgppF)  
> 🌐 **EurekaMag Academic Record:** [eurekamag.com/research/107/899/107899461.php](https://eurekamag.com/research/107/899/107899461.php) (Accession: `107899461`)  
> 📌 **Digital Object Identifier (DOI):** [`10.1007/978-3-032-21164-4_30`](https://doi.org/10.1007/978-3-032-21164-4_30)

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 📚 Research Paper & Publication Summary

| Parameter | Publication Metadata |
| :--- | :--- |
| **Paper Title** | **ML-Based Price Prediction for Agri-Horticultural Commodities** |
| **Authors** | **Dr. Debdutta Pal**, **Babin Bid**, **Ritika Pramanick**, **Liza Ghosh** |
| **Affiliation** | Department of Computer Science & Engineering, Adamas University, Kolkata, India |
| **Proceedings Title** | *Smart Systems and Wireless Communication* |
| **Book Series** | **Smart Innovation, Systems and Technologies (SIST)**, Volume 484 |
| **Conference** | International Conference on Smart Systems and Wireless Communication (SSWC) |
| **Publisher** | **Springer Nature Switzerland / Springer, Cham** |
| **Online Publication Date** | May 01, 2026 (Online First: March 2026) |
| **Page Numbers** | pp. 378–389 |
| **Print ISBN / Online ISBN** | `978-3-032-21164-4` / `978-3-032-21163-7` |
| **Series ISSN** | `2190-3018` (Print) / `2190-3026` (Electronic) |
| **Digital Object Identifier** | [`10.1007/978-3-032-21164-4_30`](https://doi.org/10.1007/978-3-032-21164-4_30) |
| **Indexing & Repositories** | [Springer Nature Link](https://link.springer.com/chapter/10.1007/978-3-032-21164-4_30) • [EurekaMag (ID: 107899461)](https://eurekamag.com/research/107/899/107899461.php) • [Google Share Link](https://share.google/D4xw5wSU0QzhLgppF) |

### 📖 Paper Abstract

> *"The agricultural sector is currently facing significant hardships due to the uneven pricing of agri-horticultural commodities such as pulses and vegetables. The objective of our research is to develop machine learning-based models for predicting the prices of vegetables and fruits across different seasons. In our study, we focused on three major Indian seasons: winter, rainy, and summer. These crops are typically seasonal, and our research scope is confined to such crops. Using historical price data, weather conditions, and socioeconomic features, the models provide precise and timely predictions to support crop planning, market interventions, and price stabilization efforts. We employ Support Vector Machine (SVM) and Random Forest (RF) to visualize seasonal price trends and evaluate their effectiveness. Line graphs, bar graphs, and pie charts are utilized to highlight essential data features. These visualizations help stakeholders understand market patterns and mitigate risks associated with price fluctuations. Ultimately, the study emphasizes the role of ML-driven predictive analytics in empowering farmers and reducing price uncertainties for consumers."*

**Keywords:** `Agri-horticultural Commodities`, `Support Vector Machine`, `Random Forest`, `ML-driven Predictive Analytics`, `Socioeconomic`

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 📋 Project Overview

This project analyzes market prices of various agricultural commodities across India and builds predictive machine learning models to forecast **Modal Prices (₹ per Kg)** based on market and commodity characteristics such as State, District, Market, Commodity type, Variety, Grade, Minimum Price, and Maximum Price.

### Models Implemented

- **Random Forest Regressor** (`n_estimators=100`, `random_state=42`)
- **Support Vector Regressor (SVR)** (`kernel='rbf'`, `C=100.0`, `epsilon=0.1`)

### Seasonal Commodity Groups Analyzed

The project analyzes agricultural produce across three major harvest seasons:

- ❄️ **Winter Season (Babin's Dataset)**: Apple, Beetroot, Cabbage, Carrot, Cauliflower, Orange
- 🌧️ **Monsoon / Fruit Season (Liza's Dataset)**: Banana, Guava, Papaya, Peach, Plum
- ☀️ **Summer Season (Ritika's Dataset)**: Bhindi (Ladies Finger), Bitter gourd, Brinjal, Mango, Spinach
- 🇮🇳 **National Master Dataset**: Comprehensive weekly national agricultural commodity records

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 📁 Project Structure

```text
├── data/                                      # Raw CSV datasets
│   ├── Book1(Babin).csv
│   ├── Book1(Liza).csv
│   ├── Book1(Ritika).csv
│   └── Price_Agriculture_commodities_Week.csv
├── models/                                    # ML model implementations & utilities
│   ├── legacy/                                # Original member scripts
│   ├── random_forest.py                       # Random Forest Regressor module
│   ├── svm.py                                 # Support Vector Regressor module
│   └── utils.py                               # Preprocessing, metrics & plotting utilities
├── results/                                   # Saved plots & visual analytics (22 figures)
├── config.py                                  # Centralized dynamic configuration & paths
├── main.py                                    # Pipeline entry point & model comparison
├── requirements.txt                           # Project dependencies
├── LICENSE                                    # MIT Open-Source License
├── .gitignore                                 # Git ignore rules
└── README.md                                  # Documentation
```

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Babin123456/ML-Based-Price-Prediction.git
   cd ML-Based-Price-Prediction
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv .venv
   # Git Bash (Windows):
   source .venv/Scripts/activate

   # PowerShell (Windows):
   .venv\Scripts\Activate.ps1

   # Command Prompt (cmd.exe):
   .venv\Scripts\activate.bat

   # Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 📦 Dependencies

- **pandas** - Data manipulation, CSV parsing, and aggregation
- **numpy** - Numerical operations and array indexing
- **scikit-learn** - Model training (RandomForestRegressor, SVR), scaling, and metrics
- **matplotlib** - Data plotting and dual-layer pie charts
- **seaborn** - Statistical visualizations and color palette generation

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 🔧 Usage

> [!TIP]
> **One-Click Execution:** Simply run `python main.py`. It automatically processes all three seasons (**Winter, Monsoon, and Summer**), evaluates both Random Forest and SVM on each, prints the Master Benchmark Summary, and saves all 22 figures to [`results/`](results/) in silent headless mode (no pop-up windows).

### Run the complete pipeline

```bash
python main.py
```

#### Expected Terminal Output

```text
🌱 Starting Agricultural Price Prediction Pipeline...
• Target Seasons:   Winter (Babin), Monsoon (Liza), Summer (Ritika)
• Selected Model:   Both (RF + SVM Comparison)
• Target Variable:  Modal Price
• Output Mode:      Headless saving (all figures saved to 'results/', no popup windows)

======================================================================
📂 Processing: Babin - Winter Season
📁 Source File: data\Book1(Babin).csv
======================================================================
  🌲 Random Forest Evaluation:  Complete
  🎯 SVM Evaluation:            Complete
  💾 Comparison plot saved to: results\model_comparison_babin.png

======================================================================
📂 Processing: Liza - Monsoon Season
📁 Source File: data\Book1(Liza).csv
======================================================================
  🌲 Random Forest Evaluation:  Complete
  🎯 SVM Evaluation:            Complete
  💾 Comparison plot saved to: results\model_comparison_liza.png

======================================================================
📂 Processing: Ritika - Summer Season
📁 Source File: data\Book1(Ritika).csv
======================================================================
  🌲 Random Forest Evaluation:  Complete
  🎯 SVM Evaluation:            Complete
  💾 Comparison plot saved to: results\model_comparison_ritika.png

💾 Master multi-dataset comparison plot saved to: results\master_comparison_all.png
✅ Execution completed successfully! All charts are saved under the 'results/' folder.
```

### Optional Power-User Commands

For users who want to isolate a single season or model, optional flags are supported:

| Command | Description |
| --- | --- |
| `python main.py --dataset winter` | Run on **Winter season** (Babin) only |
| `python main.py --dataset monsoon` | Run on **Monsoon season** (Liza) only |
| `python main.py --dataset summer` | Run on **Summer season** (Ritika) only |
| `python main.py --model rf` | Run **Random Forest** only across all seasons |
| `python main.py --model svm` | Run **SVM** only across all seasons |
| `python main.py --show` | Display interactive pop-up windows instead of silent saving |

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 📊 Features Used

The models predict the target price using the following feature set:

| Feature | Type | Description |
| --- | --- | --- |
| **State** | Categorical | State where the agricultural transaction occurred |
| **Market** | Categorical | Local APMC / Mandi market location |
| **Commodity** | Categorical | Specific agricultural crop/fruit/vegetable |
| **Variety** | Categorical | Specific variety or hybrid cultivar |
| **Grade** | Categorical | Quality classification grade (FAQ, Medium, etc.) |
| **Min Price** | Numerical | Minimum recorded trading price |
| **Max Price** | Numerical | Maximum recorded trading price |

**Target Variable:** `Modal Price` (₹ per Kg)

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 📈 Model Workflow

```mermaid
flowchart LR
    A["📁 Raw Mandi Data<br/>(Winter, Monsoon, Summer)"] --> B["⚙️ Feature Preprocessing<br/>(LabelEncoding, Scaling)"]
    B --> C["🤖 Dual ML Models<br/>(Random Forest & SVR)"]
    C --> D["📊 Evaluation Benchmark<br/>(R², MAE, RMSE)"]
    D --> E["📈 Visual Outputs<br/>(22 Headless Plots)"]
```

1. **Data Loading & Cleaning**:
   - Automated path resolution via `config.py` (relative paths, no broken absolute paths).
   - Missing value imputation and null handling (`dropna`).
2. **Feature Engineering & Preprocessing**:
   - Categorical columns encoded via `LabelEncoder`.
   - Feature scaling applied using `StandardScaler` on training split.
3. **Train-Test Split**:
   - 80% training data, 20% testing data (`test_size=0.2`, `random_state=42`).
4. **Model Training**:
   - Random Forest Regressor (`n_estimators=100`).
   - Support Vector Regressor (`kernel='rbf'`).
5. **Evaluation & Visualization**:
   - Evaluation metrics: $R^2$ Score, MAE, and RMSE.
   - Dual-layer visualization, trend comparison, and multi-dataset master benchmark.

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 🏆 Model Performance Comparison

Evaluated on the test split (80/20 train-test ratio) across each seasonal commodity group:

| Season & Contributor | Model | $R^2$ Score | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) |
| :--- | :--- | :--- | :--- | :--- |
| ❄️ **Winter Season (Babin)** | **Random Forest Regressor** | **0.9799** | **₹151.88** | **₹528.73** |
| ❄️ Winter Season (Babin) | Support Vector Machine (SVM) | 0.8062 | ₹631.69 | ₹1640.37 |
| 🌧️ **Monsoon Season (Liza)** | **Random Forest Regressor** | **0.9855** | **₹74.85** | **₹195.11** |
| 🌧️ Monsoon Season (Liza) | Support Vector Machine (SVM) | 0.8295 | ₹299.14 | ₹668.26 |
| ☀️ **Summer Season (Ritika)** | **Random Forest Regressor** | **0.9893** | **₹64.04** | **₹148.67** |
| ☀️ Summer Season (Ritika) | Support Vector Machine (SVM) | 0.9185 | ₹165.56 | ₹409.86 |

> **Key Finding:** Random Forest consistently outperforms SVM across all three seasons ($R^2 \approx 98\%\text{--}99\%$), demonstrating exceptional capability in capturing non-linear relationships and supply-demand interactions across agricultural mandi markets.

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 📊 Output Visualizations Gallery

All 22 visualization figures are automatically generated in silent headless mode and saved to the [`results/`](results/) folder:

### 🌟 Master Multi-Dataset Benchmark

The 3-panel comparative performance plot comparing $R^2$, MAE, and RMSE side-by-side across all seasonal datasets:

![Master Multi-Dataset Benchmark Comparison](./results/master_comparison_all.png)

### 🔍 Seasonal Model Comparison Charts

| ❄️ Winter Season (Babin) | 🌧️ Monsoon Season (Liza) | ☀️ Summer Season (Ritika) |
| :---: | :---: | :---: |
| ![Winter Model Comparison](./results/model_comparison_babin.png) | ![Monsoon Model Comparison](./results/model_comparison_liza.png) | ![Summer Model Comparison](./results/model_comparison_ritika.png) |

### 📈 Actual vs Predicted Trend Lines & Residuals

| Season | Random Forest Trend Line | Support Vector Machine Trend Line |
| :---: | :---: | :---: |
| **Winter (Babin)** | ![RF Line Winter](./results/rf_line_babin.png) | ![SVM Line Winter](./results/svm_line_babin.png) |
| **Monsoon (Liza)** | ![RF Line Monsoon](./results/rf_line_liza.png) | ![SVM Line Monsoon](./results/svm_line_liza.png) |
| **Summer (Ritika)** | ![RF Line Summer](./results/rf_line_ritika.png) | ![SVM Line Summer](./results/svm_line_ritika.png) |

### 🍩 Dual-Layer Nested Donut Charts (Price Distribution)

| Season | Random Forest Dual Donut | Support Vector Machine Dual Donut |
| :---: | :---: | :---: |
| **Winter (Babin)** | ![RF Pie Winter](./results/rf_pie_babin.png) | ![SVM Pie Winter](./results/svm_pie_babin.png) |
| **Monsoon (Liza)** | ![RF Pie Monsoon](./results/rf_pie_liza.png) | ![SVM Pie Monsoon](./results/svm_pie_liza.png) |
| **Summer (Ritika)** | ![RF Pie Summer](./results/rf_pie_ritika.png) | ![SVM Pie Summer](./results/svm_pie_ritika.png) |

### 📊 Commodity-Wise Price Bar Comparisons

| Season | Random Forest Grouped Bar | Support Vector Machine Grouped Bar |
| :---: | :---: | :---: |
| **Winter (Babin)** | ![RF Bar Winter](./results/rf_bar_babin.png) | ![SVM Bar Winter](./results/svm_bar_babin.png) |
| **Monsoon (Liza)** | ![RF Bar Monsoon](./results/rf_bar_liza.png) | ![SVM Bar Monsoon](./results/svm_bar_liza.png) |
| **Summer (Ritika)** | ![RF Bar Summer](./results/rf_bar_ritika.png) | ![SVM Bar Summer](./results/svm_bar_ritika.png) |

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 👥 Authors & Academic Supervision

- **Dr. Debdutta Pal** - Project Supervisor & Corresponding Author, Department of Computer Science & Engineering (CSE), Adamas University, Kolkata, India (`pal.debdutta@gmail.com`)
- **Babin Bid** - Co-Author & Lead Pipeline Developer, Department of Computer Science & Engineering (CSE), Adamas University, Kolkata, India
- **Liza Ghosh** - Co-Author & Research Analyst, Department of Computer Science & Engineering (CSE), Adamas University, Kolkata, India
- **Ritika Pramanick** - Co-Author & Machine Learning Developer, Department of Computer Science & Engineering (CSE), Adamas University, Kolkata, India

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

## 🐛 Troubleshooting

**Import Errors:**

```bash
pip install -r requirements.txt
```

**File Path Issues:**

- Datasets are stored in the `data/` directory.
- `config.py` automatically resolves absolute paths relative to the project root, so the project works out of the box regardless of directory location.

**Images Not Displaying on GitHub:**

- If visual plots appear as broken images on GitHub, ensure that the `results/` directory is tracked by git and pushed to the remote repository (`git add results/ && git commit -m "Add visualization charts" && git push`).

![Wave Divider](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=80&section=header)

<a id="academic-citation"></a>

## 📄 License & Academic Citation

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for complete terms.

### Academic Citation

If you utilize or reference this codebase, methodology, or seasonal findings in your academic work, please cite the published research paper:

```bibtex
@incollection{pal2026ml,
  author    = {Pal, Debdutta and Bid, Babin and Pramanick, Ritika and Ghosh, Liza},
  title     = {ML-Based Price Prediction for Agri-Horticultural Commodities},
  booktitle = {Smart Systems and Wireless Communication},
  series    = {Smart Innovation, Systems and Technologies},
  volume    = {484},
  pages     = {378--389},
  year      = {2026},
  publisher = {Springer, Cham},
  doi       = {10.1007/978-3-032-21164-4_30},
  url       = {https://link.springer.com/chapter/10.1007/978-3-032-21164-4_30},
  isbn      = {978-3-032-21164-4},
  issn      = {2190-3018}
}
```

![Footer Wave Animation](https://capsule-render.vercel.app/api?type=waving&color=0:10b981,50:06b6d4,100:3b82f6&height=120&section=footer)
