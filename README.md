# SpaceX Falcon 9 First Stage Landing Prediction

## Project Overview
This project analyzes SpaceX Falcon 9 launch data to predict the success of first stage landings. Using data science and machine learning techniques, we aim to determine the likelihood of successful rocket landings, which is crucial for understanding launch cost effectiveness.

## Project Components

### 1. Data Collection
- **Data Collection API.ipynb**: Collects SpaceX launch data using the SpaceX API
- **Data Collection web scraping.ipynb**: Web scraping additional launch information

### 2. Data Wrangling
- **Data wrangling.ipynb**: Cleans and prepares the data for analysis
  - Creates binary classification labels (successful/failed landings)
  - Analyzes launch sites, orbits, and landing outcomes
  - Exports cleaned dataset for further analysis

### 3. Exploratory Data Analysis (EDA)
- **EDA with SQL.ipynb**: SQL-based analysis of SpaceX launch data
  - Database setup with SQLite
  - Launch site analysis
  - Payload mass statistics (total, average)
  - Landing outcome analysis (RTLS, ASDS, Ocean)
  - Temporal analysis of landing success rates
  - Comprehensive insights with professional documentation

- **EDA with visualization.ipynb**: Visual analysis of SpaceX launch patterns
  - **7 Key Visualizations:**
    1. Flight Number vs Payload Mass - Success correlation analysis
    2. Flight Number vs Launch Site - Site usage and success over time
    3. Payload Mass vs Launch Site - Site payload capacity analysis
    4. Success Rate by Orbit Type - Orbit difficulty assessment
    5. Flight Number vs Orbit Type - Mission evolution tracking
    6. Payload Mass vs Orbit Type - Orbit payload capacity
    7. Yearly Success Trend - Progressive improvement from 0% (2010) to 85% (2020)
  - **Feature Engineering:**
    - Selected 12 relevant features for ML modeling
    - One-hot encoded categorical variables (Orbit, LaunchSite, LandingPad, Serial)
    - Expanded to 76 features for comprehensive analysis
    - All features standardized to float64 data type
  - Professional markdown documentation throughout
  - Clear, descriptive code comments

- **Interactive Visual Analytics with Folium.ipynb**: **NEW** - Interactive geospatial analysis of SpaceX launch sites
  - **Complete Analysis with 10 Sections:**
    1. Import required libraries (Folium, Pandas, plugins)
    2. Load and prepare SpaceX launch data with data type conversions
    3. Create launch sites summary with unique site coordinates
    4. Basic map creation centered at NASA Johnson Space Center
    5. Visualize all SpaceX launch sites with circles and labels

- **SpaceX Launch Analysis Insights.ipynb**: 📊 Comprehensive insights analysis notebook
  - **Answers 5 Critical Questions:**
    1. Which site has the largest successful launches?
    2. Which site has the highest launch success rate?
    3. Which payload range has the highest launch success rate?
    4. Which payload range has the lowest launch success rate?
    5. Which F9 Booster version has the highest launch success rate?
  - **Professional Notebook Format:**
    - Interactive cells for step-by-step execution
    - Visual formatting with emojis and clear sections
    - Dataset overview and basic statistics
    - Detailed analysis with pandas aggregations
    - Success rate calculations by site, payload range, and booster version
    - Comprehensive summary with key findings and recommendations
  - **Data Analysis Techniques:**
    - Groupby aggregations for multi-level analysis
    - Binning payload mass into ranges for comparison
    - Success rate calculations with percentage formatting
    - Sorting and ranking for identifying top performers
    6. Mark success/failed launches with color-coded markers (Green=Success, Red=Failed)
    7. Proximity analysis with distance calculations to coastlines and cities
    8. Interactive tools (MousePosition plugin for coordinate identification)
    9. Comprehensive analysis and conclusions
    10. Summary statistics by launch site and geographic characteristics
  
  - **7 Interactive Tasks Completed:**
    - Task 1: Create basic Folium map at NASA JSC
    - Task 2: Add markers and circles to NASA JSC location
    - Task 3: Mark all launch sites on map with custom styling
    - Task 4: Color-code launches by success/failure using MarkerCluster
    - Task 5: Calculate distances to geographic features (Haversine formula)
    - Task 6: Add MousePosition plugin for coordinate identification
    - Task 7: Mark and measure distances to nearest cities
  
  - **Key Visualizations:**
    - Launch site locations with popup labels
    - Success/failure marker clustering
    - Distance lines to coastlines (blue polylines)
    - Distance lines to nearest cities (red polylines)
    - Distance markers showing proximity in kilometers
  
  - **Professional Features:**
    - Comprehensive markdown documentation with clear objectives
    - Detailed code comments explaining every operation
    - Haversine formula implementation for accurate distance calculations
    - Custom HTML markers using DivIcon
    - Interactive map tools for exploration
    - Summary statistics with success rates by site

