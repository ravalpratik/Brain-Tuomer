About Dataset

Overview
A brain tumor is an abnormal growth of cells within the brain. Due to the rigid structure of the skull, any abnormal growth can increase intracranial pressure and potentially lead to severe neurological damage. Early detection and accurate classification of brain tumors are critical for selecting appropriate treatment strategies and improving patient outcomes.

This dataset is designed to support research in medical image analysis and deep learning–based brain tumor classification using MRI scans.

Dataset Description
The dataset contains 7,200 human brain MRI images categorized into four classes:

Glioma
Meningioma
Pituitary tumor
No tumor
The dataset is structured into training and testing sets with balanced class distributions.

Dataset Structure
Training/
    glioma/        (1400 images)
    meningioma/    (1400 images)
    pituitary/     (1400 images)
    notumor/       (1400 images)

Testing/
    glioma/        (400 images)
    meningioma/    (400 images)
    pituitary/     (400 images)
    notumor/       (400 images)

Data Sources
This dataset is a curated combination of the following publicly available datasets:

figshare brain MRI dataset
SARTAJ dataset
Br35H dataset
Images in the no tumor class were sourced from the Br35H dataset.

During dataset preparation, inconsistencies were observed in the glioma class of the SARTAJ dataset. To improve label reliability, those images were removed and replaced with verified glioma images from the figshare dataset.

Version 2 Updates
Removed duplicate images
Balanced classes (1400 training / 400 testing per class)
Eliminated overlap between training and testing sets to prevent data leakage

https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data