from numpy import *
from PIL import Image

def pca(X):
    """
    Principal Component Analysis (dimensionality reduction)
        :param:  X - matrix with training data stored as fattened arrays in rows
        :return: V - projection matrix (ordered by importance)
                 S - Variance matrix
                 mean_X - mean of training dat
    """
    
    # get dimentions
    num_data, dim = X.shape

    # center data
    mean_X = mean(X, axis=0)
    X = X - mean_X

    if dim > num_data:
        # PCA - compact trick used
        # A*A' = U*S*S'*U'
        M = dot(X, X.T) # covariance matrix
        e, U = linalg.eigh(M) # eigenvalues and eigenvectors
        V = dot(U.T, X) # compact trick
        V = V[::-1] # reverse because we want the last eigenvectors
        S = sqrt(e)[::-1] # reverse so that eigenvalues are in increasing order
        for i in range(V.shape[1]):
            V[:, i] /= S

    else:
        # PCD - SVD used
        U, S, V = linalg.svd(X)
        V = V[:num_data]

    return V, S, mean_X