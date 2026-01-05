import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/performance.csv")

X = df.drop("final_score",axis =1)
y = df["final_score"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
mae = mean_absolute_error(y_test, y_pred)
rt= r2_score(y_test, y_pred)

print("mse: ",mse)
print("mae: ",mae)
print("R2 : ",rt)

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient" : model.coef_
}).sort_values(by="Coefficient", ascending=False)

coef_df.to_csv("data/coef.csv",index=False)