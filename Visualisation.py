import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
SaleData_df = 'SaleData.csv'  # Replace with your actual path
SaleData_df = pd.read_csv(SaleData_df)

# Convert SaleDate column to datetime type
SaleData_df['SaleDate'] = pd.to_datetime(SaleData_df['SaleDate'])

# Sort data by SaleDate
SaleData_df = SaleData_df.sort_values(by='SaleDate')

# # Create a Line Chart for SaleAmount over time
# plt.figure(figsize=(12, 6))
# plt.plot(SaleData_df['SaleDate'], SaleData_df['SaleAmount'], marker='o', linestyle='-', color='b')
# plt.title('Sales over time')
# plt.xlabel('Sales date')
# plt.ylabel('SaleAmount')
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()










# # Calculate total SaleAmount by PaymentMethod
# payment_method_sales = SaleData_df.groupby('PaymentMethod')['SaleAmount'].sum()

# # Create a Bar Chart for Sales by Payment Method
# plt.figure(figsize=(10, 6))
# payment_method_sales.plot(kind='bar', color='skyblue')
# plt.title('Sales by payment method')
# plt.xlabel('Payment method')
# plt.ylabel('SaleAmount')
# plt.xticks(rotation=45)
# plt.grid(axis='y')
# plt.tight_layout()
# plt.show()










# # Create a Scatter Plot for Quantity and TotalAmount
# plt.figure(figsize=(10, 6))
# plt.scatter(SaleData_df['Quantity'], SaleData_df['TotalAmount'], alpha=0.6, edgecolors='w', color='purple')
# plt.title('Relationship between quantity of products and total amount')
# plt.xlabel('Quantit')
# plt.ylabel('TotalAmount')
# plt.grid(True)
# plt.tight_layout()
# plt.show()









# Calculate the percentage of payment methods
payment_method_counts = SaleData_df['PaymentMethod'].value_counts()
payment_method_percent = payment_method_counts / payment_method_counts.sum() * 100

# Create a Pie Chart for Payment Methods
plt.figure(figsize=(8, 8))
payment_method_percent.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Percentage of payment methods')
plt.ylabel('')
plt.tight_layout()
plt.show()




