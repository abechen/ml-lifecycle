import pickle
from sklearn import datasets

def get_dataset():
    print('Loading iris data set...')
    
    return datasets.load_iris()

if __name__ == "__main__":
    iris_dataset = get_dataset()
    
    # save dataset
    print('Save dataset...')
    file = open('iris.dataset', 'wb')
    pickle.dump(iris_dataset, file)
    file.close()