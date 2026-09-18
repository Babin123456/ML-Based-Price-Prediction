# 📊 Agricultural Price Prediction Project

A machine learning project to predict agricultural commodity prices using Random Forest and Support Vector Machine (SVM) regression models.

## 📋 Project Overview

This project analyzes agricultural commodity prices and builds predictive models to forecast modal prices based on various features including state, market, commodity type, variety, and grade.

**Models Implemented:**

- Random Forest Regressor
- Support Vector Machine (SVM)

**Commodities Analyzed:**

- Banana, Plum, Papaya, Guava, Peach

## 📁 Project Structure

```text
├── data/                          # Raw datasets
│   ├── Book1(Babin).csv
│   ├── Book1(Liza).csv
│   ├── Book1(Ritika).csv
│   └── Price_Agriculture_commodities_Week.csv
├── models/                        # ML model implementations
│   ├── random_forest.py
│   └── svm.py
├── results/                       # Generated outputs & visualizations
├── config.py                      # Configuration settings
├── main.py                        # Entry point
├── requirements.txt               # Dependencies
└── README.md                      # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone/Navigate to the project directory:**

   ```bash
   cd "Mini Project (Price Prediction)"
   ```

2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **scikit-learn** - Machine learning algorithms
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization

## 🔧 Usage

### Run the complete pipeline

```bash
python main.py
```

### Run specific model

```bash
# Random Forest
python models/random_forest.py

# SVM
python models/svm.py
```

## 📊 Features Used

- **State** - Agricultural state
- **Market** - Market location
- **Commodity** - Type of agricultural commodity
- **Variety** - Specific variety of commodity
- **Grade** - Quality grade
- **Min Price** - Minimum recorded price
- **Max Price** - Maximum recorded price

**Target Variable:** Modal Price (₹ per Kg)

## 📈 Model Workflow

1. **Data Loading & Cleaning**
   - Remove missing values
   - Handle outliers

2. **Feature Engineering**
   - Encode categorical features (State, District, Market, Commodity, Variety, Grade)
   - Normalize numerical features using StandardScaler

3. **Train-Test Split**
   - 80% training data
   - 20% testing data
   - Random state: 42 (for reproducibility)

4. **Model Training**
   - Random Forest: 100 estimators
   - SVM: (configuration in model file)

5. **Evaluation & Visualization**
   - Line graphs: Trend comparison
   - Bar charts: Price comparison by commodity
   - Pie charts: Price distribution analysis

## 📊 Output Visualizations

The models generate three types of visualizations:

- **Line Graph** - Actual vs Predicted price trends
- **Bar Graph** - Commodity-wise price comparison with values
- **Pie Chart** - Dual-layer pie (Actual outer, Predicted inner)

## 🔍 Key Insights

- Actual vs Predicted price analysis per commodity
- Average modal price calculation by commodity
- Color-coded visualization for easy interpretation

## 👥 Team Members

- Babin
- Liza
- Ritika

## 📝 Notes

- All prices are in **₹ per Kg**
- Data is standardized using StandardScaler before model training
- Categorical features use LabelEncoder for model compatibility

## 🐛 Troubleshooting

**Import Errors:**

```bash
pip install --upgrade scikit-learn pandas numpy matplotlib seaborn
```

**File Path Issues:**

- Ensure CSV files are in the `data/` folder
- Update file paths in `config.py` if needed

## 📄 License

This is an academic mini project.

## 📧 Contact

For questions or issues, refer to the project documentation or contact team members.

---

**Last Updated:** 18th September, 2026
