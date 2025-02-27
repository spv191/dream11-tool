import streamlit as st
import traceback

try
st.title("Dream11 AI Strategy Tool")  
st.write("📊 Analyze player stats, past performances & optimize your team.")  

st.text_input("Enter Player Name")  
st.button("Analyze Player")
st.write(App is running...")

except Exception as e:
st error(f"Error:{str(e)}")#Display error in the app
st.text((traceback.format_exc())show full error details
