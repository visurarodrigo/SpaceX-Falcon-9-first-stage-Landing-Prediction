# SpaceX Falcon 9 First Stage Landing Prediction

## Overview
This project predicts Falcon 9 first-stage landing success using historical launch data, exploratory analysis, and machine learning.

The work combines:
- Data collection from API and web sources
- Data wrangling and feature engineering
- Exploratory analysis (SQL, visualization, geospatial)
- Classification modeling and comparison
- An interactive Dash dashboard

## Project Structure

### Data Collection
| Notebook | Description |
|----------|-------------|
| Data Collection API.ipynb | Extracts launch data from the SpaceX API |
| Data Collection web scraping.ipynb | Collects additional launch details by web scraping |

### Data Preparation
| Notebook | Description |
|----------|-------------|
| Data wrangling.ipynb | Cleans data and creates binary landing labels |

### Exploratory Data Analysis
| Notebook | Description |
|----------|-------------|
| EDA with SQL.ipynb | SQL-based launch site, payload, and mission analysis |
| EDA with visualization.ipynb | Visual EDA and trend analysis with engineered features |
| Interactive Visual Analytics with Folium.ipynb | Geospatial analysis, maps, and distance calculations |
| SpaceX Launch Analysis Insights.ipynb | Consolidated business and technical insights |

### Machine Learning
| Notebook | Description |
|----------|-------------|
| Prediction ML.ipynb | End-to-end model training, tuning, and evaluation |

### Dashboard
| File | Description |
|------|-------------|
| src/spacex-dash-app.py | Dash app with interactive launch and payload analytics |

### Data Files
- data/raw/spacex_launch_data.csv: Raw launch data
- data/raw/spacex_web_scraped_data.csv: Web-scraped launch data
- data/processed/spacex_launch_data_clean.csv: Cleaned dataset (92 rows x 18 columns)
- data/processed/spacex_features.csv: ML feature set (92 rows x 76 columns)

## Key Insights

### Landing Success Trend
- 2010-2013: near 0% success rate
- 2020: approximately 85% success rate
- Marked improvement after approximately flight 25

### Site and Orbit Performance
- Highest success site: KSC LC-39A
- Most active site: CCAFS SLC 40
- Stronger outcomes: LEO/ISS missions
- More challenging outcomes: GTO missions

### Payload and Geography
- Average payload mass: 6,123 kg
- Very high payloads (>10,000 kg) show more variable outcomes
- Launch sites are near coastlines, supporting range safety and operations

### Business Value
- Model accuracy is in the 83-85% range
- Best-performing models: Decision Tree and SVM
- Successful first-stage recovery can represent approximately $50M-$60M in savings per launch

## Machine Learning Summary

### Models Evaluated
- Logistic Regression (L1/L2 regularization)
- Support Vector Machine (linear and RBF kernels)
- Decision Tree (depth tuning)
- K-Nearest Neighbors

### Evaluation Approach
- Train/test split: 80/20
- Hyperparameter tuning: GridSearchCV
- Cross-validation: 10-fold
- Metrics: accuracy, precision, recall, F1-score, confusion matrix

## Dashboard Features
The Dash app includes:
- Launch site filtering
- Success-rate visualizations
- Payload-versus-outcome scatter analysis
- Orbit-level summaries
- Timeline and trend views

Run the dashboard:

```bash
python src/spacex-dash-app.py
```

Then open: http://127.0.0.1:8050/

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/visurarodrigo/SpaceX-Falcon-9-first-stage-Landing-Prediction.git
cd SpaceX-Falcon-9-first-stage-Landing-Prediction
```

2. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn plotly dash folium scikit-learn
```

3. Open Jupyter and run notebooks in workflow order:

```bash
jupyter notebook
```

Suggested order:
1. Data Collection API.ipynb
2. Data Collection web scraping.ipynb
3. Data wrangling.ipynb
4. EDA with SQL.ipynb
5. EDA with visualization.ipynb
6. Interactive Visual Analytics with Folium.ipynb
7. Prediction ML.ipynb
8. SpaceX Launch Analysis Insights.ipynb

4. Launch the dashboard:

```bash
python src/spacex-dash-app.py
```

## Technologies Used
- Python 3.x
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- Plotly, Dash
- Folium
- SQLite and SQL
- Jupyter Notebook

## Program Context
This project is part of the IBM Data Science Professional Certificate capstone.

## Author
Visura Rodrigo
