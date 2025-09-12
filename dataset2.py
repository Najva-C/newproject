import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
import warnings 

warnings.filterwarnings("ignore", category=UserWarning)

#load data
data=pd.read_csv("NUMPY/50_startups_sample.csv",encoding='latin1')
print(data.head())

#split features and target
x=data[["R&D Spend","Administration","Marketing Spend","State"]]
y=data['Profit']
preprocessor=ColumnTransformer(transformers=[("state_enc",OneHotEncoder(drop="first",handle_unknown='ignore'),["State"])],remainder="passthrough")

#create pipeline with preprocessor + regression
pipeline=Pipeline(steps=[("preprocessing",preprocessor),("regression",LinearRegression())])

#split data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=42)

#train model
pipeline.fit(x_train,y_train)

#predict & evaluate
y_pred=pipeline.predict(x_test)
r2=r2_score(y_test,y_pred)
print("Predicted Profit:",y_pred)
print("R^2 score:",round(r2,4))





# OTHER WAY OF CODE 


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import r2_score
# import warnings 

# warnings.filterwarnings("ignore", category=UserWarning)

# # Load data (correct file path!)
# data = pd.read_csv("NUMPY/50_startups_sample.csv", encoding='latin1')
# print("First 5 rows of the dataset:\n", data.head())

# # Split features and target
# x = data[["R&D Spend", "Administration", "Marketing Spend", "State"]]
# y = data["Profit"]

# # Preprocessor: OneHotEncode 'State' (handle unknown categories gracefully)
# preprocessor = ColumnTransformer(
#     transformers=[("state_enc", OneHotEncoder(drop="first", handle_unknown='ignore'), ["State"])],
#     remainder="passthrough"
# )

# # Create pipeline: preprocessing + linear regression
# pipeline = Pipeline(steps=[("preprocessing", preprocessor), ("regression", LinearRegression())])

# # Train/test split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=42)

# # Train model
# pipeline.fit(x_train, y_train)

# # Predict & evaluate
# y_pred = pipeline.predict(x_test)
# r2 = r2_score(y_test, y_pred)

# print("\nPredicted Profit values:\n", y_pred)
# print("\nActual Profit values:\n", y_test.values)
# print("\nR^2 score:", round(r2, 4))
