# UI y lógica de empleados (Inventario)
import streamlit as st
from datetime import date
from utils import df_to_csv_bytes

def empleado_inventario_ui(inventario, usuario, opciones_valde, guardar_inventario, guardar_historial):
    st.header("Inventario")
    fecha_carga = st.date_input("Selecciona la fecha de carga", value=date.today(), key="fecha_inv")

    tabs = st.tabs(list(inventario.keys()))
    for i, categoria in enumerate(inventario.keys()):
        with tabs[i]:
            productos = inventario[categoria]
            producto_seleccionado = st.selectbox(
                f"Producto de {categoria}",
                list(productos.keys()),
                key=f"sel_{categoria}"
            )

            modo_actualizacion = st.radio(
                "¿Deseas añadir a la cantidad existente o reemplazarla?",
                ("Añadir", "Reemplazar"),
                key=f"modo_{categoria}_{producto_seleccionado}"
            )

            # ==========================
            # LÓGICA PARA "POR KILOS"
            # ==========================
            if categoria == "Por Kilos":
                st.markdown("### Cantidad de baldes a registrar:")
                num_baldes = st.number_input(
                    "Número de baldes",
                    min_value=1,
                    max_value=20,
                    value=len(productos[producto_seleccionado]) if isinstance(productos[producto_seleccionado], list) else 1,
                    step=1,
                    key=f"num_baldes_{producto_seleccionado}_{fecha_carga}_{usuario}"
                )

                # Eliminar baldes sobrantes de session_state si el número bajó
                for n in range(num_baldes + 1, 21):  # hasta 20 máximo
                    key_balde_sobrante = f"{producto_seleccionado}_balde_{n}_{fecha_carga}_{usuario}"
                    if key_balde_sobrante in st.session_state:
                        del st.session_state[key_balde_sobrante]

                estados_baldes = []
                for n in range(1, num_baldes + 1):
                    key_balde = f"{producto_seleccionado}_balde_{n}_{fecha_carga}_{usuario}"
                    if key_balde not in st.session_state:
                        valor_guardado = None
                        if isinstance(productos[producto_seleccionado], list) and len(productos[producto_seleccionado]) >= n:
                            valor_guardado = productos[producto_seleccionado][n-1]
                        st.session_state[key_balde] = valor_guardado if valor_guardado is not None else "Vacío"

                    opcion = st.selectbox(
                        f"Balde {n}",
                        list(opciones_valde.keys()),
                        index=list(opciones_valde.keys()).index(st.session_state[key_balde]) if st.session_state[key_balde] in opciones_valde else 0,
                        key=key_balde
                    )
                    estados_baldes.append(opcion)

                if st.button(
                    f"Actualizar {producto_seleccionado} ({categoria})",
                    key=f"btn_{categoria}_{producto_seleccionado}"
                ):
                    # Guardar solo la cantidad de baldes seleccionados
                    productos[producto_seleccionado] = estados_baldes.copy()
                    # Eliminar sobrantes si antes había más baldes guardados
                    if isinstance(productos[producto_seleccionado], list) and len(productos[producto_seleccionado]) > num_baldes:
                        productos[producto_seleccionado] = productos[producto_seleccionado][:num_baldes]

                    guardar_inventario(inventario)
                    guardar_historial(
                        fecha_carga, usuario, categoria, producto_seleccionado, estados_baldes, modo_actualizacion
                    )
                    st.success(f"Actualizado. Estado actual: {', '.join(estados_baldes)}")

                st.write("Inventario actual:")
                for p, c in productos.items():
                    if isinstance(c, list) and c:
                        estados = [x for x in c if x != "Vacío"]
                        if any(x == "Vacío" for x in c):
                            estados.append("Vacío")
                        st.write(f"- {p}: {', '.join(estados) if estados else 'Vacío'}")
                    else:
                        st.write(f"- {p}: Vacío")

            else:
                cantidad = st.number_input("Cantidad (unidades)", min_value=0, step=1, key=f"cant_{categoria}_{producto_seleccionado}")
                if st.button(
                    f"Actualizar {producto_seleccionado} ({categoria})",
                    key=f"btn_{categoria}_{producto_seleccionado}"
                ):
                    cantidad = max(0, int(cantidad))
                    if modo_actualizacion == "Añadir":
                        productos[producto_seleccionado] += cantidad
                    else:
                        productos[producto_seleccionado] = cantidad
                    guardar_inventario(inventario)
                    guardar_historial(
                        fecha_carga, usuario, categoria, producto_seleccionado, cantidad, modo_actualizacion
                    )
                    st.success(f"Actualizado. Nuevo stock: {productos[producto_seleccionado]}")

                st.write("Inventario actual:")
                for p, c in productos.items():
                    st.write(f"- {p}: {c if c > 0 else 'Vacío'}")
