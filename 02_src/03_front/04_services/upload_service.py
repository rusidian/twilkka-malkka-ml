from io import BytesIO
import pandas as pd

def load_uploaded_dataframe(uploaded_file) -> pd.DataFrame:
    if uploaded_file is None:
        raise ValueError("업로드된 파일이 없습니다.")

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        uploaded_file.seek(0)
        return pd.read_csv(uploaded_file)

    if file_name.endswith(".xlsx"):
        return pd.read_excel(BytesIO(uploaded_file.getvalue()))

    raise ValueError("csv 또는 xlsx 파일만 지원합니다.")