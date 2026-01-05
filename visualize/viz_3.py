import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/performance.csv")

X = df.drop("final_score",axis =1)
y = df["final_score"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model_scaled = LinearRegression()
model_scaled.fit(X_scaled,y)

coef_std = pd.DataFrame({
    "Feature" : X.columns,
    "Coefficient" : model_scaled.coef_
}).sort_values(by="Coefficient",ascending=False)

plt.figure(figsize=(8,5))
plt.barh(coef_std["Feature"],coef_std["Coefficient"])
plt.xlabel(" Std Coeff")
plt.ylabel("Std Feature")
plt.title("Standardized Feature Importance")
plt.gca().invert_yaxis()
plt.show()