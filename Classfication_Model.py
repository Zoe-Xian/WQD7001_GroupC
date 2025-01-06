# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the Dataset
file_path = 'cleaned_data.csv'  # Update with your Google Colab file path
df = pd.read_csv(file_path)

# Step 3: Create the Classification Target
average_daily_donations = df['daily'].mean()
df['donations_daily_category'] = df['daily'].apply(
    lambda x: 'Sufficient' if x > average_daily_donations else 'Insufficient'
)

# Drop unnecessary columns
df = df.drop(columns=['date', 'hospital', 'daily'])

# Step 4: Prepare Data for Model Training
X = df.drop(columns=['donations_daily_category'])
y = df['donations_daily_category']

# Encode target variable
y = y.map({'Sufficient': 1, 'Insufficient': 0})

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Classification Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 7: Feature Importance Plot
feature_importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=feature_names)
plt.title('Feature Importance')
plt.show()