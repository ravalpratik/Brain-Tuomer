from PIL import Image
import numpy as np

# Image size for model input
IMG_SIZE = 224

# Class names based on your dataset folders
CLASS_NAMES = ["glioma", "meningioma", "notumor", "pituitary"]


def preprocess_image(uploaded_file):
    """
    Preprocess uploaded MRI image for prediction
    Steps:
    1. Open image
    2. Convert to RGB
    3. Resize to model input size
    4. Normalize pixel values to [0,1]
    5. Add batch dimension
    """

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Resize image
    image = image.resize((IMG_SIZE, IMG_SIZE))

    # Convert image to numpy array
    image_array = np.array(image, dtype=np.float32)

    # Normalize image
    image_array = image_array / 255.0

    # Add batch dimension => (1, 224, 224, 3)
    image_array = np.expand_dims(image_array, axis=0)

    return image_array


def get_class_name(class_index):
    """
    Convert predicted class index to class label
    """
    return CLASS_NAMES[class_index]