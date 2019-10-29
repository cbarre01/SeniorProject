# first neural network with keras make predictions
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = loadtxt('mergedDataReduced.csv', delimiter=',', skiprows = 1)

dataset2 = loadtxt('mergedDataReduced2.csv', delimiter=',', skiprows = 1)
dataset5 = loadtxt('mergedDataReduced5.csv', delimiter=',', skiprows = 1)
dataset8 = loadtxt('mergedDataReduced8.csv', delimiter=',', skiprows = 1)

# split into input (X) and output (y) variables
X = dataset[:,0:25]
y = dataset[:,26]

X2 = dataset2[:,0:25]
y2 = dataset2[:,26]

X5 = dataset5[:,0:25]
y5 = dataset5[:,26]

X8 = dataset8[:,0:25]
y8 = dataset8[:,26]

# define the keras model
model = Sequential()
model.add(Dense(10, input_dim=25, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=15, batch_size=32, verbose=1)

# make class predictions with the model
predictions = model.predict_classes(X)

# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))


#testing for specific innings
model.fit(X, y, validation_data=(X2,y2), epochs=15, batch_size=32)
model.fit(X, y, validation_data=(X5,y5), epochs=15, batch_size=32)
model.fit(X, y, validation_data=(X8,y8), epochs=15, batch_size=32)

