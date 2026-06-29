def generate_advice(predicted_class, confidence):
    """
    Generate advice based on predicted tumor class and confidence score.

    Args:
        predicted_class (str): glioma / meningioma / notumor / pituitary
        confidence (float): prediction confidence in percentage

    Returns:
        str: advice message
    """

    predicted_class = predicted_class.lower()

    # Common warning for low confidence
    low_confidence_note = ""
    if confidence < 70:
        low_confidence_note = (
            "\n\n⚠️ The model confidence is low. "
            "Please verify with a medical professional and, if possible, use a clearer MRI image."
        )

    if predicted_class == "notumor":
        return (
            "✅ No tumor detected by the model.\n\n"
            "This means the uploaded MRI image does not show strong signs of a brain tumor according to the trained model. "
            "However, this system is only for educational purposes and is not a medical diagnosis tool. "
            "If the patient has symptoms such as severe headaches, seizures, vomiting, vision problems, or neurological issues, "
            "please consult a neurologist or radiologist for proper medical evaluation."
            + low_confidence_note
        )

    elif predicted_class == "glioma":
        return (
            "⚠️ The model predicts **Glioma tumor**.\n\n"
            "Glioma is a type of brain tumor that develops from glial cells in the brain. "
            "It may require urgent medical attention depending on its type and severity. "
            "Please consult a neurologist, neurosurgeon, or radiologist as soon as possible for proper diagnosis, MRI review, and treatment planning. "
            "Do not rely only on this AI prediction."
            + low_confidence_note
        )

    elif predicted_class == "meningioma":
        return (
            "⚠️ The model predicts **Meningioma tumor**.\n\n"
            "Meningioma is a tumor that forms in the membranes surrounding the brain and spinal cord. "
            "Many meningiomas grow slowly, but they still require professional medical evaluation. "
            "Please consult a neurologist or neurosurgeon for proper diagnosis, MRI interpretation, and next steps."
            + low_confidence_note
        )

    elif predicted_class == "pituitary":
        return (
            "⚠️ The model predicts **Pituitary tumor**.\n\n"
            "Pituitary tumors occur in the pituitary gland and may affect hormone balance, vision, headaches, and other body functions. "
            "A specialist consultation with a neurologist, endocrinologist, or neurosurgeon is strongly recommended for further medical examination."
            + low_confidence_note
        )

    else:
        return (
            "Unable to generate advice for this prediction result. "
            "Please consult a medical professional for further evaluation."
        )