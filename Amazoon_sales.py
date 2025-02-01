import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("C://Users//lenovo//Desktop//lib_python_proj//Amazon Sale Report.csv",encoding= 'unicode_escape')

print(df.shape) #to check no of rows and columns
print(df.head) # first 5 rows
print(df.tail) #last 5 rows
print(df.info) #coumn details and its data type details etc

#drop unrelated/blank columns
col=df.drop(['New','PendingS'], axis=1, inplace=True) # axis=1 to delete whole column , inplace =true to save whatever changes we did
print(col) # as these 2 column has 0 values
# o/p- None
print(df.info)


# checking null value
print(pd.isnull(df))
"""
        index  Order ID   Date  ...  ship-country    B2B  fulfilled-by
0       False     False  False  ...         False  False         False
1       False     False  False  ...         False  False         False
2       False     False  False  ...         False  False          True
3       False     False  False  ...         False  False         False
4       False     False  False  ...         False  False          True
...       ...       ...    ...  ...           ...    ...           ...
128971  False     False  False  ...         False  False          True
128972  False     False  False  ...         False  False          True
128973  False     False  False  ...         False  False          True
128974  False     False  False  ...         False  False          True
128975  False     False  False  ...         False  False          True
"""


# sum will give total values of null values
print(pd.isnull(df).sum())
"""
index                     0
Order ID                  0
Date                      0
Status                    0
Fulfilment                0
Sales Channel             0
ship-service-level        0
Category                  0
Size                      0
Courier Status            0
Quantity                  0
currency               7800
Amount                 7800
ship-city                35
ship-state               35
ship-postal-code         35
ship-country             35
B2B                       0
fulfilled-by          89713
dtype: int64
"""

print(df.shape)
#o/p- no of rows & columns (128976, 19)

#drop null values
print(df.dropna(inplace=True))
print(df.shape)
#o/p-(37514, 19) as null values droped

"""
Index(['index', 'Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel',
       'ship-service-level', 'Category', 'Size', 'Courier Status', 'Quantity',
       'currency', 'Amount', 'ship-city', 'ship-state', 'ship-postal-code',
       'ship-country', 'B2B', 'fulfilled-by'],
      dtype='object')
"""

print("************************")
# change data type of postal code
# Fill NaN values with a default value (e.g., 0), then convert to int32
df['ship-postal-code'] = df['ship-postal-code'].fillna(0).astype('int32')

# Check the data type
print(df['ship-postal-code'].dtype)

# change date datatype
df['Date']=pd.to_datetime (df['Date'])
print(df.columns)
"""
Index(['index', 'Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel',
       'ship-service-level', 'Category', 'Size', 'Courier Status', 'Quantity',
       'currency', 'Amount', 'ship-city', 'ship-state', 'ship-postal-code',
       'ship-country', 'B2B', 'fulfilled-by'],
      dtype='object')"""

#rename Columns
df.rename(columns={'Qty':'Quantity'},inplace=True)
print(df)
print(df.columns)
print("---------------------------------------")


#describe() method return description of the data in the DataFrame(i.e count,mean,std,min..etc)
print(df.describe()) # used for numeric type
"""
              index  ... ship-postal-code
count   37514.000000  ...     37514.000000
mean    60953.809858  ...    463291.552754
min         0.000000  ...    110001.000000
25%     27235.250000  ...    370465.000000
50%     63470.500000  ...    500019.000000
75%     91790.750000  ...    600042.000000
max    128891.000000  ...    989898.000000
std     36844.853039  ...    194550.425637
"""

print(df.describe(include='object')) # described used include for object
"""
                  Order ID  ... fulfilled-by
count                 37514  ...        37514
unique                34664  ...            1
top     171-5057375-2831560  ...    Easy Ship
freq                     12  ...        37514
"""

#use describe() for specific columns
print(df[['Quantity','Amount']].describe())
"""
            Quantity       Amount
count  37514.000000  37514.000000
mean       0.867383    646.553960
std        0.354160    279.952414
min        0.000000      0.000000
25%        1.000000    458.000000
50%        1.000000    629.000000
75%        1.000000    771.000000
max        5.000000   5495.000000
"""

# Print the 'ship-state' column
print(df['ship-state'])
# ##Convert state names to uppercase
df['ship-state'] = df['ship-state'].str.upper()

