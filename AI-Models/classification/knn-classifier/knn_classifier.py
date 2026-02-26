import statistics

import numpy as np


class KNNClassifier:
    def __init__(self, distance_metric):
        self.distance_metric = distance_metric

    @staticmethod
    def euclidean_distance(training_data_point, test_data_point):
        dist = 0
        for i in range(len(training_data_point)):
            dist += (training_data_point[i] - test_data_point[i]) ** 2
        return np.sqrt(dist)

    @staticmethod
    def manhattan_distance(training_data_point, test_data_point):
        dist = 0
        for i in range(len(training_data_point)):
            dist += abs(training_data_point[i] - test_data_point[i])
        return dist

    def get_distance_metric(self, training_data_point, test_data_point):
        if self.distance_metric == "euclidean":
            return self.euclidean_distance(training_data_point, test_data_point)

        elif self.distance_metric == "manhattan":
            return self.manhattan_distance(training_data_point, test_data_point)

    def nearest_neighbors(self, X_train, test_data, k=3):
        distances = []
        for training_data_point in X_train:
            distance = self.get_distance_metric(training_data_point, test_data)
            distances.append((training_data_point, distance))

        nearest_neighbors = sorted(distances, key=lambda x: x[1])

        nearest_neighbors_list = [nearest_neighbor[1] for nearest_neighbor in nearest_neighbors[:k]]

        return nearest_neighbors_list

    def predict(self, X_train, test_data, k):
        labels = []
        nearest_neighbors = self.nearest_neighbors(X_train, test_data, k)
        for nearest_neighbor in nearest_neighbors:
            labels.append(nearest_neighbor[-1])

        predicted_class = statistics.mode(labels)
        return predicted_class

knn_classifier = KNNClassifier(distance_metric='euclidean')