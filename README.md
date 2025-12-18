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

### 3. Datasets
- `spacex_launch_data.csv`: Raw launch data
- `spacex_web_scraped_data.csv`: Web scraped launch data
- `spacex_launch_data_clean.csv`: Cleaned and processed data with classification labels

## Technologies Used
- Python
- Pandas & NumPy for data manipulation
- Jupyter Notebooks for interactive analysis

## Project Goals
- Predict first stage landing success to estimate launch costs
- Identify factors that contribute to successful landings
- Provide insights for space exploration cost optimization

## Part of IBM Data Science Professional Certificate
This project is part of the Applied Data Science Capstone course in the IBM Data Science Professional Certificate program.
