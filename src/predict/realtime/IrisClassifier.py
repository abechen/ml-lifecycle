#encoding:utf-8
from sklearn.externals import joblib

class IrisClassifier(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing")
        self.model = joblib.load('model.pkl')
        self.class_names = ["iris-setosa", "iris-vericolor", "iris-virginica"]

    def predict(self, X, features_names=None):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called - will run identity function")
        return self.model.predict_proba(X)

    """
    https://docs.seldon.io/projects/seldon-core/en/latest/python/python_component.html
    """
    # def transform_input(self, X: np.ndarray, names: Iterable[str], meta: Dict = None) -> Union[np.ndarray, List, str, bytes]:

    # def transform_output(self, X: np.ndarray, names: Iterable[str], meta: Dict = None) -> Union[np.ndarray, List, str, bytes]:

    # def aggregate(self, features_list: List[Union[np.ndarray, str, bytes]], feature_names_list: List) -> Union[np.ndarray, List, str, bytes]:

    # def route(self, features: Union[np.ndarray, str, bytes], feature_names: Iterable[str]) -> int:

    # def metrics(self) -> List[Dict]:

    # def tags(self) -> Dict:

    # def health_status(self) -> Union[np.ndarray, List, str, bytes]:
