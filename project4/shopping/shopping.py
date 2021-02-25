import csv
import sys

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    months = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5,
              'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}

    evidences = []
    labels = []
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        for row in file:
            if row[0] != "Administrative":
                evidence = row[:-1]
                label = 1 if row[-1] == "TRUE" else 0

                evidence[0] = int(evidence[0])
                evidence[1] = float(evidence[1])
                evidence[2] = int(evidence[2])
                evidence[3] = float(evidence[3])
                evidence[4] = int(evidence[4])
                evidence[5] = float(evidence[5])
                evidence[6] = float(evidence[6])
                evidence[7] = float(evidence[7])
                evidence[8] = float(evidence[8])
                evidence[9] = float(evidence[9])
                evidence[10] = months[evidence[10]]
                evidence[11] = int(evidence[11])
                evidence[12] = int(evidence[12])
                evidence[13] = int(evidence[13])
                evidence[14] = int(evidence[14])
                evidence[15] = 0 if evidence[15] == "New_Visitor" else 1
                evidence[16] = 1 if evidence[16] == "TRUE" else 0

                evidences.append(evidence)
                labels.append(label)

    return evidences, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    negatives = 0
    true_negatives = 0
    positives = 0
    true_positives = 0

    for label, prediction in zip(labels, predictions):
        if label == 0:
            negatives += 1
            if prediction == 0:
                true_negatives += 1

        if label == 1:
            positives += 1
            if prediction == 1:
                true_positives += 1

    sensitivity = true_positives / positives
    specificity = true_negatives / negatives

    return sensitivity, specificity


if __name__ == "__main__":
    main()
