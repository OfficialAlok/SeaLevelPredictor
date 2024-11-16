# Sea Level Predictor

## Overview
The Sea Level Predictor project aims to analyze global average sea level changes since 1880 and predict future sea level changes through the year 2050. Using a dataset of historical sea level measurements, we employ linear regression to model sea level rise and visualize both historical data and future predictions.

## Features
- **Data Import**: Load sea level data from a CSV file using Pandas.
- **Data Cleaning**: Filter and clean the data to remove outliers for more accurate analysis.
- **Linear Regression**: Use the linregress function from scipy.stats to create lines of best fit.
- **Visualization**: Create scatter plots with lines of best fit to illustrate sea level trends.
- **Future Predictions**: Extend regression models to predict sea levels up to the year 2050.

## Usage
1. **Import Data:** Load the dataset from "epa-sea-level.csv".
2. **Clean Data:** Filter out outliers to improve the accuracy of the analysis.
3. **Generate Visualizations:** Use the provided functions to create scatter plots with regression lines.

## Visualization
- Blue Points: Historical sea level data.
- Green Line: Line of best fit for all data.
- Red Line: Line of best fit for data from the year 2000 onwards.

## Analysis Result
![level plot](https://github.com/OfficialAlok/SeaLevelPredictor/blob/main/sea_level_plot.png?raw=true)
