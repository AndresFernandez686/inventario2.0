#Utilidades generales (conversiones de datos y helpers)
import pandas as pd
from io import BytesIO

def df_to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")

def df_to_excel_bytes(df: pd.DataFrame) -> bytes:
    """Convierte un DataFrame a bytes de Excel (.xlsx)"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Datos')
    output.seek(0)
    return output.getvalue()

# Puedes agregar aquí más utilidades generales 
