import pandas as pd
import streamlit as st

st.title("Pandas Operations with Python")
st.header("Session-based File Upload")

# ---------------- Sidebar ----------------
st.sidebar.title("File Upload")

# Initialize session state
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
# -----------------------------------------

row1, row2 = st.rows(2)

with col1:
    st.write("Please expand to see the uploaded file")


with st.expander("Uploaded File"):
    if st.session_state.uploaded_file is not None:
        uploaded_file = st.session_state.uploaded_file

        if uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)

        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)

        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            df = None

        if df is not None:
            st.dataframe(df.head())
    else:
        st.info("No file uploaded yet. Please upload a file from the sidebar.")

# ---------------- Operations ----------------

if "df" not in st.session_state:
    st.session_state.df = None

with row2:
    choice1 = st.radio("Choose an operation", ("Describe", "Info", "Shape"))
    st.write("You selected:", choice1)

try:
    df = st.session_state.df

    if df is None:
        raise ValueError("Please upload a file first")

    if choice1 == "Describe":
        st.write(df.describe())

    elif choice1 == "Info":
        buffer = []
        df.info(buf=buffer)
        st.text("\n".join(buffer))

    elif choice1 == "Shape":
        st.write(f"Shape of the DataFrame: {df.shape}")

except ValueError as e:
    st.warning(e)

except Exception as e:
    st.error(f"Something went wrong: {e}")


