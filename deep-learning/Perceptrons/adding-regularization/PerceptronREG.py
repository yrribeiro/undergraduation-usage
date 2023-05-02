import numpy as np

class PerceptronREG:
    def __init__(self, lr=0.1, n_epochs=100, alpha=None):
        self.lr = lr
        self.n_epochs = n_epochs
        self.alpha = alpha

    def fit(self, X, y):
        # Adicionando bias ao conjunto de dados
        X = np.c_[X, np.ones(X.shape[0])]

        # Inicializando pesos aleatórios
        self.w = np.zeros(X.shape[1])

        # Treinamento do modelo
        for epoch in range(self.n_epochs):
            for xi, yi in zip(X, y):
                z = np.dot(xi, self.w)
                output = 1 if z > 0 else 0
                self.w += self.lr * (yi-output) * xi
                if self.alpha:
                    self.w -= self.lr * self.alpha * self.w

    def predict(self, X):
        # Adicionando bias ao conjunto de dados
        X = np.c_[X, np.ones(X.shape[0])]
        z = np.dot(X, self.w)
        # Fazendo a predição
        return np.where(z>0, 1, 0)
