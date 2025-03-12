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

def set_custom_css():
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #2d3e50, #4c5c6d);
                color: #ffffff;
            }
            .sidebar .sidebar-content {
                background-color: #2d3e50;
                color: #ffffff;
                border-radius: 8px;
                padding: 20px;
            }
            .sidebar input, .sidebar select, .sidebar textarea {
                background-color: #374a63;
                color: #ffffff;
                border-radius: 4px;
            }
            .sidebar .css-1d391kg {
                background-color: #4c5c6d !important;
                border: none;
                color: white;
            }
            .stButton>button {
                background-color: #1e90ff;
                color: white;
                border-radius: 8px;
                border: none;
                width: 100%;
                height: 50px;
                font-size: 18px;
            }
            .stButton>button:hover {
                background-color: #003366;
                transition: all 0.3s;
            }
            .stButton>button:active {
                background-color: #004080;
            }
            .stImage {
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            }
        </style>
    """, unsafe_allow_html=True)

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