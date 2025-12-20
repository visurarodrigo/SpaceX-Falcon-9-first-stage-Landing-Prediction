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

### 4️⃣ Interactive Dashboard
| File | Description |
|------|-------------|
| **spacex-dash-app.py** | Professional Dash web app with 9 interactive visualizations |

### 5️⃣ Datasets
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
- Feature engineering (one-hot encoding)
- Geospatial analysis (Haversine formula)
- Data visualization & interactive dashboards

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

---

## 🎓 IBM Data Science Professional Certificate
Applied Data Science Capstone Project

---

## 📌 Quick Start

1. **Clone repository**
   ```bash
   git clone https://github.com/visurarodrigo/SpaceX-Falcon-9-first-stage-Landing-Prediction.git
   cd SpaceX-Falcon-9-first-stage-Landing-Prediction
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

## 📄 License
This project is part of IBM Data Science Professional Certificate coursework.

## 👤 Author
Visura Rodrigo
