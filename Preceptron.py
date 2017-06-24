import csv, numpy as np

#Reads the file and returns it after appending in a list
def ReadFile():
    my_list = []

    with open('dataset.csv',newline='') as f:
        reader = csv.reader(f)

        for row in reader:
            my_list.append(row)
      
    return my_list

#To convert elements from string to float
def String_to_Float(my_list):
    for i in range(len(my_list)):
        if my_list[i][4] == 'Iris-virginica':
            my_list[i][4] = 2
        elif my_list[i][4] == 'Iris-versicolor':
            my_list[i][4] = 1
        elif my_list[i][4] == 'Iris-setosa':
            my_list[i][4] = 0
    l = [[float(string) for string in inner] for inner in my_list]
    return l

# Make a prediction with weights
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return weights

# Calculate weights
dataset = String_to_Float(ReadFile())
l_rate = 0.1
n_epoch = 7
weights = train_weights(dataset, l_rate, n_epoch)
print(weights)