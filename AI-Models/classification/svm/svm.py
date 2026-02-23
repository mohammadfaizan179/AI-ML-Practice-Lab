import numpy as np
import pandas as pd
from requests.packages import target
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class SVM_Clasifier:
    def __init__(self, iteration, learning_rate, lambda_parameter):
        self.iteration = iteration
        self.learning_rate = learning_rate
        self.lambda_parameter = lambda_parameter
        self.weights = None
        self.bias = None
        self.X = None
        self.Y = None


    def fit(self, X_train, Y_train):
        rows, columns = X_train.shape
        self.weights = np.zeros(columns)
        self.bias = 0
        self.X = X_train
        self.Y = Y_train

        for i in range(self.iteration):
            self.update()

    def predict(self, X_test):
        output = np.dot(X_test, self.weights) - self.bias
        predicted_label = np.sign(output)
        h_hat = np.where(predicted_label == 1, 1, 0)
        return h_hat

    def update(self):
        y_label = np.where(self.Y == 1, 1, -1)

        for index, x_i in enumerate(self.X):
            condition = (y_label[index] * np.dot(x_i, self.weights) - self.bias) >= 1

            if condition:
                dw = 2 * self.lambda_parameter * self.weights
                db = 0
            else:
                dw = (2 * self.lambda_parameter * self.weights) - np.dot(x_i, y_label[index])
                db = y_label[index]

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

        return self


def main():
    diabetes = pd.read_csv("../../../Datasets/diabetes.csv")

    target = diabetes["Outcome"]
    features = diabetes.drop(columns="Outcome", axis=1)

    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    X_train, X_test, Y_train, Y_test = train_test_split(features, target, random_state=2, test_size=0.2)


    svm_classifier = SVM_Clasifier(1000, 0.01, 0.01)
    svm_classifier.fit(X_train, Y_train)
    Y_pred = svm_classifier.predict(X_test)
    score = accuracy_score(Y_test, Y_pred)

    print("True Value: ", Y_test[0:3])
    print("Pred Value: ", Y_pred[0:3])
    print("Score: ", score)

    input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)
    input_data = np.asarray(input_data)
    input_data = input_data.reshape(1, -1)
    input_data = StandardScaler().transform(input_data)
    prediction = svm_classifier.predict(input_data)
    if prediction == 1:
        print("Diabetes")
    else:
        print("Not Diabetes")

if __name__ == "__main__":
    main()