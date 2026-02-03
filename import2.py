import pandas as pd
import streamlit as st
import os

# Configure page
st.set_page_config(page_title="Pandas Operations", layout="wide")

# Try to load logo - with error handling
logo_path = r"C:\Users\Swati\AI-ML\Deployment\Streamlit - Demo\project 1\Pandas Project\csv1proj\Images\logo.png"

# Check if logo exists
if os.path.exists(logo_path):
    try:
        # Display logo with title
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(logo_path, width=120)
        with col2:
            st.markdown("# Pandas Operations with Python")
    except Exception as e:
        st.warning(f"Could not load logo: {e}")
        st.title("Pandas Operations with Python")
else:
    st.title("Pandas Operations with Python")

st.header("Session-based File Upload")

# ---------------- Sidebar ----------------
upload_img_path = r"C:\Users\Swati\AI-ML\Deployment\Streamlit - Demo\project 1\Pandas Project\csv1proj\Images\upload.jpg"

if os.path.exists(upload_img_path):
    try:
        st.sidebar.image(upload_img_path, width=300)
    except:
        pass

st.sidebar.title("File Upload")

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

if "df" not in st.session_state:
    st.session_state.df = None

file1 = st.sidebar.file_uploader(
    "Upload CSV / Excel file",
    type=["csv", "xlsx", "xls"]
)

if file1 is not None:
    st.session_state.uploaded_file = file1
    st.sidebar.success("File uploaded successfully!")

# -------------------------------------------------
# HORIZONTAL SECTION 1 (TOP) – Uploaded file preview
# -------------------------------------------------

top_section = st.container()

with top_section:
    st.write("Please expand to see the uploaded file")

    with st.expander("Uploaded File"):
        if st.session_state.uploaded_file is not None:
            uploaded_file = st.session_state.uploaded_file

            try:
                if uploaded_file.name.endswith(('.xlsx', '.xls')):
                    st.session_state.df = pd.read_excel(uploaded_file)

                elif uploaded_file.name.endswith('.csv'):
                    st.session_state.df = pd.read_csv(uploaded_file)

                else:
                    st.error("Unsupported file format")
                    st.session_state.df = None

                if st.session_state.df is not None:
                    st.dataframe(st.session_state.df.head())

            except Exception as e:
                st.error(f"Error reading file: {e}")
                st.session_state.df = None
        else:
            st.info("No file uploaded yet. Please upload a file from the sidebar.")

st.divider()

# -------------------------------------------------
# HORIZONTAL SECTION 2 (BOTTOM) – Operations
# -------------------------------------------------

bottom_section = st.container()

with bottom_section:
    if st.session_state.df is not None:

        choice1 = st.radio(
            "Choose an operation",
            ("Describe", "Count NA in data", "Shape")
        )

        st.write("You selected:", choice1)

        try:
            df = st.session_state.df

            if choice1 == "Describe":
                st.write(df.describe())

            elif choice1 == "Count NA in data":
                st.write(df.isna().sum())

            elif choice1 == "Shape":
                st.write(f"Shape of the DataFrame: {df.shape}")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

    else:
        st.warning("Please upload a file to enable operations.")