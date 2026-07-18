# Employee Data Cleaning & Preprocessing Pipeline

A Python data engineering project designed to identify, isolate, and fix severe structural data anomalies in a mock corporate human resource file (`employee_data.csv`). This project serves as a practical application of data cleaning methodologies using **Pandas** and **NumPy**.

## 📊 Identified Data Issues Resolved
The raw input dataset contains several deliberate data corruption scenarios to test algorithmic handling:
- **Duplicate Records**: Multiple duplicate entries tracking identical worker primary keys.
- **Missing Observations (`NaN`)**: Absent fields across quantitative attributes (`Salary`, `Performance Rating`).
- **Mathematical Infinites (`inf`)**: Division-by-zero or system exceptions inserting infinite bounds into mathematical vectors.
- **Signage Failures**: Non-logical negative numerical figures in operational tracking.
- **Statistical Outliers**: Disproportionately high or low salaries lying beyond bounds.

## 🛠️ Cleaning Operations Pipeline
The cleaning pipeline script (`data_clean.py`) processes structural data validation sequentially:
1. **Vector Conversion**: Translates positive/negative infinite indicators into standardized `NaN` flags.
2. **Anomaly Isolation**: Neutralizes operational anomalies (e.g., negative metrics) by dropping or zeroing them out before running aggregation metrics.
3. **Statistical Imputation**: Replaces missing variables with reliable column metrics (Mean for uniform arrays, Median for skewed ratings).
4. **Deduplication**: Purges overlapping registry rows to establish precise data records.
5. **Outlier Filtering**: Drops rows containing metrics skewed beyond ±3 Standard Deviations from the clean population mean.

## 🚀 Getting Started

### Prerequisites
Ensure your current virtual environment features modern data pipeline libraries:
```bash
pip install pandas numpy
```

### Execution
Run the core processing script to convert your raw data source into the sanitized export file:
```bash
python data_clean.py
```

## 📂 Project Tree Structure
```text
├── employee_data.csv          # Raw data input filled with structural anomalies
├── data_clean.py              # Automated data cleaning processing script
├── Cleaned_Employee_Data.csv  # Output dataset verified for pipeline consumption
└── README.md                  # System design description
```
