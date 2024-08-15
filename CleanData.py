import pandas as pd
CustomerData_df = pd.read_csv('CustomerData.csv')
MarketTrendData_df = pd.read_csv('MarketTrendData.csv')
ProductDetailData_df = pd.read_csv('ProductDetailData.csv')
ProductGroupData_df = pd.read_csv('ProductGroupData.csv')
SaleData_df = pd.read_csv('SaleData.csv')
websiteaccesscategory_df = pd.read_csv('websiteaccesscategory.csv')

import pandas as pd
# Load data
CustomerData_df = pd.read_csv('CustomerData.csv')
MarketTrendData_df = pd.read_csv('MarketTrendData.csv')
ProductDetailData_df = pd.read_csv('ProductDetailData.csv')
ProductGroupData_df = pd.read_csv('ProductGroupData.csv')
SaleData_df = pd.read_csv('SaleData.csv')
websiteaccesscategory_df = pd.read_csv('websiteaccesscategory.csv')

# # Display the first few rows of each DataFrame

# print(Customer_Data_df.head())
# print(MarketTrend_Data_df.head())
# print(ProductDetail_Data_df.head())
# print(ProductGroup_Data_df.head())
# print(Sale_Data_df.head())
# print(website_access_category_df.head())    

# # check data type

# print(Customer_Data_df.dtypes)
# print(MarketTrend_Data_df.dtypes)
# print(ProductDetail_Data_df.dtypes)
# print(ProductGroup_Data_df.dtypes)
# print(Sale_Data_df.dtypes)
# print(website_access_category_df.head())

# # Data clearing

# # Remove (drop) Gender in CustomterData
# Customer_Data_df = Customer_Data_df.drop('Gender', axis=1)

# # Handle Missing Values in CustomterData
# Customer_Data_df = Customer_Data_df.fillna('Null')
# # or
# new_df = Customer_Data_df.dropna()
# # or
# Customer_Data_df.dropna(inplace = True)

# # Check Date in Sale, Market trends and website_access_category_df
# Sale_Data_df['Sale_Date'] = pd.to_datetime(Sale_Data_df['Sale_Date'])
# MarketTrend_Data_df['Date'] = pd.to_datetime(MarketTrend_Data_df['Date'])
# website_access_category_df['VisitDate'] = pd.to_datetime(website_access_category_df['VisitDate'])

# # Remove spaces in MarketTrendData and Sale_Data
# MarketTrend_Data_df['TrendDescription'] = MarketTrend_Data_df['TrendDescription'].str.strip()
# Sale_Data_df['SaleAmount'] = Sale_Data_df['SaleAmount'].str.strip()

# # Convert pandas object 
# Customer_Data_df['Purchase quantity'] = Customer_Data_df['Purchase quantity'].astype(int)
# ProductDetail_Data_df['ProductGroupID'] = ProductDetail_Data_df['ProductGroupID'].astype(int)
# website_access_category_df['SessionDuration'] = website_access_category_df['SessionDuration'].astype(int)

# Save Data Cleaned 
CustomerData_df.to_csv('CustomerData_Cleaned_df.csv', index=False)
MarketTrendData_df.to_csv('MarketTrendData_Cleaned_df.csv', index=False)
ProductDetailData_df.to_csv('ProductDetailData_Cleaned_df.csv', index=False)
ProductGroupData_df.to_csv('ProductGroupData_Cleaned_df.csv', index=False)
SaleData_df.to_csv('SaleData_Cleaned_df.csv', index=False)
websiteaccesscategory_df.to_csv('websiteaccesscategory_Cleaned_df.csv', index=False)