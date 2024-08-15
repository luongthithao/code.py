import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime

SaleData_df = pd.read_csv('SaleData_Cleaned_df.csv')
SaleData_df['SaleDate'] = pd.to_datetime(SaleData_df['SaleDate'])
time_series_data = SaleData_df.groupby(SaleData_df['SaleDate'].dt.date).agg({'TotalAmount': 'sum'}).reset_index()
time_series_data['Days'] = (pd.to_datetime(time_series_data['SaleDate']) - pd.to_datetime(time_series_data['SaleDate'].min())).dt.days
X = time_series_data[['Days']]
y = time_series_data['TotalAmount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.figure(figsize=(12, 6))
plt.plot(time_series_data['SaleDate'], y, label='Actual Sales', marker='o')
plt.plot(time_series_data.iloc[X_test.index]['SaleDate'], y_pred, label='Predicted Sales', marker='x')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

future_days = np.array([(datetime(2024, 12, 31) - pd.to_datetime(time_series_data['SaleDate'].min())).days]).reshape(-1, 1)
future_sales = model.predict(future_days)
print(f"Predicted Sales on 2024-12-31: {future_sales[0]}")



