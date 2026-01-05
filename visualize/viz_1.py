import matplotlib.pyplot as plt 
import pandas as pd
 

coeff_df = pd.read_csv("data/coef.csv")

plt.figure(figsize=(8,5))
plt.barh(coeff_df["Feature"],coeff_df["Coefficient"])
plt.xlabel("Coeff")
plt.ylabel("Feature")
plt.title("Multiplr Linear Regression")
plt.gca().invert_yaxis()
plt.show()