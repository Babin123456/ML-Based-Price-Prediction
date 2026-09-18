"""
Utility functions for data loading, preprocessing, evaluation metrics, and visualization.
"""

import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Add parent directory to path to allow importing config
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config


def load_and_preprocess_data(dataset_name: str = config.DEFAULT_DATASET):
    """
    Loads dataset, handles missing values, encodes categorical columns, and splits into train/test.
    """
    file_path = config.get_dataset_path(dataset_name)
    df = pd.read_csv(file_path)

    # Handle missing values
    df = df.dropna().copy()

    # Ensure required columns exist
    missing_features = [col for col in config.FEATURES if col not in df.columns]
    if missing_features:
        raise ValueError(f"Dataset {file_path.name} is missing required columns: {missing_features}")
    if config.TARGET not in df.columns:
        raise ValueError(f"Dataset {file_path.name} is missing target column: '{config.TARGET}'")

    # Encode categorical features
    label_encoders = {}
    for col in config.CATEGORICAL_COLS:
        if col in df.columns:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col].astype(str))
            label_encoders[col] = encoder

    X = df[config.FEATURES].copy()
    y = df[config.TARGET].copy()

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_STATE
    )

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return {
        "df": df,
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "X_train_scaled": X_train_scaled,
        "X_test_scaled": X_test_scaled,
        "scaler": scaler,
        "label_encoders": label_encoders,
        "dataset_name": dataset_name,
        "file_path": file_path
    }


def compute_evaluation(y_true, y_pred, X_test, df, label_encoders):
    """
    Calculates R2, MAE, RMSE and prepares average prices dataframe for visualization.
    """
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    # Add Commodity column back for visualization
    X_test_comm = df.loc[X_test.index, 'Commodity'].copy()
    y_test_df = pd.DataFrame({
        'Actual': y_true,
        'Predicted': y_pred,
        'Commodity': X_test_comm
    })

    # Reverse Map Commodity Labels
    if 'Commodity' in label_encoders:
        y_test_df['Commodity'] = label_encoders['Commodity'].inverse_transform(y_test_df['Commodity'].astype(int))

    avg_prices = y_test_df.groupby('Commodity').mean().reset_index()

    return {
        "metrics": {"R2": r2, "MAE": mae, "RMSE": rmse},
        "avg_prices": avg_prices,
        "y_test_df": y_test_df
    }


def get_commodity_colors(commodities):
    """Dynamically resolves harmonious colors for a list of commodities."""
    palette = sns.color_palette("tab10", max(len(commodities), 10))
    color_map = {}
    for idx, comm in enumerate(commodities):
        if comm in config.COMMODITY_COLORS:
            color_map[comm] = config.COMMODITY_COLORS[comm]
        else:
            color_map[comm] = palette[idx % len(palette)]
    return color_map


def plot_line_graph(avg_prices, model_name="Model", save_path=None, show=False):
    """Generates a clean Line Graph of Actual vs Predicted prices per commodity with residual shading."""
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)

    x = np.arange(len(avg_prices))
    commodities = avg_prices["Commodity"].tolist()
    actual = avg_prices["Actual"].values
    predicted = avg_prices["Predicted"].values

    # Plot actual and predicted lines
    ax.plot(x, actual, marker='o', markersize=8, linewidth=2.5, color='#1E3A8A', label="Actual Price", zorder=4)
    ax.plot(x, predicted, marker='s', markersize=7, linewidth=2.2, linestyle='--', color='#DC2626', label=f"{model_name} Predicted", zorder=4)

    # Shaded difference area
    ax.fill_between(x, actual, predicted, color='#DC2626', alpha=0.12, label="Prediction Delta / Gap", zorder=2)

    # Value annotations with alternating vertical offsets and soft white background pills
    y_range = actual.max() - actual.min() if (actual.max() - actual.min()) > 0 else 1000
    for i, (act, pred) in enumerate(zip(actual, predicted)):
        diff = pred - act
        act_offset = 12 if diff <= 0 else -18
        pred_offset = -18 if diff <= 0 else 12

        ax.annotate(f"₹{act:,.0f}", (i, act), textcoords="offset points",
                    xytext=(0, act_offset), ha='center', fontsize=8.5, fontweight='bold', color='#1E3A8A',
                    bbox=dict(boxstyle='round,pad=0.18', facecolor='white', edgecolor='#DBEAFE', alpha=0.9, linewidth=0.5))
        ax.annotate(f"₹{pred:,.0f}", (i, pred), textcoords="offset points",
                    xytext=(0, pred_offset), ha='center', fontsize=8.5, fontweight='bold', color='#DC2626',
                    bbox=dict(boxstyle='round,pad=0.18', facecolor='white', edgecolor='#FEE2E2', alpha=0.9, linewidth=0.5))

    y_max = max(actual.max(), predicted.max())
    y_min = min(actual.min(), predicted.min())
    ax.set_ylim(max(0, y_min - y_range * 0.15), y_max + y_range * 0.22)

    ax.set_xticks(x)
    ax.set_xticklabels(commodities, rotation=35, ha='right', fontsize=10, fontweight='semibold')
    ax.set_ylabel("Price (₹ per Kg)", fontsize=11, fontweight='bold', color='#1F2937')
    ax.set_title(f"Actual vs {model_name} Predicted Prices per Commodity", fontsize=13, fontweight='bold', pad=14, color='#111827')

    ax.grid(True, linestyle='--', alpha=0.35, color='#9CA3AF', zorder=1)
    ax.set_axisbelow(True)
    ax.legend(frameon=True, facecolor='white', framealpha=0.95, edgecolor='#E5E7EB', loc='upper right', fontsize=9.5)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()


