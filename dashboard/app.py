#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("G:/DSP DATA SET/new saved data/df_dashboard_final_with_shap_direction.csv")

# Page settings
st.set_page_config(page_title="Student Dropout Risk Prediction", layout="wide")
st.title("🎓 Student Dropout Risk Prediction")
st.markdown("Select a student to view predicted dropout probability and feature importance (SHAP).")

# Select a student
student_ids = df['id_student'].unique()
selected_id = st.selectbox("Select Student ID:", sorted(student_ids))

# Get student data
student_row = df[df['id_student'] == selected_id].iloc[0]

# Student info display
st.subheader("📌 Student Information")
info_cols = ['gender_x', 'region_x', 'highest_education_x',
             'imd_band_x', 'age_band_x', 'disability_x']

info_labels = {
    'gender_x': "Gender",
    'region_x': "Region",
    'highest_education_x': "Highest education",
    'imd_band_x': "Imd band",
    'age_band_x': "Age band",
    'disability_x': "Disability"
}

for col in info_cols:
    label = info_labels.get(col, col.replace("_x", "").capitalize())
    value = student_row[col]
    st.markdown(f"**{label}:** {value}")

# Show prediction
st.subheader("📈 Model Prediction")
prob = student_row['dropout_probability']
st.metric("Predicted Dropout Probability", f"{prob:.2%}")

# SHAP explanation section
st.subheader("💡 SHAP Top Contributing Features")

# Dynamically find SHAP columns with arrow marks (↑ or ↓)
shap_cols = [col for col in df.columns if ('↑' in col or '↓' in col)]

# If no SHAP features found, show warning
if not shap_cols:
    st.warning("No SHAP features with arrows (↑/↓) found in the dataset.")
else:
    # Slider to choose number of top features
    top_n = st.slider("Number of SHAP features to show:", min_value=3, max_value=10, value=5)

    # Get current student's SHAP values and sort by absolute value
    shap_values = student_row[shap_cols]
    shap_top = shap_values.abs().sort_values(ascending=False).head(top_n)
    top_features = shap_top.index.tolist()

    # Format into table
    shap_table = pd.DataFrame({
        'Feature': top_features,
        'SHAP Value': student_row[top_features].values
    })

    # Show table
    st.dataframe(shap_table, use_container_width=True)

    # Optional: show bar chart
    st.bar_chart(shap_table.set_index('Feature')['SHAP Value'])


# In[ ]:




