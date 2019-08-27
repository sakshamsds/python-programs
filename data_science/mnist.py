from keras.datasets import mnist

#download mnist dataset and split into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt

#plot the first image of dataset
plt.imshow(X_train[0])

#check the image shape
X_train[0].shape

#reshape data to fill the model
X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000, 28,28,1)

from keras.utils import to_categorical

#one-hot encode target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

y_train[0]

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

#create model
model = Sequential()

#add model layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))     

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs =2)

#predict the first 4 images in the test set
model.predict(X_test[0:4]) > 0.5