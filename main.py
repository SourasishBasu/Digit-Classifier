import gradio as gr
import numpy as np
import tensorflow as tf

# Load MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalize data

# Build a simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])
model.compile(optimizer='adam',
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

def classify_digit(img):
    img = img.reshape(1, 28, 28)
    prediction = model.predict(img).tolist()[0]
    return {str(i): prediction[i] for i in range(10)}

# Gradio UI
interface = gr.Interface(fn=classify_digit,
                         inputs="sketchpad",
                         outputs="label")
interface.launch()