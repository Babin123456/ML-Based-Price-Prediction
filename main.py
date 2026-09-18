"""
Agricultural Commodity Price Prediction - Main Execution Pipeline.
Executes Random Forest and SVM models, generates performance comparisons, and saves results.
"""

import sys
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import config
from models.random_forest import run_random_forest
from models.svm import run_svm


def compare_models(rf_eval, svm_eval, dataset_name: str, save_plots: bool = True, show_plots: bool = True):
    """Generates comparison bar chart and summary table between Random Forest and SVM."""
    rf_metrics = rf_eval["metrics"]
    svm_metrics = svm_eval["metrics"]

    summary_df = pd.DataFrame([
        {"Model": "Random Forest", "R² Score": rf_metrics["R2"], "MAE (₹)": rf_metrics["MAE"], "RMSE (₹)": rf_metrics["RMSE"]},
        {"Model": "Support Vector Machine (SVM)", "R² Score": svm_metrics["R2"], "MAE (₹)": svm_metrics["MAE"], "RMSE (₹)": svm_metrics["RMSE"]}
    ])

    print("\n" + "=" * 65)
    print(f"🏆 MODEL PERFORMANCE COMPARISON ({dataset_name.upper()} DATASET)")
    print("=" * 65)
    print(summary_df.to_string(index=False))
    print("=" * 65 + "\n")

    # Comparative Plot
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=300)
    metrics_to_plot = [
        ("R² Score", "R² Score (Higher is Better)", "{:.4f}"),
        ("MAE (₹)", "Mean Absolute Error (₹) (Lower is Better)", "₹{:.2f}"),
        ("RMSE (₹)", "Root Mean Squared Error (₹) (Lower is Better)", "₹{:.2f}")
    ]

    model_colors = {"Random Forest": "#2A9D8F", "Support Vector Machine (SVM)": "#457B9D"}

    for ax, (col, title, fmt) in zip(axes, metrics_to_plot):
        bars = ax.bar(summary_df["Model"], summary_df[col],
                      color=[model_colors[m] for m in summary_df["Model"]],
                      width=0.45, edgecolor='#1F2937', linewidth=0.8, zorder=3)
        ax.set_title(title, fontsize=11, fontweight='bold', pad=12, color='#111827')
        ax.set_xlabel("")
        ax.set_ylabel(col, fontsize=10, fontweight='semibold')
        ax.grid(axis='y', linestyle='--', alpha=0.35, color='#9CA3AF', zorder=1)
        ax.set_axisbelow(True)

        # Set headroom
        max_val = summary_df[col].max()
        ax.set_ylim(0, max_val * 1.25 if max_val > 0 else 1)

        for bar in bars:
            height = bar.get_height()
            ax.annotate(fmt.format(height),
                        (bar.get_x() + bar.get_width() / 2., height + max_val * 0.02),
                        ha='center', va='bottom', fontsize=10, fontweight='bold', color='#111827')

    plt.suptitle(f"Model Performance Benchmark: Random Forest vs SVM ({dataset_name.title()} Data)",
                 fontsize=13, fontweight='bold', y=1.02, color='#111827')
    plt.tight_layout()

    if save_plots:
        dataset_tag = Path(dataset_name).stem.replace(" ", "_").lower()
        for member in ["babin", "liza", "ritika"]:
            if member in dataset_tag:
                dataset_tag = member
                break
        comp_path = config.RESULTS_DIR / f"model_comparison_{dataset_tag}.png"
        plt.savefig(comp_path, dpi=300, bbox_inches='tight')
        print(f"💾 Comparison plot saved to: {comp_path}")

    if show_plots:
        plt.show()
    else:
        plt.close(fig)

    return summary_df


