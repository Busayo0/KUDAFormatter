import os
import time

try:
    os.system("start cmd /k streamlit run app.py")
except Exception as e:
    print("Failed to launch Streamlit:", e)
    time.sleep(10)
