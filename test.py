import pytest
from utils import prepare_data, create_model, train_model

def test_accuracy():
    X_train, Y_train, X_test, Y_test = prepare_data()

    model = create_model()

    accuracy = train_model(model=model, X_train=X_train, Y_train=Y_train, X_test=X_test, Y_test=Y_test)

    assert accuracy > 0.45
