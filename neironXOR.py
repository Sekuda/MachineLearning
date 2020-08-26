import numpy as np


def sigmoid(x):
    # Наша функция активации: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # Вводные данные о весе, добавление смещения
        # и последующее использование функции активации

        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)


weights = np.array([0, 1])  # w1 = 0, w2 = 1
bias = 4  # b = 4
n = Neuron(weights, bias)

x = np.array([2, 3])  # x1 = 2, x2 = 3
print(n.feedforward(x))  # 0.9990889488055994


class OurNeuralNetwork:
    """
    Нейронная сеть, у которой:
        - 2 входа
        - 1 скрытый слой с двумя нейронами (h1, h2)
        - слой вывода с одним нейроном (o1)
    У каждого нейрона одинаковые вес и смещение:
        - w = [0, 1]
        - b = 0
    """

    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        # Класс Neuron из предыдущего раздела
        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        # Вводы для о1 являются выводами h1 и h2
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1


network = OurNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x))  # 0.7216325609518421

