"""
Configuration settings for Agricultural Price Prediction Project.
Provides dynamic file paths, dataset mappings, feature lists, and visualization settings.
"""

from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"
MODELS_DIR = BASE_DIR / "models"

# Ensure results directory exists
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Datasets Mapping
DATASETS = {
    "babin": DATA_DIR / "Book1(Babin).csv",
    "liza": DATA_DIR / "Book1(Liza).csv",
    "ritika": DATA_DIR / "Book1(Ritika).csv",
    "master": DATA_DIR / "Price_Agriculture_commodities_Week.csv",
}

TEAM_DATASETS = ["babin", "liza", "ritika"]
DEFAULT_DATASET = "all"

# Seasonal Representation Mapping
SEASON_INFO = {
    "babin": {"name": "Babin", "season": "Winter", "desc": "Winter Produce (Apple, Beetroot, Cabbage, Carrot, Cauliflower, Orange)"},
    "liza": {"name": "Liza", "season": "Monsoon", "desc": "Monsoon / Fruit Produce (Banana, Guava, Papaya, Peach, Plum)"},
    "ritika": {"name": "Ritika", "season": "Summer", "desc": "Summer Produce (Bhindi, Bitter Gourd, Brinjal, Mango, Spinach)"},
}

# ML Pipeline Settings
CATEGORICAL_COLS = ['State', 'District', 'Market', 'Commodity', 'Variety', 'Grade']
FEATURES = ['State', 'Market', 'Commodity', 'Variety', 'Grade', 'Min Price', 'Max Price']
TARGET = 'Modal Price'
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Random Forest Hyperparameters
RF_PARAMS = {
    "n_estimators": 100,
    "random_state": RANDOM_STATE
}

# SVM Hyperparameters
SVM_PARAMS = {
    "kernel": "rbf",
    "C": 100.0,
    "epsilon": 0.1
}

# Commodity Custom Color Mapping for Consistent Charts
COMMODITY_COLORS = {
    # Babin's Commodities
    "Apple": "#E63946",
    "Beetroot": "#9B2226",
    "Cabbage": "#2A9D8F",
    "Cauliflower": "#90BE6D",
    "Carrot": "#F4A261",
    "Orange": "#F77F00",

    # Liza's Commodities
    "Banana": "#F9C74F",
    "Plum": "#7209B7",
    "Papaya": "#FB8500",
    "Guava": "#588157",
    "Peach": "#F28482",

    # Ritika's Commodities
    "Bhindi(Ladies Finger)": "#43AA8B",
    "Brinjal": "#5E548E",
    "Spinach": "#386641",
    "Bitter gourd": "#3A5A40",
    "Mango": "#FFB703",
}

def get_dataset_path(name: str = DEFAULT_DATASET) -> Path:
    """
    Returns the Path object for a given dataset key, file name, or path.
    Supports:
      - Short aliases: 'babin', 'liza', 'ritika', 'master', 'week'
      - Exact file names: 'Book1(Babin).csv', 'Price_Agriculture_commodities_Week.csv'
      - Relative paths: 'data/Book1(Liza).csv'
      - Case-insensitive lookups
    """
    if not name:
        return DATASETS[DEFAULT_DATASET]

    cleaned = str(name).strip().strip("'\"")
    key = cleaned.lower()

    # 1. Direct key match in DATASETS dict
    if key in DATASETS:
        return DATASETS[key]

    # 2. Friendly aliases
    aliases = {
        "winter": DATA_DIR / "Book1(Babin).csv",
        "monsoon": DATA_DIR / "Book1(Liza).csv",
        "summer": DATA_DIR / "Book1(Ritika).csv",
        "week": DATA_DIR / "Price_Agriculture_commodities_Week.csv",
        "national": DATA_DIR / "Price_Agriculture_commodities_Week.csv",
        "book1(babin).csv": DATA_DIR / "Book1(Babin).csv",
        "book1(babin)": DATA_DIR / "Book1(Babin).csv",
        "book1(liza).csv": DATA_DIR / "Book1(Liza).csv",
        "book1(liza)": DATA_DIR / "Book1(Liza).csv",
        "book1(ritika).csv": DATA_DIR / "Book1(Ritika).csv",
        "book1(ritika)": DATA_DIR / "Book1(Ritika).csv",
        "price_agriculture_commodities_week.csv": DATA_DIR / "Price_Agriculture_commodities_Week.csv",
        "price_agriculture_commodities_week": DATA_DIR / "Price_Agriculture_commodities_Week.csv",
    }
    if key in aliases:
        return aliases[key]

    # 3. Direct path if it exists
    path_obj = Path(cleaned)
    if path_obj.exists() and path_obj.is_file():
        return path_obj

    # 4. Check inside data/ directory
    inside_data = DATA_DIR / path_obj.name
    if inside_data.exists() and inside_data.is_file():
        return inside_data

    # 5. Check inside data/ with .csv extension appended
    inside_data_csv = DATA_DIR / f"{path_obj.name}.csv"
    if inside_data_csv.exists() and inside_data_csv.is_file():
        return inside_data_csv

    # 6. Substring match inside data/
    for existing in DATA_DIR.glob("*.csv"):
        if key in existing.name.lower():
            return existing

    valid_keys = list(DATASETS.keys()) + [f.name for f in DATA_DIR.glob("*.csv")]
    raise FileNotFoundError(
        f"Dataset '{name}' could not be resolved.\n"
        f"Available options:\n"
        f"  • Aliases: {list(DATASETS.keys())}\n"
        f"  • Files in data/: {[f.name for f in DATA_DIR.glob('*.csv')]}\n"
    )

