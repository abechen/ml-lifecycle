import pickle
from sklearn import datasets

if __name__ == "__main__":
    print('Loading iris data set...')

    iris_dataset = datasets.load_iris()
    
    # save feature
    print('Save feature...')
    file = open('/tmp/iris.feature', 'wb')
    pickle.dump(iris_dataset, file)
    file.close()