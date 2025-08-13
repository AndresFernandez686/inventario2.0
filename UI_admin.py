#UI y logica para administradores (inventario,historial,delivery)
import streamlit as st
from datetime import date
from utils import df_to_csv_bytes

def admin_inventario_ui(inventario):
    st.header("Inventario total por categoría")
    total_general = 0
    for categoria, productos in inventario.items():
        st.subheader(f"Categoría: {categoria}")
        total_categoria = sum(productos.values())
        total_general += total_categoria
        for p, c in productos.items():
            texto = f"{c:.2f} kilos" if categoria == "Por Kilos" and c > 0 else (str(c) if c > 0 else "Vacío")
            st.write(f"- {p}: {texto}")
        if categoria == "Por Kilos":
            st.markdown(f"**Total en {categoria}: {total_categoria:.2f} kilos**")
        else:
            st.markdown(f"**Total en {categoria}: {int(total_categoria)}**")
    st.markdown(f"## Total general: {total_general:.2f}")

    st.divider()
    st.subheader("Descargar inventarios por categoría (CSV)")
    for categoria, productos in inventario.items():
        import pandas as pd
        df = pd.DataFrame({
            "Producto": list(productos.keys()),
            "Cantidad": list(productos.values())
        })
        csv_bytes = df_to_csv_bytes(df)
        st.download_button(
            label=f"Descargar CSV de {categoria}",
            data=csv_bytes,
            file_name=f"inventario_{categoria.lower().replace(' ', '_')}.csv",
            mime="text/csv"
        )

def admin_historial_ui(cargar_historial):
    st.header("📅 Historial de cargas (por empleado / mes)")
    historial = cargar_historial()
    if historial.empty:
        st.info("Aún no hay registros en el historial.")
        return

    empleados = ["Todos"] + sorted(historial["Usuario"].dropna().unique().tolist())
    empleado_sel = st.selectbox("Empleado", empleados)
    año = st.number_input("Año", min_value=2000, max_value=2100, value=date.today().year)
    mes = st.number_input("Mes", min_value=1, max_value=12, value=date.today().month)

    filtro = historial.copy()
    filtro = filtro[(filtro["Fecha"].dt.year == año) & (filtro["Fecha"].dt.month == mes)]
    if empleado_sel != "Todos":
        filtro = filtro[filtro["Usuario"] == empleado_sel]

    if not filtro.empty:
        st.dataframe(filtro.sort_values("Fecha"))
        from utils import df_to_csv_bytes
        csv_bytes = df_to_csv_bytes(filtro)
        st.download_button(
            label="Descargar historial filtrado (CSV)",
            data=csv_bytes,
            file_name=f"historial_{empleado_sel}_{mes:02d}_{año}.csv".replace(" ", "_"),
            mime="text/csv"
        )
    else:
        st.warning("No hay registros con ese filtro.")

def admin_delivery_ui(cargar_catalogo_delivery, guardar_catalogo_delivery, cargar_ventas_delivery):
    st.header("Gestión de Delivery (catálogo y ventas)")
    st.subheader("Catálogo de productos de delivery")
    catalogo = cargar_catalogo_delivery()

    with st.expander("Agregar nuevo producto de delivery"):
        nombre = st.text_input("Nombre del producto (ej: Promo 2x1 Chocolate)")
        es_promocion = st.checkbox("¿Es promoción?", value=False)
        activo = st.checkbox("Activo", value=True)
        if st.button("Guardar producto"):
            if not nombre.strip():
                st.error("El nombre no puede estar vacío.")
            else:
                if any(p["nombre"].lower() == nombre.strip().lower() for p in catalogo):
                    st.warning("Ya existe un producto con ese nombre.")
                else:
                    catalogo.append({
                        "nombre": nombre.strip(),
                        "es_promocion": bool(es_promocion),
                        "activo": bool(activo)
                    })
                    guardar_catalogo_delivery(catalogo)
                    st.success("Producto agregado al catálogo.")

    if catalogo:
        st.write("Productos actuales:")
        import pandas as pd
        df_cat = pd.DataFrame(catalogo)
        st.dataframe(df_cat)

        st.subheader("Editar / Eliminar")
        nombres = [c["nombre"] for c in catalogo]
        sel = st.selectbox("Selecciona un producto", nombres)
        idx = nombres.index(sel)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            nuevo_activo = st.checkbox("Activo", value=catalogo[idx].get("activo", True), key="edit_activo")
        with col2:
            nuevo_promo = st.checkbox("Promoción", value=catalogo[idx].get("es_promocion", False), key="edit_promo")
        with col3:
            if st.button("Guardar cambios"):
                catalogo[idx]["activo"] = nuevo_activo
                catalogo[idx]["es_promocion"] = nuevo_promo
                guardar_catalogo_delivery(catalogo)
                st.success("Cambios guardados.")
        with col4:
            if st.button("Eliminar producto"):
                catalogo.pop(idx)
                guardar_catalogo_delivery(catalogo)
                st.success("Producto eliminado del catálogo.")
    else:
        st.info("No hay productos en el catálogo.")

    st.divider()
    st.subheader("Ventas registradas de delivery")
    ventas = cargar_ventas_delivery()
    if ventas.empty:
        st.info("Aún no hay ventas registradas.")
        return

    empleados = ["Todos"] + sorted(ventas["Usuario"].dropna().unique().tolist())
    año = st.number_input("Año (ventas)", min_value=2000, max_value=2100, value=date.today().year, key="anio_deliv")
    mes = st.number_input("Mes (ventas)", min_value=1, max_value=12, value=date.today().month, key="mes_deliv")

    filtro = ventas[(ventas["Fecha"].dt.year == año) & (ventas["Fecha"].dt.month == mes)]
    empleado_sel = st.selectbox("Empleado (ventas)", empleados)
    if empleado_sel != "Todos":
        filtro = filtro[filtro["Usuario"] == empleado_sel]

    if not filtro.empty:
        st.dataframe(filtro.sort_values("Fecha"))
        from utils import df_to_csv_bytes
        csv_bytes = df_to_csv_bytes(filtro)
        st.download_button(
            label="Descargar ventas de delivery (CSV)",
            data=csv_bytes,
            file_name=f"delivery_ventas_{empleado_sel}_{mes:02d}_{año}.csv".replace(" ", "_"),
            mime="text/csv"
        )
    else:
        st.warning("No hay ventas con ese filtro.")
