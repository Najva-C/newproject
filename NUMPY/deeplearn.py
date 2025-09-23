import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

#PREPROCESSING
#LOAD DATASET (MNIT IS BUILT-IN)
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data()


# NORMALISE DATA (SCALE PIXEL VALUES TO 0.1)  
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32")  /255.0

# RESHAPE DATA(CNN EXPECTS 3D:HEIGHT,WIDTH,CHANNELS)
x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)

# BUILD A SIMPLE CNN MODEL(LAYERS)
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (28,28,1)),      #relu gives 0 output for 0/-ve and same number for +ve ,convolution
    layers.MaxPooling2D((2,2)),            #pooling layer
    layers.Flatten(),                      #flatten into 1D
    layers.Dense(64,activation = 'relu'),          #fully connected layer
    layers.Dense(10, activation = 'softmax')       #output layer (10 claases)
])

# COMPILE MODEL
model.compile(optimizer = 'adam',     #Adaptive Moment Estimation(ADAM)
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# TRAIN THE MODEL
history = model.fit(
    x_train, y_train,
    epochs = 5,          #how many times the value needs to pass through network . if bigger value then time increases accuracy also increases 
    batch_size = 64,             #faster training
    validation_data = (x_test,y_test),
    verbose = 1       #shows progress bar of each output visibility ,1 if want to show and 0 if dont want to show
)

# EVALUATE ON TEST DATA
test_loss, test_acc = model.evaluate(x_test, y_test, verbose = 0)
print("Test Accuracy: ", round(test_acc * 100, 2), "%")

# PREDICT EXAMPLE
prediction = model.predict(x_test[:1])       #get prediction probabilities
predicted_label = prediction.argmax()        #find the most likely class

plt.imshow(x_test[0].reshape(28,28), cmap = "gray")
plt.title("Prediction: " +str(predicted_label))
plt.axis("off")
plt.show()

