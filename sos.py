import json 
import requests 

import time
import requests
import subprocess
import streamlit as st
from streamlit_lottie import st_lottie_spinner

st.title("ALERT !🚨")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie = load_lottiefile("Animation - 1731325019108.json")
c=True
while True:
    with st_lottie_spinner(lottie, loop=True,width =400):
        time.sleep(10)
        st.write("Request is sending....")
        subprocess.run(['python','mail.py'])
        
    
        break 
st.success("Message sent successfully")

