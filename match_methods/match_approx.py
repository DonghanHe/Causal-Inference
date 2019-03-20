from sklearn.neighbors import LSHForest

def LSHForest_matching(X,y,Z):
    """
    We will fit LSH_forest to number of different matched sets. i.e. if there are 2 Xs, namely 0,1
    Then we fit an LSH_forest to category 0, and then category 1, and hash in


    :param X: the X data arrays, of shape (N,1) for now
    :param y: the response data arrays, (N,1)
    :param Z: Confounders, must be of shape (N,D_Z)
    :return: in the order of 0,1,2,...,C (number of categories in X)
    """

    N_x, D_x = X.shape
    N_y, D_y = y.shape
    N_Z, D_z = Z.shape

    assert (N_x==N_y) and (N_y==N_z), "Shape of the arrays does not agree"

    N = N_x
    unique_X = set(X)