#Q1)  top 10-state
top_10_state = df['ship-state'].value_counts().head(10)
print(top_10_state)
"""
MAHARASHTRA       6236
KARNATAKA         4550
UTTAR PRADESH     3298
TAMIL NADU        3167
TELANGANA         3136
KERALA            2213
DELHI             1955
WEST BENGAL       1653
ANDHRA PRADESH    1621
GUJRAT        1382
Name: count, dtype: int64
"""

#Q2) What is the total revenue generated by each product category?
# Assuming 'Price' and 'Quantity' columns exist in the dataset
df['Total_Sales'] = df['Amount'] * df['Quantity']

# Group by product category and sum the total sales
category_sales = df.groupby('Category')['Total_Sales'].sum().reset_index()

# Sort in descending order
category_sales = category_sales.sort_values(by='Total_Sales', ascending=False)

print(category_sales.head())  # Show top categories by revenue

"""
   Category  Total_Sales
5   T-shirt   10103409.0
2     Shirt    5359763.0
0   Blazzer    4405510.0
6  Trousers    1083032.0
1   Perfume     179404.0
"""
print("_______________________________________")

#Q3) Which state has the highest number of orders?
# Count the number of orders per state
state_orders = df['ship-state'].value_counts().reset_index()

# Rename columns
state_orders.columns = ['State', 'Order_Count']

print(state_orders.head())  # Show top states by order count
"""
           State  Order_Count
0    MAHARASHTRA         6236
1      KARNATAKA         4550
2  UTTAR PRADESH         3298
3     TAMIL NADU         3167
4      TELANGANA         3136
"""
print("_______________________________________")

#Q4)  Which courier service has the most deliveries?
# Count the number of shipments by courier service
courier_counts = df['Fulfilment'].value_counts().reset_index()

# Rename columns
courier_counts.columns = ['Fulfilment', 'Number of Deliveries']

print(courier_counts.head())  # Show top courier services
"""
  Fulfilment  Number of Deliveries
0   Merchant                 37514"""
print("_______________________________________")

#Q5) What is the most common product size ordered?
# Count the occurrences of each size
size_counts = df['Size'].value_counts().reset_index()

# Rename columns
size_counts.columns = ['Size', 'Quantity']

print(size_counts.head())  # Show the most common sizes ordered
"""
 Size  Quantity
0    M      6806
1    L      6646
2   XL      6326
3  XXL      5090
4    S      4558
"""

#Q6)  Which month has the highest sales?
# Extract month from order date
df['Order Month'] = df['Date'].dt.month

# Group by month and sum total sales
monthly_sales = df.groupby('Order Month')['Total_Sales'].sum().reset_index()

# Sort in descending order
monthly_sales = monthly_sales.sort_values(by='Total_Sales', ascending=False)

print(monthly_sales)  # Show monthly sales
"""
 Order Month  Total_Sales
1            4    8117420.0
2            5    7494038.0
3            6    5682811.0
0            3      10797.0
"""



#Exploratory Data Analysis

print(df.columns)
"""
Index(['index', 'Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel',
       'ship-service-level', 'Category', 'Size', 'Courier Status', 'Quantity',
       'currency', 'Amount', 'ship-city', 'ship-state', 'ship-postal-code',
       'ship-country', 'B2B', 'fulfilled-by'],
      dtype='object')
      """


#1) Which size is selling the fastest in terms of quantity?
size_sales = df.groupby('Size')['Quantity'].sum().reset_index()

# Sort in descending order to see the fastest-selling sizes
size_sales = size_sales.sort_values(by='Quantity', ascending=False)

print(size_sales.head())
"""
  Size  Quantity
6     M      5905
5     L      5795
8    XL      5481
10  XXL      4465
0   3XL      3972
"""

print("$$$$$$$$$$$$$$$$$$$$$$$$$$")

#Visualization :
ax = sns.countplot(x='Size', data=df, hue='Size', palette='Set2', legend=False)

for bars in ax.containers:
    ax.bar_label(bars , padding=3) # padding can adjust the distance from the top of the bar

# title and labels
ax.set_title('Count of Different Sizes')
ax.set_xlabel('Size',)
ax.set_ylabel('Count')
ax.bar_label(bars, padding=3, fontsize=14, color='black')
plt.show()

#2) The groupby() function in pandas is used to group data based on one or more columns in a DataFrame
"""
This will give you a DataFrame where the Size values are listed in ascending order of the total quantity ."""
result = df.groupby(['Size'], as_index=False)['Quantity'].sum().sort_values(by='Quantity', ascending=True)
# Display the result
print(result)
"""
  Size  Quantity
1    4XL        93
2    5XL       104
3    6XL       170
4   Free       467
9     XS      2191
7      S      3896
0    3XL      3972
10   XXL      4465
8     XL      5481
5      L      5795
6      M      5905
"""