def plot_bar_graph(avg_prices, model_name="Model", save_path=None, show=False):
    """Generates a modern grouped Bar Graph with angled, collision-free price annotations."""
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)

    bar_width = 0.35
    x_indexes = np.arange(len(avg_prices))
    commodities = avg_prices["Commodity"].tolist()
    actual = avg_prices["Actual"].values
    predicted = avg_prices["Predicted"].values

    # Distinct, unified professional colors for Actual vs Predicted
    bars_actual = ax.bar(x_indexes - bar_width / 2, actual, width=bar_width,
                         color='#1E3A8A', alpha=0.9, label="Actual Price",
                         edgecolor='#172554', linewidth=0.8, zorder=3)
    bars_predicted = ax.bar(x_indexes + bar_width / 2, predicted, width=bar_width,
                            color='#E07A5F', alpha=0.9, label=f"{model_name} Predicted",
                            edgecolor='#C85A3B', linewidth=0.8, zorder=3)

    y_max = max(actual.max(), predicted.max())
    ax.set_ylim(0, y_max * 1.24)

    # Angled price annotations at 45° so adjacent bars never collide
    offset = y_max * 0.015
    for bar in bars_actual:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + offset, f'₹{h:,.0f}',
                ha='left', va='bottom', fontsize=8.5, fontweight='bold', color='#1E3A8A', rotation=45)

    for bar in bars_predicted:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + offset, f'₹{h:,.0f}',
                ha='left', va='bottom', fontsize=8.5, fontweight='bold', color='#C85A3B', rotation=45)

    ax.set_xticks(x_indexes)
    ax.set_xticklabels(commodities, rotation=35, ha='right', fontsize=10, fontweight='semibold')
    ax.set_ylabel("Price (₹ per Kg)", fontsize=11, fontweight='bold', color='#1F2937')
    ax.set_title(f"Actual vs {model_name} Predicted Prices per Commodity (Bar Graph)",
                 fontsize=13, fontweight='bold', pad=14, color='#111827')

    ax.grid(axis='y', linestyle='--', alpha=0.35, color='#9CA3AF', zorder=1)
    ax.set_axisbelow(True)
    ax.legend(frameon=True, facecolor='white', framealpha=0.95, edgecolor='#E5E7EB', loc='upper left', fontsize=10)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()


def plot_pie_chart(avg_prices, model_name="Model", save_path=None, show=False):
    """Generates an ultra-clean dual-ring donut chart with zero text overlaps and dedicated legend table."""
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)

    commodities = avg_prices['Commodity'].tolist()
    actual_sizes = avg_prices['Actual'].values
    predicted_sizes = avg_prices['Predicted'].values

    # Harmonious color palette
    palette = sns.color_palette("Set2", len(commodities))
    colors_actual = palette
    colors_pred = [sns.desaturate(c, 0.6) for c in palette]

    # Outer Ring (Actual Prices) - clean donut
    outer_pie = ax.pie(
        actual_sizes,
        autopct=lambda p: f'{p:.1f}%' if p > 5 else '',
        pctdistance=0.86,
        startangle=140,
        colors=colors_actual,
        wedgeprops=dict(width=0.32, edgecolor='white', linewidth=2),
        textprops=dict(fontsize=8.5, fontweight='bold', color='#1F2937')
    )
    wedges_outer = outer_pie[0]

    # Inner Ring (Predicted Prices) - clean nested donut
    ax.pie(
        predicted_sizes,
        autopct=lambda p: f'{p:.1f}%' if p > 6 else '',
        pctdistance=0.65,
        radius=0.76,
        startangle=140,
        colors=colors_pred,
        wedgeprops=dict(width=0.28, edgecolor='white', linewidth=2),
        textprops=dict(fontsize=8, fontweight='semibold', color='#374151')
    )

    # Central Badge - clean and uncluttered
    ax.text(0, 0, f"Outer: Actual\nInner: Predicted\n({model_name})",
            ha='center', va='center', fontsize=9, fontweight='bold', color='#1F2937',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#F9FAFB', edgecolor='#E5E7EB', alpha=0.9))

    # Clean, formatted Legend Table beside the chart
    legend_labels = [
        f"{comm:<12} | Actual: ₹{act:,.0f} | Pred: ₹{pred:,.0f}"
        for comm, act, pred in zip(commodities, actual_sizes, predicted_sizes)
    ]
    ax.legend(wedges_outer, legend_labels,
              title="Commodity Price Breakdown",
              title_fontsize='10',
              loc="center left",
              bbox_to_anchor=(1.02, 0.5),
              frameon=True,
              facecolor='white',
              framealpha=0.95,
              edgecolor='#E5E7EB',
              fontsize=8.5,
              prop={'family': 'monospace', 'size': 8.5})

    ax.set_title(f"Commodity Price Distribution: Actual vs {model_name} Predicted",
                 fontsize=13, fontweight='bold', pad=18, color='#111827')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()
