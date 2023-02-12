import numpy as np

class Perceptron():
    def __init__(self, lr=0.01, n_iters=1000) -> None:
        self.lr = lr
        self.n_iters = n_iters
        self.activation_function = self._activation_func
        self.weights = None
        self.bias = None

    def _activation_func(self, X):
        return np.where(X>=0, 1, 0)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        y_true = np.array([1 if i>0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_sample in enumerate(X): # foreach training sample: w += lr * (y_true - y_pred) * sample
                y_pred = self.predict(x_sample)
                update_w = self.lr * (y_true[idx] - y_pred)
                self.weights += update_w * x_sample
                self.bias = update_w

    def predict(self, X): # linear function to later be activated: transpose(weight)*x + bias
        linear_func_out = np.dot(X, self.weights) + self.bias # transpose(weight)*x == dot product!!
        y_pred = self.activation_function(linear_func_out)

        return y_pred # ŷ = g(f(weight,bias))