import streamlit as st
import pandas as pd
from Database import fetch_all_predictions, delete_prediction,clear_all_predictions

# Page Config
st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="wide"
)

# Prediction History
st.title("📜 Prediction History")

history_data = fetch_all_predictions()

if history_data:
    df = pd.DataFrame(
        history_data,
        columns=["ID", "Image Name", "Prediction", "Confidence", "Advice", "Prediction Time"]
    )
    st.dataframe(df, use_container_width=True)
else:
    st.info("No prediction history found yet.")

# Prediction History
# st.markdown('<div class="history-title">📜 Prediction History</div>', unsafe_allow_html=True)

# history_data = fetch_all_predictions()

# if history_data:
#     df = pd.DataFrame(
#         history_data,
#         columns=["ID", "Image Name", "Prediction", "Confidence", "Advice", "Prediction Time"]
#     )
#     st.dataframe(df, use_container_width=True)
# else:
#     st.info("No prediction history found yet.")

col1,col2 = st.columns(2)
with col1:
    if st.button("Delete Row"):
        id = int(st.number_input("Enter Id to delete a Row"))
        delete_prediction(id)
with col2:
    if st.button("Clear All Data"):
        clear_all_predictions()
