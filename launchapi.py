from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

interpreter = tf.lite.Interpreter(model_path="model_unquant.tflite")
interpreter.allocate_tensors()

def predict(input_data):

    input_details = interpreter.get_input_details()
    input_shape = input_details[0]['shape']

    input_data = np.array(input_data, dtype=np.float32)
    input_data = np.expand_dims(input_data, axis=0)

    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    output_details = interpreter.get_output_details()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Load class names from labels.txt file
    with open("labels.txt", "r") as f:
        class_names = f.read().splitlines()

    prediction_index = np.argmax(output_data[0])
    prediction_class = class_names[prediction_index]

    return prediction_class


def preprocess_image(image):

    target_size = (224, 224)  
    image = image.resize(target_size)

    image_np = np.array(image)
 
    image_np = image_np / 255.0
    

    if len(image_np.shape) > 2:
        image_np = image_np[..., :3] 
    
    return image_np


@app.route("/predict", methods=["POST"])
def inference():
    if request.method == "POST":
    
        data = request.json.get("data")
        img_data = base64.b64decode(data)
        image = Image.open(BytesIO(img_data))

        image_np = preprocess_image(image)

        prediction = predict(image_np)

        return jsonify({"ans": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    