import pandas as pd
import csv
from utils import prepare_data, create_model, train_model


if __name__ == "__main__":
    X_train, Y_train, X_test, Y_test = prepare_data()

    model = create_model()

    model = train_model(model=model, X_train=X_train, Y_train=Y_train, X_test=X_test, Y_test=Y_test)