# Plot the result using a bar plot
plt.figure(figsize=(10, 6))  # Optional: Adjust the size of the plot
ax = sns.barplot(x='Size', y='Quantity', data=result,hue='Size', palette='Set2',legend=False)

ax.set_title('Total Quantity by Size')
ax.set_xlabel('Size')
ax.set_ylabel('Total Quantity')

# Rotate x-axis labels to 45 degrees
plt.xticks(rotation=45)
plt.show()

#3) Courier Status :- From above Graph the majority of the orders are shipped through the courier.
# Create a count plot with 'Courier Status' on the x-axis and 'Status' as hue
plt.figure(figsize=(10, 5))

ax=sns.countplot(data=df, x='Courier Status', hue='Status')

plt.title('Courier Status by Status')
plt.xlabel('Courier Status')
plt.ylabel('Count')
plt.show()

#4) Plot 4
plt.figure(figsize=(10, 6))
df['Size'].hist(bins=20, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Distribution of Size')
plt.xlabel('Size')
plt.ylabel('Frequency')

# Show the plot
plt.show()


#5) hot selling product category distribution
df['Category'] = df['Category'].astype(str)
category_counts = df['Category'].value_counts()

plt.figure(figsize=(10, 5))
bars = category_counts.plot(kind='bar', color='purple', edgecolor='red')
most_bought_index = category_counts.idxmax()
bars.patches[category_counts.index.get_loc(most_bought_index)].set_color('orange')

plt.title('Hot selling product category distribution')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

#From above chart we can see that maximum i.e. 99.2% of buyers are retailers and 0.8% are B2B buyers
#6) Retailers v/s B2B buyers pie chart
B2B_Check = df['B2B'].value_counts()

# Define custom colors for the slices
colors = ['#FF9999', '#66B3FF']  # Soft red and blue colors

plt.figure(figsize=(8, 8))
plt.pie(B2B_Check,
        labels=B2B_Check.index,
        autopct='%1.1f%%',           # Display percentage on the chart
        startangle=60,               # Start angle to make it more visually appealing
        colors=colors,               # Set custom colors for the slices
        explode=(0.1, 0),            # Explode the first slice (highlight 'Yes' or the larger category)
        shadow=True)                 # Add a shadow effect to the pie chart for depth

plt.axis('equal')
plt.title('Retailers v/s B2B buyers')
plt.show()
###From above chart you can see that most of the Fulfilment are done by amazon"""

#
#7) plot count of cities by state
plt.figure(figsize=(12, 6))
ax = sns.countplot(data=df, x='ship-state', palette='viridis')

plt.xlabel('Ship State', fontsize=10)
plt.ylabel('Count', fontsize=12)
plt.title('Distribution of Ship State wise', fontsize=14, fontweight='bold')

plt.xticks(rotation=90)

max_state = df['ship-state'].value_counts().idxmax()  # Get the state with the highest count
for bar in ax.patches:
    if bar.get_x() == df['ship-state'].unique().tolist().index(max_state):
        bar.set_color('red')

for bar in ax.containers:
    ax.bar_label(bar, fontsize=8, color='black')
plt.show()

### maximum buyers are from which state? or top 10 states?

#8) Get top 10 states by count
top_10_state = df['ship-state'].value_counts().head(10)
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700', '#FF6347', '#8A2BE2', '#20B2AA', '#FF4500', '#6495ED', '#D2691E']

plt.figure(figsize=(10, 6))
wedges, texts, autotexts = plt.pie(top_10_state,
                                   labels=top_10_state.index,  # Labels as state names
                                   autopct='%1.1f%%',         # Show percentage
                                   startangle=140,            # Rotate for better visibility
                                   colors=colors,             # Use custom colors
                                   wedgeprops={'edgecolor': 'white'},  # White edges for clarity
                                   shadow=True,               # Add shadow effect
                                   explode=[0.1 if i == 0 else 0 for i in range(10)])  # Highlight top state

# Improve text readability
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')

plt.title('Top 10 Ship States Distribution', fontsize=14, fontweight='bold')
plt.show()



"""

Conclusion
The data analysis reveals that the business has a significant customer base in Maharashtra state,
 mainly serves retailers, fulfills orders through Amazon, experiences high demand for T-shirts,
 and sees M-Size as the preferred choice among buyers.
"""