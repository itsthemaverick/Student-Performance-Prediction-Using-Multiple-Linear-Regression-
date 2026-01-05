import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("data/performance.csv")

X = df.drop("final_score",axis =1)
y = df["final_score"]

features = X.columns

plt.figure(figsize=(15,10))

for i,feature in enumerate(features,1):
    plt.subplot(2,3,i)
    plt.scatter(df[feature],y,alpha=0.4)
    plt.xlabel(feature)
    plt.ylabel("final_score")
    plt.title(f"{feature} vs Final score")

plt.tight_layout()
plt.show()
