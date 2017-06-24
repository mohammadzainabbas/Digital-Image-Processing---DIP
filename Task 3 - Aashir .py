import pandas as pd, matplotlib.pyplot as plt, numpy as np

class Perceptron(object):
    def __init__(self, eta=0.1, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w = np.zeros(1 + X.shape[1])
        self.erros = []
        for _ in range(self.n_iter):
            erros = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w[1:] += update * xi
                self.w[0] += update
                erros += int(update != 0.0)
            self.erros.append(erros)
        print((self.w))
        print((self.erros))
        return self

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def predict(self, x):
        return np.where(self.net_input(x) >= 0.0, 1, -1)


# as its binary classifier
# considering two classes

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values
plt.scatter(X[:50, 0], X[:50, 1], color='black', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, -1], color='green', marker='x', label='versicolor')
plt.xlabel('sapel length')
plt.ylabel('petal length')
plt.legend(loc='upper left')

plt.show()

# calling class

# at 10 iterations you almost get zero error for this data set
# as you decrease number of iterations the error will increase
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
print(ppn.erros)
plt.plot(range(1, len(ppn.erros) + 1), ppn.erros)
plt.xlabel('Attempts')
plt.ylabel('Number of Missclassification')
plt.show()