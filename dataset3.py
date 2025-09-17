# SUPERVISED DATA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#  x = square feet & y = price           #    reshape used to covert 1D array to 2D array
x = np.array([2500,2000,1000,1500,1650]).reshape(-1,1)
y = np.array([12000,234570,345680,35790,12345])
model = LinearRegression()
model.fit(x,y)
                                                 
# MODEL PARAMETERS 
print("Intercept (base price)",model.intercept_)
print("Slope (price per sqft)",model.coef_[0])

size = 1100
predicted_price = model.predict([[size]])
print(f"Predicted price for {size} sqft = ${predicted_price[0]:2f}")