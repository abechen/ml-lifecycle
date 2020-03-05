import sys
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

import mlflow
import mlflow.sklearn

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def training(X, y, random_state):
    print("Training LogisticRegression model (random_state=%f):" % (random_state))

    lr = LogisticRegression(random_state=random_state)

    # train model
    print('Training model...')
    lr.fit(X, y)
    print('Model trained!')

    # save model to local
    #filename_p = 'tmp/IrisClassifier.model'
    #print('Saving model in %s' % filename_p)
    #joblib.dump(p, filename_p)
    #print('Model saved!')

    return lr

def predict_for_test(model, x, y):
    print("Testing model")


if __name__ == "__main__":
    print('Get model parameters...')

    # random_state
    random_state_input = int(sys.argv[1]) if len(sys.argv) > 1 else 0

    print('Loading feature...')
    with open('iris.feature', 'rb') as file:
        iris_feature = pickle.load(file)

    # Split the data into training and test sets. (0.75, 0.25) split.
    X_train, X_test, y_train, y_test = train_test_split(iris_feature.data, iris_feature.target, test_size=0.25)

    with mlflow.start_run():
        model = training(X_train, y_train, random_state=random_state_input)

        predicted_qualities = model.predict(X_test)

        (rmse, mae, r2) = eval_metrics(y_test, predicted_qualities)
        
        print("LogisticRegression model (random_state=%f):" % (random_state_input))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        # log_param
        mlflow.log_param("random_state", random_state_input)

        # log_metric
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)
        
        # log_model
        mlflow.sklearn.log_model(model, "IrisClassifier")