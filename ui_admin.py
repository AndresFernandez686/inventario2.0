import streamlit as st
import pandas as pd
from datetime import datetime

def df_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

def admin_inventario_ui(inventario):
    st.header("Inventario (vista administrador)")
    for categoria, productos in inventario.items():
        st.subheader(f"{categoria}")
        st.dataframe(pd.DataFrame(productos.items(), columns=["Producto", "Cantidad"]))

def admin_historial_ui(historial):
    st.header("Historial de movimientos")
    if not historial:
        st.info("No hay registros en el historial.")
        return

    df = pd.DataFrame(historial)
    if "fecha" in df.columns:
        df["Fecha"] = pd.to_datetime(df["fecha"])
    else:
        df["Fecha"] = pd.NaT

    st.dataframe(df)
    filtro = df.copy()

    empleado_sel = st.selectbox("Filtrar por empleado", ["Todos"] + sorted(df["usuario"].unique()))
    if empleado_sel != "Todos":
        filtro = filtro[filtro["usuario"] == empleado_sel]

    if "Fecha" in filtro.columns:
        mes = st.number_input("Mes", 1, 12, value=datetime.now().month)
        año = st.number_input("Año", 2000, 2100, value=datetime.now().year)
        filtro = filtro[(filtro["Fecha"].dt.month == mes) & (filtro["Fecha"].dt.year == año)]

    if not filtro.empty:
        st.dataframe(filtro.sort_values("Fecha"))
        csv_bytes = df_to_csv_bytes(filtro)
        st.download_button(
            label="Descargar historial filtrado (CSV)",
            data=csv_bytes,
            file_name=f"historial_{empleado_sel}_{mes:02d}_{año}.csv".replace(" ", "_"),
            mime="text/csv"
        )
    else:
        st.warning("No hay registros con ese filtro.")
