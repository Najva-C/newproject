import tensorflow as tf
from tensorflow.keras import layers,models
import matpotlib.pyplot as plt


#LOAD DATASET (MNIT IS BUILT-IN)
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data()


# NORMALISE DATA (SCALE PIXEL VALUES TO 0.1)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32")  /255.0

# RESHAPE DATA(CNN EXPECTS 3D:HEIGHT,WIDTH,CHANNELS)
x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)