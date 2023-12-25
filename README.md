# Taxi Demand Predictor
![Frontend](ss.png)
# Taxi Demand Prediction App

This repository contains the source code for a Streamlit-based web application designed for predicting taxi demand in New York City. The application utilizes various Python libraries and custom modules to analyze and visualize taxi demand based on historical data and predictive models.

## Overview

The application primarily focuses on predicting taxi demand in NYC. It uses historical data to forecast demand in different zones of the city. The prediction model is built using a set of features derived from past taxi rides, and the predictions are visualized on an interactive map.

## Features

- **Real-time Data Processing**: Utilizes current date and time to process and visualize data.
- **Interactive NYC Map**: Visualizes taxi demand predictions across different NYC zones.
- **Predictive Modeling**: Uses machine learning models to predict taxi demand.
- **Data Visualization**: Provides a graphical representation of taxi demand.

## Requirements

- Python 3.6+
- Streamlit
- Pandas
- Numpy
- Requests
- GeoPandas
- PyDeck

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:


## Usage

To run the Streamlit application:
1. Navigate to the project directory.
2. Execute the following command:


## Application Structure

- `src/`: Contains the source code for the application.
- `inference.py`: Functions for model loading and prediction.
- `paths.py`: Defines paths to data directories.
- `plot.py`: Functions for data plotting.

- `app.py`: The main Streamlit application script.

## Data Flow

1. **Shape Data Fetching**: Downloads and processes shape data for NYC taxi zones.
2. **Feature Loading**: Fetches batch of features for the prediction model.
3. **Model Loading**: Loads the predictive model from the registry.
4. **Prediction Generation**: Generates taxi demand predictions.
5. **Data Plotting**: Merges predictions with shape data and plots on NYC map.

## Contributing

Contributions to improve the application are welcome. Please follow the standard Git workflow - fork the repository, make changes, and submit a pull request.

## License

[MIT License](LICENSE)

## Contact

For any inquiries or issues, please open an issue on the GitHub repository.

