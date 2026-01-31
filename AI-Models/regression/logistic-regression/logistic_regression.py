import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class LogisticRegression:
    def __init__(self, iteration, learning_rate):
        self.iteration = iteration
        self.learning_rate = learning_rate
        self.W, self.b = None, None
        self.m, self.b = None, None
        self.X, self.Y = None, None


    def fit(self, X, Y):
        self.m, self.n = X.shape

        self.W = np.zeros(self.n)
        self.b = 0

        self.X, self.Y = X, Y

        for i in range(self.iteration):
            self.update()

    def sigmoid(self, z):
        return  1 / (1 + np.exp(-z))

    def update(self):
        z = np.dot(self.X, self.W) + self.b
        Y_hat = self.sigmoid(z)

        dw = (1 / self.m) * np.dot(self.X.T, (Y_hat - self.Y))
        db = (1 / self.m) * np.sum(Y_hat - self.Y)

        self.W = self.W - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db

        return self

    def predict(self, X):
        z = np.dot(X, self.W) + self.b
        sigmoid = self.sigmoid(z)
        return np.where(sigmoid > 0.5, 1, 0)

def main():
    diabetes_df = pd.read_csv('../../../Datasets/diabetes.csv')

    features = diabetes_df.drop(columns='Outcome', axis=1)

    scaler = StandardScaler()
    scaler.fit(features)
    standardized_data = scaler.transform(features)
    features = standardized_data
    target = diabetes_df['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(features, target, random_state=2, test_size=0.2)

    model = LogisticRegression(1000, 0.01)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    test_data_accuracy = accuracy_score(Y_test, Y_pred)

    print("Predicted values ", np.round(Y_pred[:3], 2))

    print("Real values      ", Y_test[:3])

    print("Trained W        ", round(model.W[0], 2))

    print("Trained b        ", round(model.b, 2))

    print("Test data accuracy        ", test_data_accuracy)

if __name__ == "__main__":
    main()