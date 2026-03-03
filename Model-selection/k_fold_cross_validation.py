import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


heart_data = pd.read_csv("../Datasets/heart.csv")
X = heart_data.drop(columns="target", axis=1)
Y = heart_data["target"]


model = LogisticRegression(max_iter=1000)
cv_score_lr = cross_val_score(model, X, Y, cv=5)
mean_accuracy_lr = sum(cv_score_lr) / len(cv_score_lr)
mean_accuracy_lr = mean_accuracy_lr * 100
mean_accuracy_lr = round(mean_accuracy_lr, 2)
print(mean_accuracy_lr)
