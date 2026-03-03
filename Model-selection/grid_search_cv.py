import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

breast_cancer_ds = load_breast_cancer()
data_frame = pd.DataFrame(breast_cancer_ds.data, columns=breast_cancer_ds.feature_names)

data_frame["label"] = breast_cancer_ds.target

X = data_frame.drop(["label"], axis=1)
Y = data_frame["label"]

X = np.asarray(X)
Y = np.asarray(Y)

model = SVC()

parameters = {
    "C": [1, 5, 10, 20],
    "kernel": ['linear','poly','rbf','sigmoid']
}

classifier = GridSearchCV(
    estimator=model,
    param_grid=parameters,
    cv=5
)
print("Before fit")
classifier.fit(X, Y)
print("After fit")


print(classifier.cv_results_)
print(classifier.best_params_)
print(classifier.best_score_)
print(classifier.cv_results_)
print(classifier.best_estimator_)
