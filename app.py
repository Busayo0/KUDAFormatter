import pandas as pd
import streamlit as st

column_mapping = {
    "A": "maskpan", "B": "bank", "C": "tid", "D": "code_message",
    "E": "customer_identification_number", "F": "transaction_type_code",
    "G": "approved_status_code", "H": "represent_code", "I": "currency_code",
    "K": "settlement_amount", "L": "transaction_type", "M": "settlement_date",
    "N": "transaction_date", "Q": "transaction_amount", "S": "constant",
    "T": "country_currency_amount", "U": "constant_to_different_channels",
    "V": "transaction_channel_type", "W": "merchant_narration",
    "X": "country_currency_code", "Z": "authorization_code",
    "AA": "acquirer_reference_number", "AM": "issuer_reference_number"
}

def mask_pan(pan):
    pan = pan.strip()
    return pan[:6] + "*" * (len(pan) - 10) + pan[-4:] if len(pan) >= 10 else pan

st.title("KUDA TXT File Formatter")

uploaded_file = st.file_uploader("Upload KUDA .txt File", type=["txt"])
if uploaded_file:
    lines = uploaded_file.readlines()
    data = [line.decode("utf-8").strip().split("|") for line in lines]
    for row in data:
        while len(row) < 44:
            row.append("")

    df = pd.DataFrame(data)
    df[0] = df[0].apply(mask_pan)

    excel_headers = [chr(65+i) if i < 26 else "A" + chr(65+i-26) for i in range(len(df.columns))]
    new_headers = [column_mapping.get(h, f"col_{i+1}") for i, h in enumerate(excel_headers)]
    df.columns = new_headers

    st.dataframe(df)

    if st.button("Export as CSV"):
        df.to_csv("data/output.csv", index=False)
        st.success("Exported to data/output.csv")
