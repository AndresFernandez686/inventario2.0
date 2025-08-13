#entrada de la app, orquesta de los modulos y las vistas
import streamlit as st
from datetime import date

from persistencia import (
    cargar_inventario, guardar_inventario, guardar_historial,
    cargar_historial, cargar_catalogo_delivery, guardar_catalogo_delivery,
    guardar_venta_delivery, cargar_ventas_delivery
)
from auth import login
from ui_empleado import empleado_inventario_ui, empleado_delivery_ui
from ui_admin import admin_inventario_ui, admin_historial_ui, admin_delivery_ui

# Datos base
productos_por_categoria = {
    "Impulsivo": {
        "Galletas": 0,
        "Chicles": 0,
        "Snack Salado": 0
    },
    "Por Kilos": {
        "Helado Vainilla": 0.0,
        "Helado Chocolate": 0.0,
        "Helado Fresa": 0.0
    },
    "Extras": {
        "Vasos": 0,
        "Cucharas": 0,
        "Servilletas": 0
    }
}

opciones_valde = {
    "Vacío": 0.0,
    "Casi lleno": 0.3,
    "Medio lleno": 3.5,
    "Valde lleno": 7.8
}

def main():
    st.set_page_config(page_title="Heladería - Inventario y Delivery", page_icon="🍦", layout="wide")
    usuario, rol = login()

    if not (usuario and rol):
        st.title("Por favor, ingresa un usuario válido en el panel lateral para continuar.")
        st.info("Usuarios de ejemplo: empleado1, empleado2, empleado3, admin1")
        return

    inventario = cargar_inventario(productos_por_categoria)

    if rol == 'empleado':
        tab_inv, tab_deliv = st.tabs(["🧊 Inventario", "🚚 Delivery"])
        with tab_inv:
            empleado_inventario_ui(
                inventario, usuario, opciones_valde,
                guardar_inventario, guardar_historial
            )
        with tab_deliv:
            empleado_delivery_ui(
                usuario, cargar_catalogo_delivery, guardar_venta_delivery, cargar_ventas_delivery
            )

    elif rol == 'administrador':
        tab_inv, tab_hist, tab_deliv = st.tabs(["📦 Inventario", "📅 Historial", "🛠️ Delivery"])
        with tab_inv:
            admin_inventario_ui(inventario)
        with tab_hist:
            admin_historial_ui(cargar_historial)
        with tab_deliv:
            admin_delivery_ui(
                cargar_catalogo_delivery, guardar_catalogo_delivery, cargar_ventas_delivery
            )

if __name__ == "__main__":
    main()
