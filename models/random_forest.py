"""
Random Forest Regression Model for Agricultural Commodity Price Prediction.
"""

import sys
import argparse
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Include project root in path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import config
from models.utils import load_and_preprocess_data, compute_evaluation, plot_line_graph, plot_bar_graph, plot_pie_chart


def run_random_forest(dataset_name: str = "babin", save_plots: bool = True, show_plots: bool = False):
    """Trains Random Forest model, calculates performance metrics, and plots visualizations."""
    if dataset_name.lower() == "all":
        results = {}
        for ds in config.TEAM_DATASETS:
            results[ds] = run_random_forest(dataset_name=ds, save_plots=save_plots, show_plots=show_plots)
        return results

    print(f"\n==========================================")
    print(f"🌲 Training Random Forest Regressor")
    print(f"📁 Dataset: {dataset_name}")
    print(f"==========================================")

    data = load_and_preprocess_data(dataset_name)
    X_train_scaled = data["X_train_scaled"]
    X_test_scaled = data["X_test_scaled"]
    y_train = data["y_train"]
    y_test = data["y_test"]
    X_test = data["X_test"]
    df = data["df"]
    label_encoders = data["label_encoders"]

    # Model training
    model = RandomForestRegressor(**config.RF_PARAMS)
    model.fit(X_train_scaled, y_train)

    # Predict
    y_pred = model.predict(X_test_scaled)

    # Compute evaluation
    evaluation = compute_evaluation(y_test, y_pred, X_test, df, label_encoders)
    metrics = evaluation["metrics"]
    avg_prices = evaluation["avg_prices"]

    print(f"\n📊 Random Forest Model Evaluation:")
    print(f"  • R² Score: {metrics['R2']:.4f}")
    print(f"  • Mean Absolute Error (MAE): ₹{metrics['MAE']:.2f}")
    print(f"  • Root Mean Squared Error (RMSE): ₹{metrics['RMSE']:.2f}\n")

    # Plot paths with sanitized dataset tag
    dataset_tag = Path(dataset_name).stem.replace(" ", "_").lower()
    for member in ["babin", "liza", "ritika"]:
        if member in dataset_tag:
            dataset_tag = member
            break
    line_path = config.RESULTS_DIR / f"rf_line_{dataset_tag}.png" if save_plots else None
    bar_path = config.RESULTS_DIR / f"rf_bar_{dataset_tag}.png" if save_plots else None
    pie_path = config.RESULTS_DIR / f"rf_pie_{dataset_tag}.png" if save_plots else None

    # Visualizations
    plot_line_graph(avg_prices, model_name="Random Forest", save_path=line_path, show=show_plots)
    plot_bar_graph(avg_prices, model_name="Random Forest", save_path=bar_path, show=show_plots)
    plot_pie_chart(avg_prices, model_name="Random Forest", save_path=pie_path, show=show_plots)

    if save_plots:
        print(f"💾 Plots saved to {config.RESULTS_DIR}")

    return {
        "model": model,
        "metrics": metrics,
        "avg_prices": avg_prices,
        "data": data
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Random Forest Regressor on Agricultural Price Data")
    parser.add_argument("--dataset", type=str, default="babin",
                        help="Dataset key (babin, liza, ritika, master, all) or custom CSV path")
    parser.add_argument("--save", action="store_true", default=True, help="Save visualization plots to results/ (default: True)")
    parser.add_argument("--show", action="store_true", default=False, help="Display interactive pop-up windows (default: False, saves to results/ only)")
    parser.add_argument("--no-show", action="store_true", help="Explicitly suppress interactive windows (default)")

    args = parser.parse_args()
    show_plots = args.show and not args.no_show
    run_random_forest(dataset_name=args.dataset, save_plots=args.save, show_plots=show_plots)
