import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression


def convert_txt_2_csv(file_path):
    with open(file_path, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open('apt_data.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)


def read_csv(file_path):
    headers = [
        "unknown_0",
        "unknown_1",
        "complex_age",
        "total_rooms",
        "total_bedrooms",
        "complex_inhabitants",
        "apartaments_nr",
        "unknown_2",
        "median_complex_value"
    ]

    return pd.read_csv(file_path, names=headers)


def prepare_data():
    convert_txt_2_csv(file_path='apartmentComplexData.txt')

    apt_data = read_csv(file_path='apt_data.csv')

    apt_data.info()

    Y = apt_data.iloc[:, 8].values
    X = apt_data.drop(['median_complex_value'], axis=1)

    X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2)

    return X_train, Y_train, X_test, Y_test


def create_model():
    model = LinearRegression()

    return model

def train_model(model, X_train, Y_train, X_test, Y_test):
    model.fit(X_train, Y_train)
    accuracy = model.score(X_train, Y_train)

    prediction = model.predict(X_test)

    #prepare data for plot
    res = pd.DataFrame({'Predicted':prediction,'Actual':Y_test})
    res = res.reset_index()
    res = res.drop(['index'],axis=1)

    print(res)

    #plot
    plt.plot(res[:30])
    plt.legend(['Actual', 'Predicted'])
    plt.savefig('filename.svg')

    return accuracy

