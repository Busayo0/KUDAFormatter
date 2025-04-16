import os
import sys
import subprocess

try:
    subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py"])
except Exception as e:
    import time
    print("Error launching app:", e)
    time.sleep(10)
