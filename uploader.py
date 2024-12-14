import streamlit as st
import pandas as pd

def main():
    if 'connection' not in st.session_state:
            st.warning("Please connect to the database first")
            return
    with st.form(key='uploader'):
        st.title("File Uploader")
        table_name = st.text_input("Table Name:",placeholder="Name your Table")
        table = st.file_uploader("Upload your file must be csv format")
        Submit = st.form_submit_button(label = 'Upload it👍')
            
    if Submit and table is not None:
        data = pd.read_csv(table)
        st.dataframe(data)
        connection = st.session_state['connection']
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                
        columns = data.columns.tolist()
        columns_with_types = ", ".join([f"{col} TEXT" for col in columns])
        create_table_query = f"CREATE TABLE {table_name} ({columns_with_types})"
        cursor.execute(create_table_query)
            
            # Insert data
        for _, row in data.iterrows():
            values = tuple(row)
            insert_query = f"INSERT INTO {table_name} VALUES {values}"
            cursor.execute(insert_query)
            
            connection.commit()
            st.success(f"Table '{table_name}' created and data uploaded successfully.")   
                
if __name__ == "__main__":
    main()