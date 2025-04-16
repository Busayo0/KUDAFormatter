# KUDAFormatter

A lightweight Streamlit app that:
- Uploads `.txt` transaction files from KUDA
- Masks PANs (first 6, last 4 visible)
- Maps headers based on standard codes
- Allows export to CSV

## 🔧 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📦 To build Windows EXE (via GitHub Actions)

GitHub Actions automatically builds a Windows `.exe` and uploads it to the Actions tab.
