# Base Idea:
- Gather historical stock price data for a selection of NASDAQ-listed stocks and use data mining techniques to analyze and predict stock price movements utilizing specific features, leading to an analysis of how much each feature influences the prediction and how quickly the market adjusts and renders the prediction no longer accurate.

# Data:
## Data Collection:
- Gather historical stock price data for a selection of NASDAQ-listed stocks using APIs provided by financial data providers like Alpha Vantage, Finazon, IEX Cloud, and Twelve Data.
## Data Preprocessing:
- Clean the data by handling missing values, outliers, and formatting issues.
- Calculate additional features such as moving averages, relative strength index (RSI), and other technical indicators that can be used as inputs for the model.
- Select features from 101 Alpha.
## Data Exploration and Visualization:
- Explore the data to understand the distribution of stock prices, trading volume, and other variables.
- Visualize the data to identify patterns and trends.

# Model:
## Model Creation:
- Build an ensemble model consisting of (potentially, needs further exploration) time series models (e.g., ARIMA, LSTM) and machine learning models (e.g., Random Forest, XGBoost).
- Split the data into training and test sets.
- Train and tune the model on data from a rather short period of time.
## Feature Analysis:
- Run feature importance analysis, and see which features yield a significant influence on the prediction.
- Use the trained model to make predictions on future stock prices.
- Analyze the predictions to identify potential trading opportunities and assess the performance of the model.
- Analyze residue with data from the timeframe following the training data, and see how much and how quickly the accuracy drops as time goes on.
## Model Evaluation:
- Evaluate the model using MSE/RMSE.
- Compare the model's performance against a baseline model or a simple benchmark.
## Reporting and Visualization:
- Present the results of the analysis with visualizations and summary statistics.
- Insights and recommendations based on the analysis.