def compare_all_datasets(all_results, save_plots: bool = True, show_plots: bool = False):
    """Generates cross-dataset comparison bar chart and master summary table across all seasons."""
    rows = []
    chart_labels = []
    for ds_name, res in all_results.items():
        rf_m = res["rf"]["metrics"]
        svm_m = res["svm"]["metrics"]
        info = config.SEASON_INFO.get(ds_name.lower(), {})
        season_title = f"{info.get('name', ds_name.capitalize())} ({info.get('season', 'General')} Season)" if info else ds_name.capitalize()
        c_label = f"{info.get('name', ds_name.capitalize())}\n({info.get('season', '')})" if info else ds_name.capitalize()
        chart_labels.append(c_label)
        rows.append({"Dataset / Season": season_title, "Model": "Random Forest", "R² Score": rf_m["R2"], "MAE (₹)": rf_m["MAE"], "RMSE (₹)": rf_m["RMSE"]})
        rows.append({"Dataset / Season": season_title, "Model": "Support Vector Machine (SVM)", "R² Score": svm_m["R2"], "MAE (₹)": svm_m["MAE"], "RMSE (₹)": svm_m["RMSE"]})

    master_df = pd.DataFrame(rows)

    print("\n" + "=" * 90)
    print("🏆 MASTER MULTI-SEASON BENCHMARK SUMMARY (WINTER, MONSOON & SUMMER)")
    print("=" * 90)
    print(master_df.to_string(index=False))
    print("=" * 90 + "\n")

    # Multi-dataset comparative grouped bar chart
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), dpi=300)
    metrics_info = [
        ("R² Score", "R² Score (Higher is Better)", "{:.4f}"),
        ("MAE (₹)", "Mean Absolute Error (₹) (Lower is Better)", "₹{:.1f}"),
        ("RMSE (₹)", "Root Mean Squared Error (₹) (Lower is Better)", "₹{:.1f}")
    ]

    datasets_keys = list(all_results.keys())
    x = np.arange(len(datasets_keys))
    width = 0.35

    rf_color = "#2A9D8F"
    svm_color = "#457B9D"

    for ax, (col, title, fmt) in zip(axes, metrics_info):
        rf_vals = [master_df[(master_df["Dataset / Season"].str.contains(d, case=False)) & (master_df["Model"] == "Random Forest")][col].values[0] for d in datasets_keys]
        svm_vals = [master_df[(master_df["Dataset / Season"].str.contains(d, case=False)) & (master_df["Model"] == "Support Vector Machine (SVM)")][col].values[0] for d in datasets_keys]

        bars1 = ax.bar(x - width / 2, rf_vals, width, label="Random Forest", color=rf_color,
                       edgecolor='#1F2937', linewidth=0.7, zorder=3)
        bars2 = ax.bar(x + width / 2, svm_vals, width, label="SVM", color=svm_color,
                       edgecolor='#1F2937', linewidth=0.7, zorder=3)

        ax.set_title(title, fontsize=11, fontweight='bold', pad=12, color='#111827')
        ax.set_xticks(x)
        ax.set_xticklabels(chart_labels, fontsize=10, fontweight='semibold')
        ax.set_ylabel(col, fontsize=10, fontweight='semibold')
        ax.grid(axis='y', linestyle='--', alpha=0.35, color='#9CA3AF', zorder=1)
        ax.set_axisbelow(True)

        max_val = max(max(rf_vals), max(svm_vals))
        ax.set_ylim(0, max_val * 1.25 if max_val > 0 else 1)

        for bar in list(bars1) + list(bars2):
            h = bar.get_height()
            ax.annotate(fmt.format(h),
                        (bar.get_x() + bar.get_width() / 2., h + max_val * 0.02),
                        ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111827')

        ax.legend(frameon=True, facecolor='white', framealpha=0.95, edgecolor='#E5E7EB', fontsize=9)

    plt.suptitle("Master Seasonal Benchmark: Random Forest vs SVM Across Winter, Monsoon & Summer",
                 fontsize=13, fontweight='bold', y=1.02, color='#111827')
    plt.tight_layout()

    if save_plots:
        comp_path = config.RESULTS_DIR / "master_comparison_all.png"
        plt.savefig(comp_path, dpi=300, bbox_inches='tight')
        print(f"💾 Master multi-dataset comparison plot saved to: {comp_path}")

    if show_plots:
        plt.show()
    else:
        plt.close(fig)

    return master_df


def run_pipeline_for_dataset(dataset_key_or_path: str, selected_model: str, save_plots: bool, show_plots: bool):
    """Executes model training and evaluation for a single dataset."""
    dataset_path = config.get_dataset_path(dataset_key_or_path)
    try:
        rel_dataset = dataset_path.relative_to(config.BASE_DIR)
    except ValueError:
        rel_dataset = dataset_path

    tag = Path(dataset_key_or_path).stem.replace(" ", "_").lower()
    for member in ["babin", "liza", "ritika"]:
        if member in tag:
            tag = member
            break

    info = config.SEASON_INFO.get(tag, {})
    season_text = f" - {info['season']} Season ({info['desc']})" if info else ""
    tag_clean = info.get('name', tag.capitalize()) if info else tag.capitalize()

    print("\n" + "=" * 70)
    print(f"📂 Processing: {tag_clean}{season_text}")
    print(f"📁 Source File: {rel_dataset}")
    print("=" * 70)

    rf_eval = None
    svm_eval = None

    if selected_model in ["rf", "all"]:
        rf_eval = run_random_forest(dataset_name=str(rel_dataset), save_plots=save_plots, show_plots=show_plots)

    if selected_model in ["svm", "all"]:
        svm_eval = run_svm(dataset_name=str(rel_dataset), save_plots=save_plots, show_plots=show_plots)

    if selected_model == "all" and rf_eval and svm_eval:
        compare_models(rf_eval, svm_eval, dataset_name=tag, save_plots=save_plots, show_plots=show_plots)

    return {"rf": rf_eval, "svm": svm_eval, "rel_path": rel_dataset}


def main():
    parser = argparse.ArgumentParser(
        description="Agricultural Commodity Price Prediction Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                              # Run complete pipeline on all team datasets
  python main.py --dataset babin              # Run on Babin's dataset only
  python main.py --dataset liza               # Run on Liza's dataset only
  python main.py --dataset ritika             # Run on Ritika's dataset only
  python main.py --model rf --dataset babin   # Run only Random Forest on Babin
  python main.py --model svm --dataset liza   # Run only SVM on Liza
  python main.py --show                       # Display interactive matplotlib popups
        """
    )
    parser.add_argument(
        "--model", type=str, default="all",
        help="Model to execute: 'rf' (Random Forest), 'svm' (SVR), or 'all' (default: 'all')"
    )
    parser.add_argument(
        "--dataset", type=str, default=config.DEFAULT_DATASET,
        help="Dataset choice: 'all' (all team datasets), 'babin', 'liza', 'ritika', 'master', or CSV path (default: 'all')"
    )
    parser.add_argument(
        "--save", action="store_true", default=True,
        help="Save generated figures to results/ (default: True)"
    )
    parser.add_argument(
        "--show", action="store_true", default=False,
        help="Display interactive matplotlib pop-up windows (default: False, saves to results/ only)"
    )
    parser.add_argument(
        "--no-show", action="store_true",
        help="Explicitly suppress interactive matplotlib windows (default)"
    )

    args = parser.parse_args()
    show_plots = args.show and not args.no_show

    # Resolve model input flexibly
    model_choice = args.model.lower().strip()
    if model_choice in ["rf", "random_forest", "random-forest", "forest"]:
        selected_model = "rf"
    elif model_choice in ["svm", "svr", "support_vector_machine"]:
        selected_model = "svm"
    else:
        selected_model = "all"

    is_all_datasets = args.dataset.lower() in ["all", "team", "full"]
    target_datasets = config.TEAM_DATASETS if is_all_datasets else [args.dataset]

    print("\n🌱 Starting Agricultural Price Prediction Pipeline...")
    if is_all_datasets:
        print("• Target Seasons:   Winter (Babin), Monsoon (Liza), Summer (Ritika)")
    else:
        info = config.SEASON_INFO.get(args.dataset.lower(), {})
        season_label = f" ({info['season']} Season)" if info else ""
        print(f"• Target Dataset:   {args.dataset}{season_label}")
    print(f"• Selected Model:   {'Both (RF + SVM Comparison)' if selected_model == 'all' else selected_model.upper()}")
    print(f"• Target Variable:  {config.TARGET}")
    print(f"• Output Mode:      Headless saving (all figures saved to 'results/', no popup windows)")

    all_results = {}
    for ds in target_datasets:
        res = run_pipeline_for_dataset(
            dataset_key_or_path=ds,
            selected_model=selected_model,
            save_plots=args.save,
            show_plots=show_plots
        )
        all_results[ds] = res

    # If all datasets were evaluated with both models, generate comprehensive multi-dataset benchmark
    if is_all_datasets and selected_model == "all":
        compare_all_datasets(all_results, save_plots=args.save, show_plots=show_plots)

    print("\n✅ Execution completed successfully! All charts are saved under the 'results/' folder.")


if __name__ == "__main__":
    main()
