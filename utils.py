import streamlit as st
import re

def validate_product_description(description):
    """Validate if the product description seems reasonable."""
    description = description.strip()

    if len(description.split()) < 5:
        return False

    if not re.search(r'[a-zA-Z]', description):
        return False

    non_alphabetic = sum(1 for char in description if not char.isalpha() and not char.isspace())
    total_chars = len(description.replace(" ", ""))

    if total_chars > 0 and non_alphabetic / total_chars > 0.7:
        return False

    return True

def set_sidebar_css():
    st.markdown("""
    <style>
    /* Sidebar background */
    .sidebar .sidebar-content {
        background-color: #f7f7f7;
    }
    /* Sidebar text color */
    .sidebar p, .sidebar .css-ffhzg2 {
        color: #333333 !important;
    }
    .sidebar .block-container {
        padding-top: 1rem;
        padding-right: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)