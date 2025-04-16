import subprocess
import sys

try:
    subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py"])
except Exception as e:
    import time
    print("Failed to start Streamlit:", e)
    time.sleep(10)
