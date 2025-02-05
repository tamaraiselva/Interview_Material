import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Example dataset
data = {'Area': [2600, 3000, 3200, 3600, 4000], 'Price': [550000, 565000, 610000, 680000, 725000]}
df = pd.DataFrame(data)

# Features and target
X = df[['Area']]
y = df['Price']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Output coefficients
print(f'Coefficients: {model.coef_}')
