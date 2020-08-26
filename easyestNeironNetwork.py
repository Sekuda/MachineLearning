import numpy


def sigmoid(x, der=False):
    """
    Функция сигмойд для определения значения весов
    """
    if der:
        return x * (1 - x)
    return 1 / (1 + numpy.exp(-x))


# Входные данные
x = numpy.array([[1, 0, 1],
                  [0, 1, 0],
                  [1, 0, 1],
                  [0, 1, 1]])

# Ожидаемые данные
# T-Функция переноса что бы получить 1 столбец и 4 ряда
y = numpy.array([[1, 0, 1, 1]]).T

#Чтобы случайное распределение было одинаковым
#Сделаем случайные веса более определенными
numpy.random.seed(1)

#инициируем веса случайным образом со средним 0
syn0 = 2 * numpy.random.random((3, 1)) - 1


l1 = []

for i in range(1000):

    #прямое распространение
    l0 = x
    l1 = sigmoid(numpy.dot(l0, syn0))

    #на сколько мы ошиблись
    l1_error = y - l1

    #перемножим это с наклоном сигмойды
    #на основе значений в l1
    l1_delta = l1_error * sigmoid(l1, True)

    #Обновим веса
    syn0 += numpy.dot(l0.T, l1_delta)

print(l1)


new_test = numpy.array([1, 0, 1])
l1_new = sigmoid(numpy.dot(new_test, syn0))
print("-------------")
print(l1_new)