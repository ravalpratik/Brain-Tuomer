import numpy as np
import tensorflow as tf
from preprocess import preprocess_image, CLASS_NAMES

MODEL_PATH = "brain_tumor_model.h5"

# Load trained model once
model = tf.keras.models.load_model(MODEL_PATH)


def predict_brain_tumor(uploaded_file):
    """
    Predict brain tumor class from uploaded MRI image

    Returns:
        predicted_class (str): glioma / meningioma / notumor / pituitary
        confidence (float): confidence score in percentage
    """

    # Preprocess image
    processed_image = preprocess_image(uploaded_file)

    # Model prediction
    predictions = model.predict(processed_image)

    # Get predicted class index
    predicted_index = np.argmax(predictions[0])

    # Get predicted class name
    predicted_class = CLASS_NAMES[predicted_index]

    # Confidence score in %
    confidence = float(np.max(predictions[0]) * 100)

    return predicted_class, confidence