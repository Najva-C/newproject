import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("Naajva/Walmart_sales.csv")

data['date'] = pd.to_datetime(data['date'])
data['month'] = data['date'].dt.month
data['day_of_week'] = data['date'].dt.dayofweek

data = data.drop(['date', 'store'], axis=1)

X = data.drop('sales', axis=1)
y = data['sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)  

print("Mean Squared Error:", mse)
print("R² Score (Accuracy):", r2)


print(pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred}).head())
