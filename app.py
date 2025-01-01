import streamlit as st
from importlib import import_module
def main():
    pages = {
        "MySQL connector ⚙️ ": "connection",
        "Uploader 💻": "uploader",
        
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to",list(pages.keys()))
    page = pages[selection]
    module = import_module(page)
    module.main()
    
if __name__=="__main__":
    main()
