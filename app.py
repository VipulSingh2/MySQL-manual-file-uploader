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
        try:
                module = import_module(page)
                module.main()
        except ModuleNotFoundError:
                st.error(f"Module '{page}' not found.")
        except AttributeError:
                st.error(f"The module '{page}' does not have a 'main' function.")
        except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

if __name__=="__main__":
        main()
