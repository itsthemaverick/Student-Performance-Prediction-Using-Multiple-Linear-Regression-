import numpy as np 
import pandas as pd 

n=10000

np.random.seed(42)

study_hours = np.random.normal(5, 2, n).clip(0)
sleep_hours = np.random.normal(7, 1.5, n).clip(3)
attendance = np.random.uniform(85, 10, n).clip(50,100)
previous_score = np.random.normal(70,15,n).clip(0,100)
stress_level = np.random.randint(1,11,n)

final_score = (
    5*study_hours+
    2*sleep_hours+
    0.3*attendance+
    0.4*previous_score-
    2*stress_level+ np.random.normal(0,5,n)
).clip(0,100)

df = pd.DataFrame({
    "study_hours": study_hours,
    "sleep_hours": sleep_hours,
    "attendance": attendance,
    "previous_score":previous_score,
    "stress_level":stress_level,
    "final_score": final_score 
})

df.to_csv("performance.csv",index=False)