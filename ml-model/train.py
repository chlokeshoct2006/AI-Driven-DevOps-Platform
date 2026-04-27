import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Simulated dataset (you can replace later with real CloudWatch data)
data = pd.DataFrame({
    'cpu': [10, 20, 30, 40, 50, 60, 70, 80, 90, 95],
    'memory': [30, 35, 40, 50, 60, 70, 75, 85, 90, 95],
    'failure': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})

X = data[['cpu', 'memory']]
y = data['failure']

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved")