# 🚀 SpaceX Falcon 9 First Stage Landing Prediction

## 📋 Overview
Predicting SpaceX Falcon 9 first stage landing success using data science and machine learning. This analysis helps understand factors affecting landing outcomes and estimate launch costs.

---

## 📂 Project Structure

### 1️⃣ Data Collection
| Notebook | Description |
|----------|-------------|
| **Data Collection API.ipynb** | SpaceX API data extraction |
| **Data Collection web scraping.ipynb** | Web scraping launch information |

### 2️⃣ Data Preparation
| Notebook | Description |
|----------|-------------|
| **Data wrangling.ipynb** | Data cleaning, binary classification labels (success/failed) |

### 3️⃣ Exploratory Data Analysis
| Notebook | Key Features |
|----------|--------------|
| **EDA with SQL.ipynb** | Database queries, launch site analysis, payload statistics |
| **EDA with visualization.ipynb** | 7 visualizations, feature engineering (76 features), success trends |
| **Interactive Visual Analytics with Folium.ipynb** | Interactive maps, geospatial analysis, distance calculations |
| **SpaceX Launch Analysis Insights.ipynb** | 5 key questions answered with detailed statistical analysis |

### 4️⃣ Machine Learning Prediction
| Notebook | Description |
|----------|-------------|
| **Prediction ML.ipynb** | Comprehensive ML analysis with 4 algorithms, hyperparameter tuning, and detailed evaluation |

**Models Evaluated:**
- ✅ Logistic Regression (L1/L2 regularization)
- ✅ Support Vector Machine (Linear & RBF kernels)
- ✅ Decision Tree (depth optimization)
- ✅ K-Nearest Neighbors (algorithm comparison)

**Results:**
- Test Accuracy: 83-85% across all models
- Best Models: Decision Tree & SVM
- Comprehensive metrics: Accuracy, Precision, Recall, F1-Score
- Cross-validation scores comparison
- Confusion matrices for all models

### 5️⃣ Interactive Dashboard
| File | Description |
|------|-------------|
| **spacex-dash-app.py** | Professional Dash web app with 9 interactive visualizations |

### 6️⃣ Datasets
- `spacex_launch_data.csv` - Raw data
- `spacex_launch_data_clean.csv` - Cleaned data (92 rows × 18 columns)
- `spacex_features.csv` - ML-ready features (92 rows × 76 columns)
- `spacex_web_scraped_data.csv` - Web scraped data
- `my_data1.db` - SQLite database

---

## 🎯 Key Insights

### 📈 Success Rate Evolution
- **2010-2013**: 0% success rate
- **2020**: ~85% success rate
- Significant improvement after flight #25

### 🏆 Best Performers
- **Highest Success Site**: KSC LC-39A
- **Most Active Site**: CCAFS SLC 40
- **Best Orbit**: LEO/ISS missions
- **Challenging Orbit**: GTO missions

### 🗺️ Geographic Findings
- All sites located near coastlines (safety)
- CCAFS SLC 40: Cape Canaveral, FL (28.56°N, 80.58°W)
- VAFB SLC 4E: Vandenberg, CA (34.63°N, 120.61°W)
- KSC LC 39A: Kennedy Space Center, FL (28.57°N, 80.65°W)

### 📦 Payload Analysis
- Average payload: 6,123 kg
- Heavier payloads (>10,000 kg) show variable success
- Optimal payload ranges identified

### 🤖 Machine Learning Results
- **Best Accuracy**: 83-85% for landing prediction
- **Top Models**: Decision Tree & SVM
- **Key Features**: Launch site, orbit type, payload mass, reusability components (grid fins, legs)
- **Business Impact**: $50-60M cost savings per successful landing can be forecasted with high confidence

---

## 🖥️ Interactive Dashboard Features

**Run the dashboard:**
```bash
cd SpaceX-Falcon-9-first-stage-Landing-Prediction
python spacex-dash-app.py
# Open http://127.0.0.1:8050/
```

**Dashboard includes:**
- 🎯 Launch site dropdown filter
- 📊 Dynamic statistics cards (Total, Success Rate, Avg Payload)
- 🥧 Success rate pie charts with AI insights
- 📈 Payload vs Success scatter plots
- 🛰️ Orbit type analysis
- 📅 Timeline visualization
- 💡 Real-time insights generation

---

## 🛠️ Technologies Used

**Languages & Tools:**
- Python 3.12 | Pandas | NumPy | Scikit-learn
- SQL & SQLite
- Dash 3.3.0 & Plotly 6.5.0
- Folium (interactive maps)
- Jupyter Notebooks

**Analysis Methods:**
- Statistical analysis & aggregations
- Feature engineering (one-hot encoding, standardization)
- Geospatial analysis (Haversine formula)
- Machine Learning (GridSearchCV, cross-validation)
- Data visualization & interactive dashboards

**ML Techniques:**
- GridSearchCV for hyperparameter optimization
- 10-fold cross-validation
- StandardScaler for feature normalization
- Classification metrics (confusion matrix, precision, recall, F1)

---

## 📊 Analysis Notebooks Summary

### SpaceX Launch Analysis Insights
**Answers 5 Critical Questions:**
1. Which site has the most successful launches?
2. Which site has the highest success rate?
3. Which payload range performs best/worst?
4. Which F9 Booster version is most reliable?
5. What are the key success factors?

### Folium Interactive Analysis
**7 Interactive Tasks:**
- NASA JSC location mapping
- Launch site markers & circles
- Success/failure color coding
- Distance calculations (coastlines, cities)
- Mouse position coordinates
- Proximity analysis
- Geographic pattern identification

### Prediction ML Notebook
**Complete ML Pipeline:**
1. 📦 Data loading & preprocessing (90 launches, 76+ features)
2. 🎯 Train-test split (80/20)
3. 🔧 Hyperparameter tuning with GridSearchCV
4. 📊 Model comparison (4 algorithms)
5. 📈 Comprehensive evaluation metrics
6. 🎨 Professional visualizations (confusion matrices, bar charts)
7. 💡 Business insights & recommendations

---
## 📌 Quick Start

1. **Clone repository**
   ```bash
   git clone https://github.com/visurarodrigo/SpaceX-Falcon-9-first-stage-Landing-Prediction.git
   cd SpaceX-Falcon-9-first:
     1. Data Collection (API & Web Scraping)
     2. Data Wrangling
     3. EDA (SQL & Visualization)
     4. Prediction ML (Machine LearningLanding-Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly dash folium scikit-learn
   ```

3. **Run notebooks**
   - Open Jupyter: `jupyter notebook`
   - Run notebooks in order (1→2→3)

4. **Launch dashboard**
   ```bash
   python spacex-dash-app.py
   ```

---

## 🎓 IBM Data Science Professional Certificate
This project is part of IBM Data Science Professional Certificate coursework.

## 👤 Author
Visura Rodrigo
