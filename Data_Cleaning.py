import pandas as pd
# Read the dataset
data = pd.read_csv('D://DS//python_learning//7003_Lab4//7001//donations_facility.csv')

# Step A: Remove rows with missing values in the hospital columns
cleaned_data = data.dropna(subset=['hospital'])

# Step B: Convert date column to date format
cleaned_data['date'] = pd.to_datetime(cleaned_data['date'])

# Step C: Retain data for 2014 and beyond
cleaned_data = cleaned_data[cleaned_data['date'].dt.year >= 2014]

# save the cleaned data
cleaned_data.to_csv('cleaned_donations_facility_new.csv', index=False)

import matplotlib.pyplot as plt

# Number of records before and after data cleansing
before = [193201, 151801, 87517]
steps = ['Original', 'Removed Missing', 'Filtered Year >= 2014']

plt.figure(figsize=(8, 5))
plt.bar(steps, before, color=['blue', 'orange', 'green'])
plt.title('Data Cleaning Process')
plt.ylabel('Number of Records')
plt.xlabel('Steps')
plt.show()

import matplotlib.pyplot as plt

plt.boxplot(data['daily'])
plt.title('Boxplot of Daily Donations')
plt.ylabel('Daily Donations')
plt.show()


import matplotlib.pyplot as plt

# Plotting histograms to locate 'daily' outliers
plt.figure(figsize=(10, 6))
plt.hist(cleaned_data['daily'], bins=50, edgecolor='black', alpha=0.7)
plt.title('Histogram of Daily Donations')
plt.xlabel('Daily Donations')
plt.ylabel('Frequency')

# Add dotted lines for mean and median values
plt.axvline(cleaned_data['daily'].mean(), color='red', linestyle='dashed', linewidth=1.5, label='Mean')
plt.axvline(cleaned_data['daily'].median(), color='green', linestyle='dashed', linewidth=1.5, label='Median')

# Adding Legends and Grids
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show Chart
plt.show()
