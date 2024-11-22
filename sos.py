import json 
import requests 
#import mail
import time
import requests
import subprocess
import streamlit as st
from streamlit_lottie import st_lottie_spinner


st.title("ALERT !🚨")

def load_lottiefile2(file_path:str):
      with open(file_path,"r") as file:
            return json.load(file)
def load_lottiefile1(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie = load_lottiefile1("Animation - 1731325019108.json")
c=True
#if not st.session_state.email_sent: 
with st_lottie_spinner(lottie, loop=True,width =400):
          time.sleep(10)
          subprocess.run(["python","mail.py"])
          #st.session_state.email_sent=True
          #break 
st.success("Message sent successfully")
#else: 
#    st.info("Email has sent already")
            #break

