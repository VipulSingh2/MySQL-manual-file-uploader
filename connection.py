import streamlit as st
import mysql.connector

def create_connection(Host, Username, Password, Database):
    connection = None
    try:
        connection = mysql.connector.connect(host=Host, user=Username, password=Password, database=Database)
        st.success("Connected to MySQL Database Successfully")
    except mysql.connector.Error as e:
        st.error("You have entered something wrong! 😤")
    
    return connection
    
def main():
    with st.form(key='my_form'):
        st.title("MySQL Connector")
        Host = st.text_input("Host", placeholder='Host')
        Username = st.text_input("Username", placeholder='Username') 
        Password = st.text_input("Password", placeholder='Password', type='password')
        Database = st.text_input("Database")
        connect = st.form_submit_button(label='Connect it 🤝')
        
        if connect:
            if Host and Username and Password and Database:
                connection = create_connection(Host, Username, Password, Database)
            if connection:
                st.session_state['connection'] = connection
                st.write("Connected Successfully")
            else:
                st.error("Connection Failed!", icon='🥲')

if __name__ == "__main__":
    main()