### 4. Datasets
- `spacex_launch_data.csv`: Raw launch data
- `spacex_web_scraped_data.csv`: Web scraped launch data
- `spacex_launch_data_clean.csv`: Cleaned and processed data with classification labels (90 rows × 18 columns)
- `spacex_features.csv`: **NEW** - Engineered features dataset ready for ML model training (90 rows × 76 features)
- `my_data1.db`: SQLite database for SQL analysis

## Key Findings from EDA

### SQL Analysis Insights:
- **Launch Sites**: Three primary launch sites - CCSFS SLC 40, VAFB SLC 4E, and KSC LC 39A
- **Payload Statistics**: 
  - Total ISS mission payload: 68,878.7 kg
  - Average payload per launch: 6,123.55 kg
- **Landing Milestones**: First successful ground landing (RTLS) on 2015-12-22
- **Success Patterns**: Progressive improvement in landing capabilities from 2010-2017

### Visual Analysis Insights:
- **Temporal Improvement**: Landing success rate dramatically improved from 0% (2010-2013) to ~85% (2020)
- **Payload Impact**: Heavier payloads (>10,000 kg) show varying success rates across different orbits

### 5. Interactive Dashboard
- **spacex-dash-app.py**: Professional web dashboard for launch analytics
  - **Framework**: Built with Dash 3.3.0 and Plotly 6.5.0
  - **Features**:
    - 🚀 Launch site dropdown filter (ALL, CCAFS LC-40, CCSFS SLC 40, KSC LC-39A, VAFB SLC-4E)
    - 📊 Dynamic statistics cards (Total Launches, Successful, Success Rate, Avg Payload)
    - 🥧 Success rate pie charts by site with insights
    - 📈 Payload mass range slider (0-10,000 kg) for filtering
    - 🔵 Scatter plot: Payload vs Success correlation (color-coded by booster version)
    - 📊 Bar chart: Success rate by orbit type analysis
    - 📅 Timeline: Cumulative success rate over time
    - 💡 AI-generated insights for each visualization
  - **Design**:
    - Professional light theme with clean color palette
    - Responsive layout (max-width: 1400px, centered)
    - Insights panels beside each chart for context
    - Full-height background with card-based components
  - **Technical Implementation**:
    - 9 callback functions for interactivity
    - Real-time filtering by site and payload range
    - Comprehensive data analysis and visualization
    - Production-ready code with proper structure

## Running the Dashboard

```bash
# Navigate to project directory
cd "SpaceX-Falcon-9-first-stage-Landing-Prediction"

# Activate virtual environment (if needed)
../.venv/Scripts/activate

# Run dashboard
python spacex-dash-app.py

# Access at http://127.0.0.1:8050/
```
- **Launch Site Performance**: CCAFS SLC 40 shows the highest activity with mixed success rates across flight numbers
- **Orbit Difficulty**: LEO and ISS missions show highest success rates, while GTO missions are more challenging
- **Mission Evolution**: Clear shift towards LEO and VLEO missions in recent flights (flight #80+)
- **Technology Advancement**: Significant improvement in landing success after flight #25, indicating refined techniques

### Geographic & Interactive Analysis Insights:
- **Strategic Location**: All launch sites are located near coastlines for safety (failed launches fall into ocean)
- **Site Distribution**: 
  - CCSFS SLC 40: Cape Canaveral, Florida (Atlantic coast) - Latitude: 28.5618, Longitude: -80.5774
  - VAFB SLC 4E: Vandenberg, California (Pacific coast) - Latitude: 34.6321, Longitude: -120.6108
  - KSC LC 39A: Kennedy Space Center, Florida - Latitude: 28.5721, Longitude: -80.6480
- **Coastal Proximity**: Launch sites are strategically positioned within 1-5 km of coastlines
- **City Distance**: Maintains safe distance from populated areas (Cape Canaveral ~5 km, Lompoc ~15 km)
- **Site Clustering**: Interactive map shows clear clustering of launches at primary sites with color-coded success/failure patterns
- **Success Rate by Location**: Visual analysis reveals geographic patterns in landing success across different sites

## Technologies Used
- **Python Libraries**: 
  - Pandas & NumPy for data manipulation
  - Matplotlib & Seaborn for data visualization
  - Scikit-learn for feature engineering
  - Folium for interactive geospatial mapping
  - Folium Plugins (MarkerCluster, MousePosition, DivIcon) for enhanced map features
- **Database**: SQL & SQLite for data querying
- **Geospatial Analysis**: Haversine formula for accurate distance calculations
- **Development**: Jupyter Notebooks for interactive analysis
- **Version Control**: Git & GitHub for code management

## Project Goals
- Predict first stage landing success to estimate launch costs
- Identify factors that contribute to successful landings
- Provide insights for space exploration cost optimization

## Part of IBM Data Science Professional Certificate
This project is part of the Applied Data Science Capstone course in the IBM Data Science Professional Certificate program.
