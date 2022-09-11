"""A simple Neural Network to implement multi-class clasification on iris data"""

#importing the necessary libraries
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#load_the data
data = load_iris()
X = data.data
y = data.target
#print(X.shape, y.shape)

#to train the neural network single target column is converted into one-hot encoded format
# y = y.reshape(-1, 1)
# encode = OneHotEncoder(sparse=False)
# y = encode.fit_transform(y) 

#or use
y = tf.keras.utils.to_categorical(y)


#build the model
def build_model():
    
    model = Sequential([
        Dense(10, activation=tf.nn.sigmoid, input_shape=(4,)),
        Dense(3, activation = tf.nn.softmax)
        ])
    
    optimizer = tf.keras.optimizers.Adam(0.01)
    loss = tf.keras.losses.CategoricalCrossentropy()
    
    model.compile(optimizer=optimizer,loss= loss, metrics=["accuracy"] )
    model.summary()
    return model


#define a callback
class myCallbacks(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get("accuracy") > 0.97):
            print("Stopping Training.......")
            self.model.stop_training = True
        
 

#split the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

#blah-blah
stop = myCallbacks()
model = build_model()   
hist = model.fit(X_train, y_train, epochs=100, verbose=2 ,validation_split= 0.2, callbacks = [stop])


#store training data in a dataframe
history = pd.DataFrame(hist.history)
history["epoch"] = hist.epoch


#define a function to print the trainig data
def plot_history(history):
    plt.figure()
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    
    plt.plot(history["epoch"], history["accuracy"], label="Training Error")
    plt.legend(loc="best")
    
    plt.plot(history["epoch"], history["val_accuracy"], color="green", label="validation Error")
    plt.legend(loc="best")
    
    plt.show()


#plot the data
plot_history(history)    

#evaluate model
loss, accuracy = model.evaluate(X_test, y_test)
print(loss, accuracy)

