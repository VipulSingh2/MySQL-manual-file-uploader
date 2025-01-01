import streamlit as st
from importlib import import_module


def mysql_connector_page():
    # Implement logic for MySQL database connection here
    st.write("This is the MySQL connector page.")


def uploader_page():
    # Implement file upload functionality here
    st.write("This is the Uploader page.")


def main():
    pages = {
        "MySQL Database Connection": mysql_connector_page,
        "File Uploader": uploader_page,
    }

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))
    selected_page()

if __name__ == "__main__":
    main()
