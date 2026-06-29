import streamlit as st
import os

# Page Config
st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 About Brain Tumor Detection System")

st.write("""
The **Brain Tumor Detection System** is a Deep Learning application that classifies
brain MRI images into four categories using a **Convolutional Neural Network (CNN)**.

The system predicts whether an MRI scan belongs to one of the following classes:

- 🟢 No Tumor
- 🔴 Glioma
- 🟡 Meningioma
- 🔵 Pituitary Tumor

This project is developed for educational and research purposes to demonstrate
the application of Artificial Intelligence in medical image classification.

**Note:** This application should not be used as a replacement for professional medical diagnosis.
""")

st.divider()

# Objectives
st.header("🎯 Project Objectives")

st.markdown("""
- Detect brain tumors from MRI images.
- Classify MRI scans into four categories.
- Display prediction confidence.
- Store prediction history in SQLite.
- Demonstrate Deep Learning using CNN.
""")

st.divider()

# Dataset
st.header("📊 Dataset Information")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Training Dataset")
    st.table({
        "Class": [
            "Glioma","Meningioma","Pituitary","No Tumor"
        ],
        "Images": [
            1400,1400,1400,1400
        ]
    })
    st.success("Total Training Images : 5,600")

with col2:
    st.subheader("Testing Dataset")
    st.table({
        "Class": [
            "Glioma","Meningioma","Pituitary","No Tumor"
        ],
        "Images": [
            400,400,400,400
        ]
    })
    st.success("Total Testing Images : 1,600")

st.divider()

# Image Preprocessing
st.header("🧹 Image Preprocessing")

st.markdown("""
Before training, every MRI image undergoes preprocessing to improve model performance.

- Resize all images to the same dimensions
- Normalize pixel values
- Convert images into NumPy arrays
- Encode labels
- Prepare data for CNN training
""")

st.divider()

# CNN Architecture
st.header("🧠 CNN Model Architecture")

st.code("""
Input (128 × 128 × 3)
↓    
Conv2D (32 Filters)
BatchNormalization
MaxPooling
↓
Conv2D (64 Filters)
BatchNormalization
MaxPooling
↓
Conv2D (128 Filters)
BatchNormalization
MaxPooling
↓
Conv2D (256 Filters)
BatchNormalization
MaxPooling
↓
Flatten
↓
Dense (256)
↓
Dropout (0.5)
↓
Dense (4)
↓
Softmax Output
""")

st.write("### Model Summary")

st.code("""
Conv2D(32, activation='relu')
BatchNormalization()
MaxPooling2D()

Conv2D(64, activation='relu')
BatchNormalization()
MaxPooling2D()

Conv2D(128, activation='relu')
BatchNormalization()
MaxPooling2D()

Conv2D(256, activation='relu')
BatchNormalization()
MaxPooling2D()

Flatten()

Dense(256, activation='relu')

Dropout(0.5)

Dense(4, activation='softmax')
""")

st.divider()

# Training Configuration
st.header("⚙️ Training Configuration")

st.table({
    "Parameter": [
        "Model","Epochs","Optimizer","Loss Function","Output Classes"
    ],
    "Value": [
        "CNN","15","Adam","Categorical Crossentropy","4"
    ]
})

st.divider()

# Training Graphs
st.header("📈 Model Training Performance")

accuracy_path = "Reports/Figure_1.png"
loss_path = "Reports/Figure_2.png"

if os.path.exists(accuracy_path):
    st.subheader("Training vs Validation Accuracy")
    st.image(accuracy_path)

if os.path.exists(loss_path):
    st.subheader("Training vs Validation Loss")
    st.image(loss_path)


st.subheader("Performance Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Training Accuracy", "~71%")
    st.metric("Training Loss", "~0.70")

with col2:
    st.metric("Validation Accuracy", "~68%")
    st.metric("Validation Loss", "~0.72")

st.info("""
### Observations

• Training accuracy increased steadily throughout training.
        
• Validation accuracy followed a similar trend.

• Training loss consistently decreased.

• Validation loss showed minor fluctuations, which is common in deep learning.

• The model demonstrates stable learning with only slight signs of overfitting.
""")

st.divider()

# Workflow
st.header("🔄 Prediction Workflow")

st.code("""
MRI Image Upload
↓
Image Preprocessing
↓
CNN Feature Extraction
↓
Classification
↓
Prediction
↓
Confidence Score
↓
Medical Advice
↓
Store in SQLite Database
""")

st.divider()

# Features
st.header("🚀 Features")

st.markdown("""
- MRI Image Upload
- CNN-based Brain Tumor Classification
- Four-Class Prediction
- Confidence Score
- Tumor-specific Advice
- Prediction History
- SQLite Database
- Streamlit User Interface
""")

st.divider()

# Database
st.header("💾 Prediction History")

st.write("""
Every prediction is automatically saved in an SQLite database.

Stored information includes:

- Predicted Tumor Type
- Confidence Score
- Uploaded Image
- Date and Time
""")

st.divider()

# Technologies
st.header("🛠 Technologies Used")

st.table({
    "Technology": [
        "Python",
        "TensorFlow",
        "Keras",
        "OpenCV",
        "NumPy",
        "Streamlit",
        "SQLite",
        "Matplotlib"
    ],
    "Purpose": [
        "Programming Language",
        "Deep Learning Framework",
        "CNN Development",
        "Image Processing",
        "Numerical Computing",
        "Web Application",
        "Database",
        "Training Visualization"
    ]
})

st.divider()

# Conclusion
st.header("📚 Conclusion")

st.write("""
The Brain Tumor Detection System demonstrates how a Convolutional Neural Network (CNN)
can classify brain MRI images into **Glioma**, **Meningioma**, **Pituitary**, and **No Tumor**
categories. The project integrates image preprocessing, deep learning, prediction history,
and an interactive Streamlit interface to create a complete end-to-end AI application.

While the model achieves encouraging performance on the available dataset, it is intended
for educational and research purposes only. Clinical decisions should always be made by
qualified healthcare professionals.
""")

st.write("""
---
© **2026 RAVAL PRATIK**. All Rights Reserved.

This **Brain Tumor Detection System** was designed and developed by **Raval Pratik Dilipbhai**
as a **Bachelor of Computer Applications (BCA) - Artificial Intelligence** 5th sem project at
**Vivekanand College of Computer Science & Management, Surat**.

The successful completion of this project was made possible through the valuable guidance,
continuous support, and encouragement of **Prof. Sumati Ma'am** and **Prof. Hiral Ma'am**.
Their expertise and mentorship played a significant role throughout the development of this project.

This project is intended solely for **educational and research purposes** and should not be used
as a substitute for professional medical diagnosis or clinical decision-making.
""")