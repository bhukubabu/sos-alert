import json 
import requests 
import mail
import time
import requests
import subprocess
import streamlit as st
from streamlit_lottie import st_lottie_spinner

if "email_sent" not in st.session_state:
    st.session_state.email_sent= False 
st.title("ALERT !🚨")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie = load_lottiefile("Animation - 1731325019108.json")
c=True
if not st.session_state.email_sent: 
      with st_lottie_spinner(lottie, loop=True,width =400):
           time.sleep(10)
        #st.write("Request is sending....")
        #subprocess.run(['python','mail.py'])
           #mail.start()
           st.session_state.email_sent=True
            #break 
      st.success("Message sent successfully")
else: 
     st.info("Email has sent already")
            #break

