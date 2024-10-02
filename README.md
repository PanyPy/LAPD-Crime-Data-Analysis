# LAPD Crime Data Analysis

This repository contains code and resources for developing a predictive model to estimate the probability of crimes occurring in various districts of Los Angeles.

## Repository Structure
1. **`data/`**: Contains datasets needed for training and evaluating the model. These include historical crime data, demographic information, and geographic variables that influence crime patterns. This data will be downloaded once you run the notebook.
   - `crime_data`: Historical crime data, including variables such as crime type, location, date, and time.
   - `demographic_data`: Demographic data from Los Angeles districts, useful for identifying correlations between socioeconomic factors and crime rates.

2. **`main.ipynb`**: The main Jupyter notebook used for data exploration, exploratory data analysis (EDA), and model development. It includes all the necessary steps to analyze crime data and develop predictive models.

- **Future improvements**: Add the following folders:
  - **`src/`**: Source code for the predictive model.
    - Functions for data preprocessing, model training, and evaluation.
  - **`models/`**: Stores trained models for use in predictions.
    - A trained model for predicting crime probabilities based on historical data.
  - **`output/`**: Contains prediction results such as heatmaps and reports.
    - Visualizations of areas with the highest crime probability.

## Technologies Used
- **Python**: For data cleaning, exploratory analysis, and model development.
- **Pandas and NumPy**: For data manipulation and analysis.
- **Scikit-learn**: For developing machine learning models.
- **Folium**: For visualizing crime heatmaps.
- **GeoPandas**: For handling geospatial data.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/panypy/LAPD-Crime-Data-Analysis.git
   cd LAPD-Crime-Data-Analysis
2. Run the `main` notebook:
  It  contains the instructions to download the required packages and data.
3. Follow the instructions within the notebook to conduct the analysis and visualize the results.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
