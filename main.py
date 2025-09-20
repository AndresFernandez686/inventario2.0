import streamlit as st
from persistencia import cargar_inventario, guardar_inventario, guardar_historial, cargar_historial
from ui_empleado import empleado_inventario_ui
from ui_admin import admin_inventario_ui, admin_historial_ui
from login import login

# Definición de productos por categoría, incluyendo "Por Kilos"
productos_por_categoria = {
    "Helados": {
        "Crocantino": 0.0,
        "Grido": 0.0,
        "Limón": 0.0,
        "Crema Americana": 0.0,
        "Dulce de Leche": 0.0,
        "Chocolate": 0.0,
        "Super Gridito": 0.0,
        "Tiramisu": 0.0,
        "Tramontana": 0.0,
        "Candy": 0.0
    },
    "Por Kilos": {
        "Vainilla": 0.0,
        "Chocolate": 0.0,
        "Fresa": 0.0,
        "Anana a la crema": 0.0,
        "Banana con Dulce de leche": 0.0,
        "Capuccino Granizado": 0.0,
        "Cereza": 0.0,
        "Chocolate Blanco": 0.0,
        "Chocolate con Almendra": 0.0,
        "Chocolate Dark": 0.0,
        "Chocolate Mani Crunch": 0.0,
        "Chocolate Suizo": 0.0,
        "Crema Americana": 0.0,
        "Crema Cookie": 0.0,
        "Crema Rusa": 0.0,
        "Dulce de Leche": 0.0,
        "Dulce de Leche con Brownie": 0.0,
        "Dulce de Leche con Nuez": 0.0,
        "Dulce de Leche Especial": 0.0,
        "Dulce de Leche Granizado": 0.0,
        "Durazno a la Crema": 0.0,
        "Flan": 0.0,
        "Frutos Rojos al Agua": 0.0,
        "Granizado": 0.0,
        "Kinotos al Whisky": 0.0,
        "Limon al Agua": 0.0,
        "Maracuya": 0.0,
        "Marroc Grido": 0.0,
        "Mascarpone con Frutos del Bosque": 0.0,
        "Menta Granizada": 0.0,
        "Naranja Helado al Agua": 0.0,
        "Pistacho": 0.0,
        "Super Gridito": 0.0,
        "Tiramisu": 0.0,
        "Tramontana": 0.0,
        "Candy": 0.0
    },
    "Extras": {
        "Cinta Grido": 0,
        "Cobertura Chocolate": 0,
        "Bolsa 40x50": 0,
        "Cobertura Frutilla": 0,
        "Cobertura Dulce de Leche": 0,
        "Leche": 0,
        "Cuchara Sunday": 0,
        "Cucharita Grido": 0,
        "Cucurucho Biscoito Dulce x300": 0,
        "Cucurucho Cascao x120": 0,
        "Cucurucho Nacional x54": 0,
        "Garrafita de Gas": 0,
        "Isopor 1 kilo": 0,
        "Isopor 1/2 kilo": 0,
        "Isopor 1/4": 0,
        "Mani tostado": 0,
        "Pajita con Funda": 0,
        "Servilleta Grido": 0,
        "Tapa Burbuja Capuccino": 0,
        "Tapa Burbuja Batido": 0,
        "Vaso capuccino": 0,
        "Vaso Batido": 0,
        "Vasito de una Bocha": 0,
        "Vaso Termico 240gr": 0,
        "Vaso Sundae": 0,
        "Rollo Termico": 0
    }
}

# Opciones de valde como texto literal
opciones_valde = {
    "Vacío": "Vacío",
    "Casi lleno": "Casi lleno",
    "Medio lleno": "Medio lleno",
    "Valde lleno": "Valde lleno"
}

def main():
    st.set_page_config(page_title="Heladería - Inventario", page_icon="🍦", layout="wide")
    usuario, rol = login()

    if not (usuario and rol):
        st.title("Por favor, ingresa un usuario válido en el panel lateral para continuar.")
        st.info("Usuarios de ejemplo: empleado1, empleado2, empleado3, admin1")
        return

    inventario = cargar_inventario(productos_por_categoria)

    if rol == 'empleado':
        empleado_inventario_ui(
            inventario, usuario, opciones_valde,
            guardar_inventario, guardar_historial
        )

    elif rol == 'administrador':
        tab_inv, tab_hist = st.tabs(["📦 Inventario", "📅 Historial"])
        with tab_inv:
            admin_inventario_ui(inventario)
        with tab_hist:
            admin_historial_ui(cargar_historial())

if __name__ == "__main__":
    main()
