import ...

class match(object):

    """
    a matching method that is able to handle high dimensional confounders.
    including methods:
        NN matching
            exact KNN matching
            inexact KNN matching
        Propensity score matching

    FINISHED:
        None
    TODO:
        exact KNN
        approximate KNN
        propensity score matching

    input

    """

    def __init__(self,X, y, Z, DF, method = None):
        """

        :param X: the treatment variables (list of int or str)
        :param y: response to treatments (int or str)
        :param Z: confounders for matching (int or str)
        :param DF: if numpy array, then we use only list indice
        :param method: please refer to methods for more information
        """

        pass

    def check_balance(self):
        """

        :return:
        """

        pass

    def exact_KNN_match(self, K ):
        """
        :param K: number of Ks
        :return:
        """
        


        pass

    def PSM_match(self):
        """

        :return:
        """

        pass

    def approx_KNN_match(self, K, method = 'auto'):
        """

        :param K: number of Ks
        :param method: plan to implement the following/use the following
                        1. LSH for hamming distance
                        2. LSH for Euclidean distance
                        3. Angular LSH
                        4. maybe more complicated ones?
        :return:
        """

        pass

    def plot_balance(self,method = 'auto'):
        """

        :param method: if variables higher than 2 dimensions, we might need to resort to PCA
        :return:
        """

        pass

