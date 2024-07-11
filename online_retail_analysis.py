import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

cus_data=pd.read_excel("online_retail_II.xlsx",sheet_name="Year 2010-2011")

# Check Missing Data
missing_values = cus_data.isnull().sum()

# Remove Missing Values
cus_data_2=cus_data.copy()
cus_data_2.dropna(inplace = True)
cus_data_2.shape

# Summary Stats
cus_data_2.describe() #there is negative value in "Quantity"
cus_data_2 = cus_data_2[cus_data_2["Quantity"] >= 0]

# STEP 1: Assign Recency, Frequency, Monetary values
# Recency
print("2010-2011: Min Date", cus_data_2["InvoiceDate"].min(), "Max Date", cus_data_2["InvoiceDate"].max())
recency1 = (dt.datetime(2011, 12, 9) - cus_data_2.groupby("Customer ID").agg({"InvoiceDate":"max"})).rename(columns = {"InvoiceDate":"Recency"})
recency1["Recency"] = recency1["Recency"].apply(lambda x: x.days)

# Frequency
freq1 = cus_data_2.groupby("Customer ID").agg({"InvoiceDate":"nunique"}).rename(columns={"InvoiceDate": "Frequency"})

# Monetary
cus_data_2["TotalPrice"] = cus_data_2["Quantity"] * cus_data_2["Price"]
monetary1 = cus_data_2.groupby("Customer ID").agg({"TotalPrice":"sum"}).rename(columns={"TotalPrice":"Monetary"})

rfm1 = pd.concat([recency1, freq1, monetary1],  axis=1)
rfm2 = pd.concat([recency1, freq1, monetary1],  axis=1)

# Summary Stats

rfm1.describe()
rfm1.boxplot()
plt.show()
rfm1.boxplot(column=['Recency'])
plt.show()
rfm1.boxplot(column=['Frequency'])
plt.show()
rfm1.boxplot(column=['Monetary'])
plt.show()

# since I found that the boxplot of "Frequency" & "Monetary" are 
# highly skewed, I decided to scale the data from 1-10, rather 
# than 1-5

# Create RFM Score
rfm1["RecencyScore"] = pd.qcut(rfm1["Recency"], 5, labels = [5, 4 , 3, 2, 1])
rfm1["FrequencyScore"]= pd.qcut(rfm1["Frequency"].rank(method="first"),10, labels=[1,2,3,4,5,6,7,8,9,10])
rfm1["MonetaryScore"] = pd.qcut(rfm1['Monetary'], 10, labels = [1,2,3,4,5,6,7,8,9,10])

# in this scenario, the retail business dataset should anticipate 
# customers with higher scores for recency and frequency compared 
# to monetary scores. Thus,  the RFM score could be calculated by 
# giving more weight to R and F scores than M. 
# RWeight 0.4 
# FWeight 0.4 
# MWeight 0.2 

rfm1["Weighted Average RFM Score"] = rfm1["RecencyScore"].astype(int)*0.4+rfm1["FrequencyScore"].astype(int)*0.4+rfm1["MonetaryScore"].astype(int)*0.2
rfm1["Weighted Average RFM Score"].describe()
rfm1.boxplot(column=['Weighted Average RFM Score'])
plt.show()

# Visualize the distribution of the RFM Score
plt.bar(rfm1["Weighted Average RFM Score"].value_counts().index, rfm1["Weighted Average RFM Score"].value_counts().values) 
plt.show()


# STEP 2: Divide customer into Tiers
# Champions: select the top 25% with the highest scores of Weighted Average RFM Score.
# Potential Loyalists: select the group from the median to the top 25%.
# At Risk Customers: Select customers from the 25th percentile to the median of Weighted Average RFM Score.
# New Customers: select the group from the minimum to 25th percentile of the Weighted Average RFM Score.

segment_category = lambda score: (
    'Champions' if score >= 6.2 else
    'Potential Loyalists' if score >= 4.4 else
    'At Risk Customers' if score >= 2.8 else
    'New Customers'
)
rfm1['Segment'] = rfm1['Weighted Average RFM Score'].apply(segment_category)

rfmStats1 = rfm1[["Segment","Recency","Frequency", "Monetary"]].groupby("Segment").agg(["mean","median","count", "std"])