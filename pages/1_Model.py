import streamlit as st
import pandas as pd
from PIL import Image

from model import predict_brain_tumor
from advice import generate_advice
from Database import insert_prediction, fetch_all_predictions

# Page Config
st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
        .main-title {
            font-size: 38px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 10px;
        }
        .sub-title {
            font-size: 18px;
            color: #cccccc;
            text-align: center;
            margin-bottom: 30px;
        }
        .result-box {
            padding: 18px;
            border-radius: 12px;
            margin-top: 20px;
            font-size: 18px;
            font-weight: 600;
        }
        .tumor-box {
            background-color: #3b0d0d;
            color: #ffb3b3;
            border: 1px solid #ff4d4d;
        }
        .notumor-box {
            background-color: #0d2b1e;
            color: #b6ffcf;
            border: 1px solid #2ecc71;
        }
        .advice-box {
            background-color: #1e1e1e;
            padding: 18px;
            border-radius: 12px;
            margin-top: 20px;
            border: 1px solid #444;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">🧠 Brain Tumor Detection System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Upload an MRI scan image to predict tumor type and view confidence score.</div>',
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Project Info")
st.sidebar.info(
    """
    **Classes supported:**
    - Glioma
    - Meningioma
    - Pituitary
    - No Tumor

    **Tech Stack**
    - Streamlit
    - TensorFlow / Keras
    - SQLite
    """
)

st.sidebar.warning(
    "⚠️ This tool is for educational purposes only and not for real medical diagnosis."
)

# File Upload
uploaded_file = st.file_uploader(
    "Upload Brain MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Uploaded MRI Image")
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded MRI Scan", use_container_width=True)

    with col2:
        st.subheader("Prediction Result")

        if st.button("Predict Tumor"):
            with st.spinner("Analyzing MRI image..."):
                # Reset file pointer before reading in prediction
                uploaded_file.seek(0)

                # Predict
                predicted_class, confidence = predict_brain_tumor(uploaded_file)

                # Advice
                advice_text = generate_advice(predicted_class, confidence)

                # Save to DB
                insert_prediction(
                    image_name=uploaded_file.name,
                    prediction=predicted_class,
                    confidence=round(confidence, 2),
                    advice=advice_text
                )

                # Show prediction box
                if predicted_class.lower() == "notumor":
                    st.markdown(
                        f"""
                        <div class="result-box notumor-box">
                            Prediction: <b>{predicted_class.upper()}</b><br>
                            Confidence: <b>{confidence:.2f}%</b>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div class="result-box tumor-box">
                            Prediction: <b>{predicted_class.upper()}</b><br>
                            Confidence: <b>{confidence:.2f}%</b>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # Confidence Progress
                st.progress(min(int(confidence), 100))
                st.write(f"Model Confidence: **{confidence:.2f}%**")

                # Advice
                st.markdown("### Medical Advice / Suggestion")
                st.markdown(
                    f'<div class="advice-box">{advice_text}</div>',
                    unsafe_allow_html=True
                )



# Footer
st.markdown("---")
st.caption("Built with Streamlit + Deep Learning + SQLite")