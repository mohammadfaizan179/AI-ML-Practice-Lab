import pandas as pd
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def accuracy_score_simple_example():
    actual_value    = [1, 0, 1, 0, 0, 1]
    predicted_value = [1, 1, 1, 0, 0, 0]
    accuracy = accuracy_score(actual_value, predicted_value)
    accuracy = round(accuracy, 2) * 100
    print("Accuracy score: ", accuracy)

def model_accuracy_score():
    heart_data = pd.read_csv("../Datasets/heart.csv")
    X = heart_data.drop(columns="target", axis=1)
    Y = heart_data["target"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)

    Y_prediction = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_prediction)

    accuracy = round(accuracy, 2) * 100
    print("Model Accuracy: ", accuracy)

    cf_matrix = confusion_matrix(Y_test, Y_prediction)
    tn, fp, fn, tp = cf_matrix.ravel()
    print(cf_matrix)
    print(f"tn, fp, fn, tp: {tn}, {fp}, {fn}, {tp}")

    sns.heatmap(cf_matrix, annot=True)

    precision_score_res = precision_score(Y_test, Y_prediction)
    precision_score_res = round(precision_score_res, 2) * 100

    f1_score_res = f1_score(Y_test, Y_prediction)
    f1_score_res = round(f1_score_res, 2) * 100

    print("Precision Score: ", precision_score_res)
    print("F1 Score: ", f1_score_res)

if __name__ == "__main__":
    accuracy_score_simple_example()
    model_accuracy_score()
